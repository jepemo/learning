# Patrón Repository

## Refactorizando Student Sign Up aplicando repositorio

* Se va a incluir el patron "Repository" al ejemplo que teniamos antes.
* Para abstraer en el  "caso de uso" la forma de almacenar los datos.
  * Es decir: "extraer la lógica de almacenamiento a la infraestructura"
* Clase StudentSignUpper:

```php
final class StudentSignUpper
{
    private static $students = [];

    public function __invoke(string $studentId, StudentName $name, StudentPassword $password)
    {
        $this->ensureStudentDoesntExist($studentId);

        $student = new Student ($studentId, $name, $password);

        self::$students[$studentId] = $student;
    }

    private function ensureStudentDoesntExist($studentId): void
    {
        $existentStudent = get($studentId, self::$students);

        if(null !== $existentStudent){
            throw new StudentAlreadyExist($studentId);
        }
    }
}
```

* Primero refactorizar para sacar la parte del guardado:

```php
final class StudentRepositoryInMemory
{
    private static $students = [];

    public function save(Student $student){
        self::$students[$student->studentId()] = $student;
    }

    public function search(StudentId $id): ?Student
    {
        return get($id->value(), self::$students)
    }
}
```
* El repositorio se pasa como dependencia al caso de uso.
* Los repositorios siempre interaccionan con "AgregateRoot".
  * Es decir, los reciben por parametro y los devuelven.
  * Si no hicieramos esto, permitiríamos que desde los clientes se interactuase con los elementos que están dentro del Aggregate Root y estaríamos rompiendo con las reglas de consistencia que permiten gestionarlo

* Con lo que al final StudentSignUpper queda:

```php
final class StudentSignUpper
{
    private $repository; 

    public function __construct(StudentRepositoryInmemory $repository)
    {
        $this->repository = $repository;
    }

    public function __invoke(StudentId $id, StudentName $name, StudentPassword $password)
    {
        $this->ensureStudentDoesntExist($id);

        $student = new Student ($id, $name, $password);

        $this->repository->save($student);
    }

    private function ensureStudentDoesntExist($studentId): void
    {
        $existentStudent = $this->repository->search($studentid);

        if(null !== $existentStudent){
            throw new StudentAlreadyExist($studentId);
        }
    }
}
```

* En este ejemplo se esta inyectando directamente la dependencia de memoria del repositori. Pero lo ideal seria inyectar por interfaz con inversion de dependencias.
* Por lo tanto al final el flujo es:
  * El controlador recibe la request
  * Convierte a ValueObjects a traves de los parametros "string" de entrada.
  * Con estos VO se llama al ApplicationService (Caso de uso)
  * El AS inyecta el repositorio
  * En el caso de uso se hace lo que se tenga que hacer y se interactua con el repositorio para guardar/recuperar agregados.
  
## Role interfaces vs Header interfaces

* El ejemplo que teniamos antes, esta usando la implementacion concreta:

```php
final class StudentSignUpper
{
    private $repository; 

    public function __construct(StudentRepositoryInmemory $repository)
    {
        $this->repository = $repository;
    }

    // ...
}
```

Esta se va a invertir, se crea una interfaz (en el dominio):

```php
interface StudentRepository
{
    public function save(Student $student): void;

    public function search(StudentId $id): ?Student
}
```

Y se inyecta con esta interfaz:

```php
final class StudentSignUpper
{
    private $repository; 

    public function __construct(StudentRepository $repository)
    {
        $this->repository = $repository;
    }

    // ...
}
```


