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


