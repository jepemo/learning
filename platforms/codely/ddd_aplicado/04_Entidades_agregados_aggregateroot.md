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
  
## Aggregate root vs Entity: Ejemplo Video y VideoHighlight

* El problema que tenemos en el siguiente curso es que el agregado ha crecido mucho. Tiene internamente entidades, que pueden dar problemas para recuperar, etc.
* Por lo que al siguiente codigo, clase course:

```java
final public class Course extends AggregateRoot {
    private final CourseId id;
    private final CourseName name;
    private final CourseRating rating;

    public Course(CourseId id, CourseName name, CourseRating rating){
        this.id = id;
        this.name = name;
        this.rating = rating;
    }
    // ...
}
```

* Se tendra que extraer la clase Review a otro agregado:

```java
public final class Review extends AggregateRoot {
    private final StudentId studentId;
    private final CourseId courseId;
    private final CourseReviewRating rating;
    private final ReviewComment comment;

    public Review(StudentId studentId, CourseId courseId,CourseReview Rating rating,ReviewComment comment){
        this.studentId = studentId;
        this.courseId = courseId;
        this.rating = rating;
        this.comment = comment;
    }
    // ...
}
```

*  Ahora Review es un elemento independiente cuya relación con el Curso será simplemente a través de un courseId, de modo que ni el curso sabrá qué reviews tiene, ni las reviews sabrán a qué curso pertenecen, por lo que no necesitaremos levantar todo el curso de BD, sino solo el valor del identificador de ese curso (Relación entre clases por identificador)
* Podemos ver en estas clases cómo estamos manteniendo dos Value Objects diferentes para el Rating, hemos decidido hacerlo de este modo porque podríamos querer que cada uno tuviera una lógica distinta, por ejemplo, computar el valor de CourseRating en base al valor de un CourseReviewRating
* Agregados:
  * Course (Agregado)
    * Course (AggregateRoot)
    * Id (VO)
    * Rating ->  se ha calculado a partir de los rating de los "CourseReview"
    * Summary (VO)
    * Description (VO)
  * CourseLesson (Agregado)
    * CourseLesson (AggregateRoot)
    * Id (VO)
    * CourseId (VO)
    * Title (VO)
    * Description (VO)
    * Duration (VO)
    * Order (VO)
    * Scheduled (VO)
  * CourseReview (Agregado)
    * CourseReview (AggregateRoot)
    * Id (VO)
    * Rating (VO)
    * StudentId (VO)
    * Comment (VO)
    
* Al igual que con las reviews del curso, también extraeremos las lecciones como Aggregate CourseLesson, de modo que nuestro Course queda como una clase mucho más pequeña y ‘tonta’, facilitándo así su mantenibilidad. Además, en términos transaccionabilidad, tener agregados más pequeños reducirá los posibles bloqueos en BD y hará que las consultas sean mucho más rápidas
* El hecho de extraer estos agregados, podía generar algunos problemas, pero veremos que solución podemos darle a cada uno de ellos:

### Asegurando consistencia en CourseLessons

* Validar orden entre lecciones: Aquí al ser una validación que debemos ejercer previamente a ejecutar el caso de uso ya que si no, éste no se debería poder llevar a cabo, haremos la consulta de forma previa encapsulándola en un **Domain Service**.
  * Para comprobar que no se insertaran dos lecciones con el mismo "orden", este por ejemplo, recuperaria todas las lecciones y comprobaria que se valida esta condicion. 
  * En vez de coordinar esto en el agregado, se haria con el "domain service".
  

### Asegurando consistencia en Course

* Incrementar total steps y videos: Aquí la estrategia será gestionar este tipo de tareas y cómputos de forma asíncrona por medio de **Eventos de Dominio** que nos permitan además una mayor performance a la hora de recuperar la información de BD

### Estructura
* src/Mooc
  * Reviews
  * Courses
    * Application
      * Create
        * CourseCreator.x
        * CreateCourseCommand.x
        * CreateCourseCommandHandler.x
    * Domain
      * Course.x
      * CourseCreatedDomainEvent.x
      * CourseDescription.x
      * CourseRepository.x
      * CourseTitle.x
    * Infraestructure
      * Persistence
        * CourseRepositoryMySql.x
* Finalmente, estos agregados estarían contenidos en un módulo (normalmente la relación será de un módulo por cada agregado, con lo que respetaremos el SRP de SOLID). Dentro de cada módulo, a su vez, encontraremos los directorios de Application, Domain e Infraestructure siguiendo el diseño de Arquitectura Hexagonal
* A nivel Bounded Context:
  * MOOC (BC)
    * Courses (modulo)
      * Courses (Agregado)
    * CourseReview (modulo)
      * CourseReview (agregado)
    * CourseLessons (modulo)
      * ...
    * Students (Modulo)
      * ...
    * Paths (modulo)
    * Roadmap (modulo)

## Fallando miserablemente modelando Agregados

* El ejemplo que explican, es en un proyecto, de una Web/Tienda de Vinos, tenian que modelar el menu (que tiene filtros, categorias, etc). Por lo que se definio como Agregado el "Menu" y como agregateRoot "menu". A su vez este tendria: idioma, tab, los tab tendrian "Filter" y estos los links.
* Ejemplo:
  * Menu (Aggretate)
    * Menu (AggregateRoot)
      * Tab (Entidad)
        * Filter (Entidad)
          * Link (VO)
* Para añadir un link, hay que hacer mucha logica. Además de todas las operaciones de gestionar: Tabs, filtros, etc.
* Que fallo?
  * ¿CRUD era suficiente?
    * Distintas representaciones del menú en distintos idiomas con reglas complejas
    * Es decir, habia mucha logica por debajo, por lo que mejor no utilizar CRUD.
  * ¿Se podría haber evitado niveles de encapsulación?
    * Validación no más de X elementos dependiente de otros
    * No por evento (acción ya realizada)
    * Si por query/caso de uso
  * ¿Y entonces tendríamos N consultas?
    * ¡Read Model!
    
    
