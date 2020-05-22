# Exprimiendo nuestro framework de testing (PHP, Java, Javascript y Scala)

## Testing en PHP con PhpUnit

* En PHP, con la herramienta componse, te crea automaticamente un proyecto con test:

```
composer create-project codelytv/php-bootstrap your-project-name

-- Luego para ejecutar los test
composer test
```

Para realizar un test:

```php
/** @Test */
public function shouldSayHelloWhenGreeting
{
  $javi1 = new Codelyber("Javi");
  $javi2 = new Codelyber("Javi");

  $this->assertEquals($javi1, $javi2) // success
  $this->assertSame($javi1, $javi2)   // fail
}
```

* assertEquals : Mira los valores de la entidad
* assertSame : mira si es el mismo objeto (referencia)
* Con el fichero "phpunit.xml", se pueden configurar los detalles de la ejecucion y tambien definis suits (conjuntos de test para ejecutarlos de forma independiente):

```php
<phpunit
        bootstrap="./apps/bootstrap.php"
        colors="true"
        beStrictAboutTestsThatDoNotTestAnything="false"
        beStrictAboutOutputDuringTests="true"
        beStrictAboutTestSize="true"
        beStrictAboutChangesToGlobalState="true">
    <testsuites>
        <testsuite name="finderKata">
            <directory>tests</directory>
        </testsuite>
    </testsuites>
</phpunit>
```

* Con "--log-junit" se puede exportar al fichero xml de junit, que es el estandar para visualizar los resultados.

## Testing en Java con jUnit

* Utilizan un proyecto bootstrap, con la estructura de test ya montado.
* En este caso, es en el fichero "build.gradle" para incluir las dependencias de test en el perfil "test" (para que no lo incluya en el build de release).
* Luego para ejecutar los tests, con la tarea de gradle que toque.
* Ejemplo de test:

```java
	@Test
	void greet_with_a_hello_message_to_the_name_it_receives() {
		Greeter greeter = new Greeter("John");
		Greeter greeter2 = new Greeter("John");
		assertEquals(greeter,greeter2);
	}
```

* assertEquals : comprueba igualdad de valores (si estan los metodos equals/hashCode), sino mira la referencia.
* assertSame : Para comprobar la referencia (en este caso da igual si estan los metodos de antes)
* Para paralelizar los tests hay una configuracion en gradle (maxParallelForks)
* Genera (en build) unos ficheros xml con los resultados para visualizarlos.

## Testing en Scala con ScalaTest

* Los mismo que los anterioes, crean el proyecto a partir de un bootstrap con todo configurado.
* Utilizan la herramienta "sbt new" con le ruta del template. Luego se completan los datos que faltan (version, nombre proyecto, etc)
* Para ejecutar: "sbt test"
* Ejemplo:

```scala
final class TestingTest extends WordSpec with GivenWhenThen {
  "Testing" should {
    "greet" in {
      val javi1 = Testing("Javi")
      val javi2 = Testing("Javi")

      javi1 shouldBe javi2
    }
  }
}
```
* El test hereda de WordSpec para ya tener los metodos que se necesitan para testear.
* shouldBe: Mira los valores
* eq: Para comprobar las referencias
* Por defecto las "suites" se ejecutan en paralelo
* Para ejecutar los tests de una "suite" en paralelo hay que añadir un trait ("ParallelTestExecution")
* Los reportes es igual que Java, estan generados en el directorio "target".
