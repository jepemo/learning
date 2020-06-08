# Arquitectura Hexagonal

## Flujo de una petición en Arquitectura Hexagonal

* Un concepto de dentro del DDD son las "Layered Architectures"
  * Una de esas "Layered Architectures" es la "Hexagonal Architecture"
  * De todas las arquitecturas por capas que existen es de las que mejores escalan (a nivel de rendimiento y equipos)
* Capas:
  * Infraestructura: E/S (BBDD, WS, Ficheros, etc) y librerias acopladas a vendors externos
  * Application: Casos de uso, empapándose de toda la semántica de negocio. Actuará como una barrera transaccional en términos(tanto en términos de BD como de publicación de eventos)
  * Dominio: Representa el modelado de nuestro negocio (Principalmente Value Objects y Entitades), en esta capa encontraremos también los servicios de dominio.
* La regla de dependencia es que la comunicacion de las capas de de fuera hacia dentro:
  * Infraestructura -> Aplicacion -> Dominio (<-)
* Flujo:
  * El flujo parte de una petición recibida por el Controller (Infraestructura) desde el que se enviaría al Application Service.
  * En este punto plantearíamos dos alternativas, una de ellas es que el Application Service sea quien montara los Value Objects a partir de los datos primitivos recibidos desde el Controller. Por otro lado, tal como vimos en el curso de CQRStambién podríamos hacer que ese mapeo se llevara a cabo a través un Bus (Command Bus o Query Bus) que los enviaría al Application Service
  * Desde el Application Service se llamaría a los distintos Services, Models y Repositories.
  * Es importante señalar aqui que la capa de aplicación se comunicaría con una Interfaz del repo de la capa de dominio, mientras que la implementación de dicha Interfaz estará dentro de la capa de Infraestructura siguiendo el Patrón Adaptador

```
                                         (Dominio)                (Infra)
     (Infra)        (Aplicacion)     -> Services
-> Controller -> Application Service -> Models
                                     -> Repos (Interfaz)  <----- Implementacion
```

## Nuestro primer caso de uso: Student Sign Up

* Caso de uso:
  * Llegará una request al Controlador StudentPutController
  * Desde el Controlador se llamará al Servicio de Aplicación StudentSignUpper. Este servicio interactuará con
    * El Servicio de Dominio StudentFinder para comprobar si ya existe ese usuario
    * El Agregado Student, entendido en este caso como una Entidad
    * El repositorio StudentRepository donde se almacenará el estudiante
    
```
    (Infra)                  (Apli)            (Dominio)
-> StudentPutController -> StudentSignUpper -> StudentFinder (servicio de dominio)      (Infra)
                                            -> Student                         
                                            -> StudentRepository <------------------- InMemoryStudentRepository
```
* Implementacion simple de A. Hexagonal:
  * Partiendo para ir probando con el test:
  
```

Feature: Sign up a student
  In order to learn from CodelyTV Pro courses
  As an anonymous student
  I want to sign up to the platform

  Scenario: Sign up a new student
    Given I send a PUT request to "/students/0ca24fc4-bdc8-48d0-9c5f-94183a627adc" with body:
    """
    {
      "name": "javi",
      "password": "superSecret"
    }
    """
    Then the response status code should be 201
    And the response should be empty
```

Clase StudentPutController:

```php
final class StudentPutController extends ApiController
{
    private $signUpper;

    public function __construct(StudentSignUpper $signUpper)
    {
        $this->signUpper = $signUpper;
    }

    public function __invoke(string $id, Request $request)
    {
        $this->signUpper->__invoke($id, $request->get('name'),$request->get('password'));

        return new ApiHttpCreatedResponse();
    }
}
```

Caso de uso:

```php
final class StudentSignUpper
{
    private static $students = [];

    public function __invoke(string $studentId, string $studentName, string $studentPassword){
        $existentStudent = get($studentId, self::$students);
        
        if(null !== $existentStudent)
        {
            throw new StudentAlreadyExist($studentId)
        }

        $student = new Student($studentId,$studentName,$studentPassword);

        self::$students[$studentId] = $studentId;
    }
}
```

Clase Student:

```php
final class Student
{
    private $studentId;
    private $studentName;
    private $studentPassword;
    
    public function __construct(string $studentId, string $studentName, string $studentPassword)
    {
        $this->studentId = $studentId;
        $this->studentName = $studentName;
        $this->studentPassword = $studentPassword;
    }
    
    // Getters y setters
}
```

* Dentro del invoke de este servicio estaríamos comprobando si el estudiante ya existe, lanzando en ese caso una excepción StudentAlreadyExist. Ojo 👀! Se trata de una excepción de dominio, por lo que la crearemos dentro de la carpeta Domain junto a las demás clases de dominio de este módulo; con esto estaremos ganando en semántica dentro de nuestra aplicación.

* En caso de que no exista, simplemente lo persistiríamos en base de datos o, en nuestro caso de ejemplo, en memoria. Vemos como una vez registrado el nuevo estudiante no estamos devolviendo nada, en nuestra opinión las mutaciones del estado global de nuestra aplicación deberían hacerse sin retornar nada por temas de separación de responsabilidades (inspirado en el enfoque de CQRS)
  