* Este acoplamiento que teníamos de Infraestructura dentro del Application Service, además de suponer un ‘smell’, nos suponía una falta de tolerancia al cambio y un alto coste de Entrada/Salida a BD en tiempo de Test. Gracias a este refactor si que podremos mockear esa Entrada/Salida, por lo que nuestros tests se ejecutarán mucho más rápido y se limitarán a comprobar que el comportamiento sea correcto.
* Pero no se trata simplemente de extraer una interface para invertir esas dependencias, a nivel estructural tampoco debemos mantenernos acoplados por unas firmas de métodos que estén condicionadas por implementaciones concretas (como podría ser pasar por parámetro una key porque estemos pensando en una implementación con Redis), puesto que el cliente no tiene que conocer los detalles de nuestra implementación
* Algo que nos ayudará a hacer que los métodos del Repositorio sean agnósticos a la implementación es el uso del Patrón Criteria que vimos en el curso de SOLID
* Lo importante de todo esto es que el cómo definimos las interfaces venga establecido por los clientes, las interfaces cumplen con un rol, en este caso el de ser el repositorio de Student, y deben ser agnósticas a cualquier implementación que haya por debajo. No son Header Interfaces a nivel de generar unas interfaces en base a las cabeceras de las implementaciones
* A modo de síntesis podemos condensar la idea que queremos transmitir en este video en que Las interfaces pertenecen a los clientes, para evitar Leaks de infraestructura en nuestra aplicación, lo mejor es no conocer la infraestructura.
* [El Arte del Patadón Pa’lante](https://youtu.be/AQK_YgFj7Ng) Presentación de Eduardo Ferro acerca de la importancia de postergar las decisiones de detalles de implementación al último momento responsable

## Comunicar modules y Bounded Contexts: Repositories vs Application Service

### Comunicación entre Modules y BC via AS vs Repos

* Pros y contras de inyectar repositorios / servicios

#### Inyectando VideoRepository

* En el primer caso, se esta inyectado el repositorio de otro dominio (Video) en este (VideoComment).
* Codigo:

```php
public class VideoCommentPublisher
{
    private $videoCommentRepository;
    private $videoRepository
    private $publisher;

    public function __construct(VideoCommentRepository $videoCommentRepository, VideoRepository $videoRepository, DomainEventPublisher $pubblisher)
    {
        $this->$videoCommentRepository = $videoCommentRepository;
        $this->videoRepository = $videoRepository;
        $this->publisher = $publisher;

    }

    public function publish(VideoCommentId $id, VideoId $videoiD, VideoCommentContent $content)
    {
        $this->ensureVideoExist($videoId);

        $comment = VideoComment::publish($id, $videoId, $content);

        $this->repository->sasve($comment)

        $this->publisher->publish(...$comment->pullDomainEvents())
    }

    private function ensureVideoExist(VideoId $id): void
    {
        $video = $this->videoRepository->search($id)

        if(null ==== $video)
        {
            throw new VideoNotFound($id)
        }
    }
}
```

* En una primera iteración vamos implementar el método ensureVideoExist inyectando el repositorio. Pero ¡ojo! 👀 estamos inyectando el repositorio de Video, referenciando desde un módulo al dominio de otro módulo
* Como pros de esta implementación tendremos, para empezar, que ya tendríamos completada la feature propuesta y podremos comprobar si el video existe. Sin embargo, estaríamos duplicando esta lógica en distintos puntos del código. Además, otro problema con esta implementación es que estamos generando un mayor acoplamiento con otros módulos (recordemos que nuestro objetivo es que Bounded Contexts y Módulos sean fácilmente modificables)

#### Inyectando VideoFinder

* Codigo:

```php
public class VideoCommentPublisher
{
    private $repository;
    private $finder
    private $publisher;

    public function __construct(VideoCommentRepository $repository, VideoFinder $finder, DomainEventPublisher $pubblisher)
    {
        $this->$repository = $repository;
        $this->finder = $finder;
        $this->publisher = $publisher;

    }

    public function publish(VideoCommentId $id, VideoId $videoiD, VideoCommentContent $content)
    {
        $this->ensureVideoExist($videoId);

        $comment = VideoComment::publish($id, $videoId, $content);

        $this->repository->sasve($comment)

        $this->publisher->publish(...$comment->pullDomainEvents())
    }

    private function ensureVideoExist(VideoId $id): void
    {
        $this->finder->__invoke($id)
    }
}
```

* Aunque sigue habiendo acoplamiento con el módulo de Video, el hecho de inyectar el Servicio de Dominio nos hace ganar en términos de no tener la lógica duplicada en diferentes puntos
* Por otro lado, estas iteraciones nos estan dejando ver que VideoId es un candidato perfecto para ser empujado a Shared puesto que estamos haciendo uso de él desde distintos módulos. En el caso de que fueramos a seguir compartiendo VideoFinder entre distintos módulos, también sería un buen candidato, pero como veremos en los siguientes videos, dejaremos de llamar a este servicio desde otros módulos distintos a Video.
