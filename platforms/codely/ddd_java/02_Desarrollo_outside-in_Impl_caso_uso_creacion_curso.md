# Desarrollo Outside-in: Implementación del caso de uso para crear curso

## Implementación del test de aceptación y controller

* El cliente tendra la responsabilidad de crear el ID del curso (CQRS)
* Primero se crea el test de aceptacion (Outside-in)

```java
public final class CoursesPutControllerShould extends MoocApplicationTestCase {
    @Test
    void create_a_valid_non_existing_course() throws Exception {
        assertRequestWithBody(
            "PUT",
            "/courses/1aab45ba-3c7a-4344-8936-78466eca77fa",
            "{\"name\": \"The best course\", \"duration\": \"5 hours\"}",
            201
        );
    }
}
```

* El codigo 201, es que el recurso se ha creado "CREATED".
* Luego se crea el controlador ("CoursesPutController"), en la plataforma de Mooc:

```java
@RestController
public final class CoursesPutController extends ApiController {

    @PutMapping(value = "/courses/{id}")
    public ResponseEntity create(
        @PathVariable String id,
        @RequestBody Request request
    ){
        return new ResponseEntity<>(HttpStatus.CREATED);
    }
}

final class Request {
    private String name;
    private String duration;

    // ...
}
```

* En Spring la forma mas "limpa" de capturar los parametros del body es crear un objeto "Request" con los nombres de los mismos campos.

## Implementación del test unitario y caso de uso

* Implementacion del test unitario del servicio, para poder reutilizarlo sea quien sea el cliente HTTP, CLI, etc.
* Crear los directorios para la logica: tv.codely.mooc.courses.{application, domain, infraestructure}. Lo anterior estaba en las "apps".
* En "aplication" creamos el directorio "create", para este caso de uso.
* Luego la clase "CourseCreator"

```java
@Service
public final class CourseCreator {
    private final CourseRepository repository;

    public CourseCreator(CourseRepository repository) {
        this.repository = repository;
    }

    public void create(String id, String name, String duration) {
        Course course = Course.create(id, name, duration);

        repository.save(course);
    }
}
```

* En el controlador, se inyectaria el "CourseCreator":

```java
public final class CoursesPutControler
{
    private CourseCreator creator;
    
    public CoursesPutController (CourseCreator creator) {
        this.creator = creator;
    }
    
    @PutMapping(value = "/courses/{id}")
    public ResponseEntity create(
        @PathVariable String id,
        @RequestBody Request request
    ){
        creator.create(id, request.name(), request.duration());
        return new ResponseEntity<>(HttpStatus.CREATED);
    }
}
```

* En el dominio, creamos el repositorio (CourseRepository):

```java
public interface CourseRepository
{
    void save(Course course);
}

// Tambien la entidad
public final class Course
{
 private String id;
 private String name;
 private String duration;
 
 public static Course create(String id, String name, String duration)
 {
    return new Course(id, name, duration);
 }
 
 // getters (se initializa por constructor)
}
```

* Y el test:

```java

final class CourseCreatorShould
{
    @Test
    void save_a_valid_course() throws Exception 
    {
        CourseRepository courseRepository = Mock(CourseRepository.class);
        CourseCreator creator = new CourseCreator(courseRepository);
        
        Course course = new Course("some-id", "some-name", "some-duration");
        
        creator.create(course.id(), course.name(), course.duration());
        
        // Comprueba que se ha llamado almenos una vez a un metodo del repository
        verify(repository, atLeatOnce()).save(course);
    }
}
```




