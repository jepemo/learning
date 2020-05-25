# Mejorando la mantenibilidad y estructura de nuestros test

## Estructura de carpetas

* Debe seguir los mismos principios que la estrucutra de codigo.
* Por ejemplo si tenemos el codigo. main -> mooc -> video -> application -> search -> VideoSearcher.scala
  * Estara en: test -> mooc -> video -> application -> search -> VideoSearcherShould.scala
  * Seria el test unitario, que comprueba el comportamiento de la clase "VideoSearcher".
  * La prueba del caso de uso (capa de aplicacion) de  "videosearcher".
* Luego en la carpeta de tests, en el nivel de "video" tambien estaria la carpeta "domain" y ahi es donde estarian los "ObjectMothers".
* Para la de infraestructura (integracion) lo mismo.
  * Respecto a la propia infraestructura de los tests, hay dos aproximaciones que podríamos seguir: tenerla en la propia raíz de la carpeta de infraestructura, o bien tener dentro de la misma una carpeta de ‘resources’ donde recoger todas esas clases
* Por otro lado, a nivel de tests de aceptación podríamos considerar dos enfoques:
  * Mimificar la carpeta ‘/app/main’, donde teníamos los puntos de entrada a la aplicación, para mantener autocontenido todo lo relativo a dicha aplicación
  * Llevarlos a la propia carpeta test, teniendo ‘/test/application’ y ‘/test/src’, de modo que todos los tests están en la misma carpeta
  * Sigamos un enfoque u otro, es realmente importante mantener la misma estructura una vez se llega al consenso de cual utilizar para que podamos mantener una mayor cohesión y el código sea mucho más comprensible
  
## Aplicando el Principio de Responsabilidad Única de SOLID

* Siguiendo el principio SRP (Single renposability principle) la idea es que si se modifica un requisito de la aplicacion (caso de uso) solo deberia fallar el test que la prueba.
* En este caso se podria entender como "unidad" tambien juntar a los colaboradores que estan implicados en el caso de uso.
* Y solamente se prueba una cosa (1 assert) con lo que podria ser un "code smell" tener varios assert en un test.

## Patrón Given-When-Then o Arrange-Act-Assert

* A la hora de definir la estructura a seguir dentro de los test cases, uno de los patrones más ampliamente utilizados es el Given-When-Then, también conocido como Arrange-Act-Assert
* Es decir: Dado que hay un determinado escenario de entrada, cuando tengan lugar una o varias acciones determinadas, entonces comprobamos que el resultado generado es el esperado
* Para el ejemplo:

```php
public function it_should_find_an_existing_video(): void
{
    // GIVEN (dado este video)
    $video = VideoMother::random();

    $this->repository()
    ->shouldReceive('search')
    ->with(equalTo($video->id()))
    ->once
    ->andReturn($video);

    // WHEN (al llamar al finder para ese video id)
    $actualResponse = $this->finder->__invoke($video->id());

    $expectedResponse = VideoResponseMother::create(
      $video->id(),
      $video->type(),
      $video->title(),
      $video->url(),
      $video->courseId()
    );

    // THEN (el resultado tiene que ser el mismo)
    $this->assertSame($expectedResponse, $actualResponse);
}
```
* **Given**: En este caso podríamos entender que el escenario dado podría ser tanto que tenemos un Video, como también incluir aquí el hecho de tenerlo persistido en nuestro repositorio
* **When**: La acción realizada aquí sería la de invocar al caso de uso
* **Then**: Finalmente lo esperado en este ejemplo es que la respuesta generada por la acción sea igual que la definida para la aserción (expectedResponse)

## Test

Para seguir una mimificación en la estructura de carpetas de producción y tests, la carpeta de Domain contendrá los tests de nuestras entidades de dominio
- [ ] Eso es Correcto
- [x] Eso es Incorrecto

(Ya que es aconsejable evitar los tests de relación 1-1 sobre nuestras clases, más que tests de agregados/entidades lo que tendremos aquí serán nuestros ObjectMothers)

Una forma de aplicar el SRP de SOLID en nuestros tests es...
- [ ] Tener un único test case por cada suite
- [x] Validar una única aserción por cada test case
- [ ] Ninguna de las anteriores es correcta

(Siguiendo este principio, un test unitario sólo debería validar que una única respuesta (o ausencia de errores) independientemente del número de colaboradores que se orquesten internamente)

El patrón Given-When-Then nos permite...
- [x] Aportar mayor legibilidad a los tests
- [ ] Automatizar la creación de tests

(Este patrón nos ayuda a tener tests más semánticos y comprensibles, además de poder encapsular su lógica mucho más fácilmente)
