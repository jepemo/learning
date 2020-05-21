# ¡Al turrón!: Nuestros primeros tests

## Tipos de test y ejemplo de test unitario

* Tipos de test:
  * **Unit testing**
  * **Test integración** (pruebas de la infraestructura a nuestro sistema)
  * Mutant testing
  * **Acceptance testing**
  * Black box testing
  * Property-based testing
  * Stress testing
  * Compatibility testing
  * Security testing
  * Load testing
* Ejemplo de test unitario a partir de una Kata (Fizzbuzz):
  * Escribe un programa que pinte una linea de con entrada de numeros de 1 al 100
  * Para multiplos de 3 pinta Fizz
  * Para multiplos de 5 pinta Buzz
  * Para multiplos de 3 y 5 pinta FizzBuzz
  * Ejemplo código (con javascript):  
```javascript
describe('Fizzbuzz should', () => {
  test('return itselfnumber', () => {
    expect(fizzBuzz(1).toBe(1))
  })
})

// Si aplicamos la filosofia de TDD de aplicar el minimo codigo para que funcione:
function fizzBuzz(number) {
  return 1;
}
```
En este caso debe devolver ya "Fizz":
```javascript
test('return Fizz if fivisible by 3', () => {
    expect(fizzBuzz(3).toBe('Fizz'))
  })
```

Modificamos el codigo:
````javascript
function fizzBuzz(number) {
  if(number % 3 === 0) {
    return 'Fizz';
  }
  return 1;
}
```

Siguiendo con la misma filosifia llegamos a:

```javascript
function fizzBuzz(number) {
  if(number % 15 === 0) {
    return 'FizzBuzz';
  }

  if(number % 3 === 0) {
    return 'Fizz';
  }

  if(number % 5 === 0) {
    return 'Buzz';
  }

  return number;
}
```

* Estos tests "prueban" una unidad, pero nunca I/O.
* SUT (Subject Under Test): Es el conjunto del "Describe" mas los tests que incluyen a ese caso.

## Test de integración - Ojo con el Unit Of Work!

* Son los tests que tambien tocan I/O
* Estos tests son los que prueba los repositorios
* Respositorio: Sistema de almacenamiento de nuestra aplicacion (BD, APIs, Cachés, etc.)
* Se haria un test para cada firma de la interfaz.
* Por ejemplo para probear la implementacion concreta de "MySQL":

```php
// Este prueba que guarda y no falla
public function it_should_save_a_student(): void 
{
  $student = new Student(
    new StudentId('195f53b6-ei62-4f22-b9f4-9d0112034277'),
    new StudentName('Javier Cane'),
    new StudentTotalVideoCreated(10)
  );
  $this->service(StudentRepositoryMySql::class)->save($student);
}

// Este prueba la recuperacion (antes guardando el dato
public function it_should_save_a_student(): void 
{
  $student = new Student(
    new StudentId('195f53b6-ei62-4f22-b9f4-9d0112034277'),
    new StudentName('Javier Cane'),
    new StudentTotalVideoCreated(10)
  );
  $this->service(StudentRepositoryMySql::class)->save($student);
  // Esto vuelca los datos en memoria a disco
  $this->clearUnitOfWork();
  
  // AssertSimilar mira que los campos sean iguales. El assertEquals miraria que la referencia sea igual, y en este caso no.
  $this->assertSimilar($student, $this->repository()->search($student->id()));
}

// aqui para probar el caso erroneo de que el usuario no existe
public function it_should_not_find_a_non_existing_student()
{
  $studentId = new StudentId('195f53b6-ei62-4f22-b9f4-9d0112034277'),

  $this->assertNull($this->repository()->search($studentId));
}
```

 * El test que ataca a I/O debe tener todo lo que necesita para su caso de prueba. Por ejemplo:
   * Si tiene que buscar un usuario, antes tiene que intertarlo
   * No vale que otro test cree los datos y otros los recuperen.
   * Un truco es borrar los datos antes de cada test o ejecutarlos en paralelo.
   
## Ejemplo test de aceptación

* Son los que cubren el aspecto mas amplio
* Simular lo mas que puedas lo que haria un usuario con tu aplicacion
* El input de la aplicación, seria el mismo que lo que haria el usuario (Llamas HTTP en api, comandos en cli, etc.)
* Utilizando la infraestructura lo mas real que se pueda.
* Intentar que el escenario sea lo mas real para que falle lo que tenga que fallar en producción
* Lenguaje Gherkin (permite generar tests a partir de un lenguaje "tipo negocio"):

```
 // ...
  Scenario: Find an existing student
  Given I send a GET request to '/students/fe7017d8-9e8f-4952-e047e36b1694'
  Then the response status code should be 200
  And the response content shuld be:
  //...
```

* En este test, aunque se realiza el flujo completo, no comprobamos si "el dato se ha guardado en BBDD" o si se "ha publicado el evento". Simplemente que la salida es la que toca. Lo otro ya lo hace los tests de integracion y los unitarios.


## Test
Los tests unitarios abarcan únicamente el scope de una única clase/método
- [ ] Eso es correcto
- [x] Eso es incorrecto
(Los tests unitarios validan el correcto funcionamiento de una unidad, que no necesariamente se corresponderá con una única clase)

Los tests de integración...
- [x] Generalmente tocan Input/Output
- [ ] Generalmente tocan la integración de varias clases de nuestra aplicación
- [ ] Generalmente mockean la infraestructura involucrada
(Este tipo de tests validan la integración con elementos externos a nuestra aplicación (BD, APIs...) por lo que no deberían mockear esta interacción)

Los tests de aceptación suelen plantearse desde el punto de vista..
- [ ] De la infraestructura (BD, Cachés, APIs..)
- [ ] Del diseñador de nuestro equipo/empresa
- [x] Del usuario
(Este tipo de tests testearán cómo sería el comportamiento de un usuario con nuestra aplicación, emulando el mismo punto de entrada y comprobando la respuesta que recibe)


