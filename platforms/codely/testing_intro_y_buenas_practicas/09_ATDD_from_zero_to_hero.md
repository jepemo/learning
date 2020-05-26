# ATDD From zero to hero: Live coding

## Introducción a ATDD e implementación del test de aceptación

* Aceptacion TDD
* Flujo desarrollo?
  * Primero se hace el test de aceptacion
  * Este falla
  * Se hace un test unitario que falla
  * Falla
  * se arregla el test unitario
  * Se arregla el test de aceptacion
* El ejemplo:

```
Given I send a GET request to "/students/fe7017d0-9e8f-4952-e047e36b1694"
Then the response status code should be 200
And the response content should be:
"""
{
  "id": "fe7017d0-9e8f-4952-e047e36b1694",
  "total_pending_videos: 5,
  "name": "Vincenc"
}
"""
```
  * El ejemplo es para devolver la informacion de un usuario
  * El test de aceptacion define el "happy path"
    * A partir de una url (en el que va el id del usuario)
    * Devuelve un json con la informacion de este
    * nos permitirá establecer los contratos desde el principio y poder paralelizar desarrollos
  * El test falla (Porque falta codigo por implementar)
    * El desarrollo del test de aceptación nos ayuda a definir el lenguaje ubicuo y el tipo de contenido
  * Se implementa ese codigo (StudentGetController)
    * Desde el Controller llamaremos al caso de uso, por lo que nos llevará a plantear los tests unitarios
    
## Implementación del test unitario del caso de uso y cierre de círculos

* Siguiente con los pasos anteriores
* Se implementa el test del codigo del caso de uso (application service)

```php
public function it_should_find_an_existing_student()
{
    $finder = new StudentFinder();

    $student = StudentMother::random();

    $this->assertSame($student, $finder($student->id()));
}
```

  * Luego tengo que implementar el codigo para uqe pase este test (Clase StudentFinder):
  
```php
public function __invoke(StudentId $id): Student
{
    return $this->repository->search($id);
}
```
  
* Hay que modificar el test porque hay que inyectar el repositorio:

```php
public function it_should_find_an_existing_student()
{
    $finder = new StudentFinder($this->repository());

    $student = StudentMother::random();

    $this->shouldSearchStudent($student->id(), $student);

    $this->assertSame($student, $finder($student->id()));
}
```

* Ahora si se prueba el test de aceptacion, debería funcionar.

* Como en el de aceptacion solo se implementa el "happy path", para el test unitario, habria que tener en cuenta el caso del error (que no encuentre el usuario):

```php
public function it_should_not_find_a_non_existing_student()
{
    $this->expectException(StudentNotExist::class);

    $finder = new StudentFinder($this->repository());

    $student = StudentMother::random();

    $this->shouldSearchStudent($student->id(), null);

    $finder($student->id());
}
```

* Lo que hara que haya que modificar el "StudentFinder":

```php
public function __invoke(StudentId $id): Student
{
    $student = $this->repository->search($id);

    if(null === $student)
    {
        throw new StudentNotExist($id);
    }

    return $student;
}
```

* Finalmente volveríamos a lanzar el test de aceptación para validar que el flujo completo para este escenario funciona correctamente (En este caso ya hemos implementado a nivel del controlador el parseo de la excepción a un error 404 del protocolo HTTP)

## Test

ATDD nos plantea un enfoque muy similar a TDD pero...
- [ ] Sustituyendo los tests unitarios por tests de aceptación
- [x] Envolviendo el flujo de tests unitarios con el de tests de aceptación
- [ ] Ninguna de las anteriores es correcta

(Este enfoque plantea añadir los tests de aceptación a modo de wrapper sobre el flujo de TDD) 

Siguiendo ATDD haremos que el test de aceptación pase y, entonces, haremos que pasen los tests unitarios
- [ ] Eso es cierto
- [x] Eso es falso

(Para que el test de aceptación pase en verde, será necesario que implementemos y hagamos pasar los tests unitarios correspondientes)
