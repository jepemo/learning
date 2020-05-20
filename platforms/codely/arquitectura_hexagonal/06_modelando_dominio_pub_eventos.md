# Modelando nuestro dominio y publicando eventos

## Teoria

* Value objects: Son clases que se identifican por el valor que representan.
  * Porque no utilizar datos primitivos? Con los valueObjects podemos hacer validaciones sobre el tipo (por ejemplo si es una URL, validar que sea una)
  * Es decir, aporta **semántica de dominio**: Tener nuestros propios tipos con conceptos de dominio como VideoUrl, UserRange, Rating, etc. nos ayudará a que el código sea más legible y a que nuestro código exprese mejor los conceptos de nuestro dominio.
  * Cohesión: Desde el momento en el que tenemos una clase para modelar las URLs de los vídeos, la lógica relacionada estará autocontenida en esta clase. De tal forma que la lógica está mucho más cerca de los datos que necesita. Esto redunda en los 2 beneficios que comentamos en el vídeo:
    * Evitar comprobaciones redundantes: Desde el momento en el que me llega algo de tipo VideoUrl, me puedo ahorrar todas las comprobaciones que podría llegar a tener duplicadas a lo largo de mi código al respecto. Es decir, en el momento de instanciación del VideoUrl es cuando validaremos que sea una URL válida, con lo cuál, podremos dar esto por hecho en el momento de recibir una instancia de la clase y evitar tener que comprobar si es null.
    * Imán de lógica: La primera vez que introducimos un determinado VO en nuestro sistema puede que no le veamos mucho sentido quizá, pero a medida que exploramos la aplicación seguro nos iremos encontrando con pequeñas porciones de lógica que, por falta de no tener un lugar ideal donde ubicarlas, las hemos implementado en servicios o modelos que han engordado demasiado.
  * Hacer esto nos ayuda a mover la logica que acompaña los valores dentro de estas clases.
  * Ejemplo:
  ```php
  final class VideoUrl extends StringValueObject
{
    public function __construct(string $value)
    {
        $this->guardValidUrl($value); // ℹ️ Validación en el momento de instanciación. No permitimos tener un VideoUrl con un null por ejemplo.

        parent::__construct($value);
    }

    private function guardValidUrl(string $url)
    {
        if (false === filter_var($url, FILTER_VALIDATE_URL)) {
            throw new \InvalidArgumentException(sprintf('The url <%s> is not well formatted', $url));
        }
    }
}
  ```
* Entidad
  * Compuesta por valueobjects
  * Se suelen utilizar "NamedConstructors" para instanciar las entidades. Así tambien podemos hacer mas acciones, como registrar los eventos involucrados en la creacion.
* Ejemplo de la publicacion del evento despues de llamar al constructor semantico:
```php
final class VideoCreator // ℹ️ Servicio de Aplicación / Caso de uso de crear nuevo vídeo!
{
    private $repository;
    private $publisher;

    public function __construct(VideoRepository $repository, DomainEventPublisher $publisher)
    {
        $this->repository = $repository;
        $this->publisher  = $publisher;
    }

    public function create(VideoId $id, VideoTitle $title, VideoUrl $url, CourseId $courseId)
    {
        $video = Video::create($id, $title, $url, $courseId); // ℹ️ Creamos el vídeo (¡Sólo registrando el evento, no publicándolo!)

        $this->repository->save($video); // ℹ️ Guardamos el vídeo en nuestro sistema de persistencia

        $this->publisher->publish(...$video->pullDomainEvents()); // ℹ️ Obtenemos los distintos eventos que se han podido registrar en la entidad, y los publicamos
    }
}
```

## Test

Siguiendo lo visto en esta lección, ¿qué firma de las siguientes sería la más adecuada?
- [ ] CourseRenamer#rename(renamerId: String, courseId: String, newName: String, reason: String)
- [ ] CourseRenamer#rename(renamerId: RenamerId, courseId: CourseId, newName: String, reason: String)
- [x] CourseRenamer#rename(renamerId: RenamerId, courseId: CourseId, newName: CourseName, reason: CourseRenameReason)
- [ ] CourseRenamer#rename(renamerId: String, courseId: String, newName: CourseName, reason: CourseRenameReason)

¿Desde dónde registraremos los eventos de dominio?
- [x] Desde la entidad y método donde se produzcan
- [ ] Desde el caso de uso donde se produzca

¿Desde dónde publicaremos los eventos de dominio?
- [ ] Desde la entidad y método donde se produzcan
- [ ] Desde un servicio de dominio intermedio que haga la modificación en la entidad y publique el evento ya que es éste quien representa la barrera a nivel de transacciones y publicación de eventos
- [x] Desde el caso de uso o Application Service ya que es éste quien representa la barrera a nivel de transacciones y publicación de eventos



