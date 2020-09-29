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
