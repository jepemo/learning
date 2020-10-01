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

## Implementación del repositorio en memoria y test de integración

* implementacion del repositorio en memoria
* En la capa de infraestructura. (Esta capa contiene)
  * E/S de datos
  * Partes de codigo que se acoplan a vendors externos
  * Que se necesite tolerancia al cambio, para falsea la implemnentacion
* Implementacion:

```java
public final class InMemoryCourseRepository implements CourseRepository {

    private HashMap<String, Course> courses = new HashMap<>();

    @Override
    public void save(Course course) {
        courses.put(course.id(), course);
    }

    public Optional<Course> search(String id) {
        return Optional.ofNullable(courses.get(id));
    }
}
```

* La interfaz no empieza con ningun prefijo "I" para evitar crear una interfaz "ICourseRepository" y luego implementacion "CourseRepository". 
  * Asi se fuerza a pensar en las implementaciones y no tener clases genericas.
  

* Test

```java
final class InMemoryCourseRepositoryShould {
    @Test
    void save_a_course() {
        InMemoryCourseRepository repository = new InMemoryCourseRepository();

        repository.save(new Course("some-id","some-name","some-duration"));
    }

    @Test
    void return_an_existing_course() {
      InMemoryCourseRepository repository = new InMemoryCourseRepository()
        Course course = new Course("some-id","some-name","some-duration");

        repository.save(course);

        assertEquals(Optional.of(course), repository.search(course.id()));
    }

    @Test
    void not_return_a_non_existing_course() {
      InMemoryCourseRepository repository = new InMemoryCourseRepository();
        assertFalse(repository.search("non-existing-id").isPresent());
    }
}
```
* En el primer testCase simplemente comprobaremos que no se produce ningún error cuando guardamos el nuevo curso en BD, mientras que en el segundo lo que haremos una vez persistido será llamar al método search() para comprobar que efectivamente se ha guardado en nuestro repositorio en memoria, comparando el Curso que hemos pasado en el save() y lo que nos devuelva la búsqueda (Recordemos que nos devolverá un Optional de Course)
* En nuestra opinión no vemos necesidad de eliminar el primer testCase pese a estar cubierto por el segundo porque de este modo, si falla al guardar saltará el error en ambos tests, mientras que si el problema está al recuperar sólo fallará el segundo test
* Finalmente también aprovechamos para comprobar que, si intentamos buscar un curso con un id no existente, no nos devolverá nada

## Test

En los Tests de Aceptación nos interesará mockear el acceso al repositorio para que se ejecuten más rápidos
- [ ] Cierto, para mejorar la velocidad en los tests
- [x] Falso, no mockearemos el repositorio
- [ ] Cierto, pero para no ensuciar la BD con las pruebas

(Lo que buscamos precisamente en estos tests es validar el flujo completo de la aplicación por lo que, aunque perdamos en velocidad, estaremos ganando en garantías)

Una de las ventajas que supone recibir el identificador del recurso en la propia petición de creación es...
- [ ] Que nos garantiza que el identificador no existe
- [ ] Ninguna, deberíamos delegar esta responsabilidad a la implementación del repositorio
- [x] Que no será necesario enviarlo en la respuesta de vuelta al cliente

(Puesto que el cliente conoce el id en el momento de enviar la petición, ya no será necesario que este espere recibirlo en la respuesta, ganando por su parte en integridad, y en mantenimiento y cambiabilidad en el backend)

Si una parte de código está inevitablemente acoplada a un vendor externo, deberíamos mantenerla en..
- [ ] En el Caso de Uso, para no duplicar este acoplamiento por cada punto de entrada
- [ ] En la capa de Dominio, lo más profundo posible
- [x] En la capa de Infraestructura, lejos de nuestro Dominio

(Llevaremos a Infraestructura aquel código que toque entrada/salida de datos, se acople a un vendor externo, o que necesitemos falsear su implementación en tiempo de test)
