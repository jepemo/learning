# Entidades, Agregados, y Aggregate Root

## Introducción a agregados - Problemas de El Mundo Real™️

* Modelo de dominio
* Se parte de la entidad base. En el ejemplo: Curso
* Esta compuesta por:
  * Rating del curso
  * Resumen
  * Descripción
  * Total de steps
  * Total de videos
  * Lecciones
  * Steps
* Estos se corresponderian con los value objects y entidades:
  * (VO) Id
  * (VO) Rating
  * (VO) Summary
  * (VO) Description
  * (Entidad) Lessons
  * etc.
* Clase Course:

```php
final class Course
{
    private $id;
    private $rating;
    private $summary;
    private $description;
    private $lessons;
    
    public function __construct(
        CourseId $id,
        CourseRating $rating,
        CourseSummary $summary,
        CourseDescription $description,
        Lessons ...$lessons)
    {
        $this->id = $id;
        $this->rating = $rating;
        $this->summary = $summary;
        $this->description = $description;
        $this->lessons = $lessons;
    }
}

    // Tell don't ask
    // Devuelve directamente el total steps a partir de los datos internos
    // Asi no se expone el Lesson fuera.
    public function totalSteps(): CourseTotalSteps
    {
        $totalSteps = new CourseTotalSteps();

        foreach ($this->lessons as $lesson)
        {
            $totalSteps = $totalSteps->add($lesson->totalSteps())
        }
    }
```

* Clase Lessons:

```php
public class Lesson
{
    // ...
    public function totalSteps(): LessonTotalSteps
    {
        return new LessonTotalSteps(count($this->steps));
    }
   
}
```

* Una siguiente mejora respecto a éste cálculo podría ser llevárnoslo al propio constructor de la clase, con sus propias claúsulas de guarda (Tal como vimos en el video anterior), asegurándonos de que no habrá una instanciación inválida del modelo.

### Relación entre entidades

* Con lo visto hasta ahora, podríamos decir que Course no deja de ser una entidad más que se está relacionando de forma directa con otras entidades, lo que habitualmente vendría definiendose en los ORM como un oneToMany o manyToMany dentro de nuestra clase. Esta relación al final implicará que cuando hagamos una consulta select course… nos acabe explotando la BD por la query tan grande que le estaríamos lanzando
  * Curso tiene dentro Lessons
* Una alternativa a esto sería la definición de un Aggregate, que no sería más que un elemento conceptual que engloba distintas entidades, de tal modo que siempre que queramos interactuar con Lessons, por ejemplo, lo haremos a través de Course.
  * Si queremos acceder al nombre de la lección no haremos una llamada del tipo “course->lesson->name” sino que lo haremos a través de un método “lessonName()” (no nos acoplaremos a cada uno de estos elementos encadenados)
* Dentro de este Aggregate tendremos un Aggregate Root, que en este caso será Course
* Ejemplo:
  * Curso (Agregado)
    * Curso (AggregateRoot)
    * Id (VO)
    * Lessons (Entidad)
    * Summary (VO)
    * Description (VO)
    * Review (Entidad)
      * Id (VO)
      * Comment (VO)
      * Rating (VO)
      * StudentId (VO)
* Codigo:

```java
final public class Course extends AggregateRoot {
    private final CourseId id;
    private final CourseName name;
    private final List<Review> reviews;

    public Course(CourseId id, CourseName name, List<Review> reviews){
        this.id = id;
        this.name = name;
        this.reviews = reviews;
    }
    public CourseId id() {
      return id;
    }
    public CourseName name() {
      return name
    }
}

...
public Review (
    ReviewId id,
    Rating rating,
    Comment comment,
    StudentId studentId
)
...
```

* Aquí podemos ver nuestro Aggregate Course, y cómo en el constructor de clase instanciamos sus atributos (para simplificar en esta ocasión no hemos añadido Lessons), de modo que estaríamos levantando todas las Review de un curso en el momento de levantar el propio curso.
* El problema que nos surge aquí es que si las entidades Lessons y Review crecen y las mantenemos dentro del aggregate, el consumo en BD será tremendo y lo mismo nos sucederá a la hora de cargarlos en memoria cuando los recuperamos
* No obstante, aunque hemos hablado de los problemas de usarlos, recordemos que el Aggregate y el Aggregate Root nos van a ofrecer unos beneficios
  * Encapsulación, siguiendo Tell Don’t Ask, nos va a permitir que los clientes no se vean afectados si en algún momento quisieramos cambiar cómo funciona todo de forma interna
  * Mantener las restricciones de integridad síncronas que se establezcan dentro del agregado
