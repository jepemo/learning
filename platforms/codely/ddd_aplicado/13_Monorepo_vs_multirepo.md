# Monorepo vs. Multirepo

## Monorepo 🐒 vs. Multirepo 🐑

* La estructura del codigo/carpetas a la hora de estructurar los bounded contexts.
* Monorepo
  * Todos los BC/Aplicaciones estan en el mismo repositorio
  * Resulta más cómodo a la hora de compartir código y tendremos el código más ‘recogido’
* Multirepo
  * Cada BC(+sus aplicaciones) estan en un repositorio
  * Resulta más sencillo utilizar diferentes lenguajes en cada contexto y que cada uno evolucione mas libremente
* A la hora de tomar la decisión sobre qué diseño seguir, un criterio crítico es ver cual nos ofrece de forma más sencilla los beneficios que estemos buscando, por lo que hay que tener claro los beneficios que estamos buscando:
  * Nuestro código está lo suficientemente desacoplado, en nuestro codigo, como para poder tener ecosistemas diferentes si hace falta
  * Está lo suficientemente cohesionado para que los cambios no impliquen que un cambio o rollback de una parte de nuestro código implique un proceso paralelo en otros puntos de éste
* Con frecuencia se asocia el uso de monorepos a connotaciones negativas derivadas de razones históricas o a malas experiencias en anteriores proyectos que pudieran tener restricciones para su adecuada implementación. 
  * Sin embargo, respetando las ‘reglas del juego’ (convenciones) de un buen uso de este tipo de diseño, no tendremos esa serie de restricciones sobre los monorepos
  
  ## Monorepo en PHP
  
* Repo ejemplo: https://github.com/CodelyTV/php-ddd-example/
* Utilizan "Composer" como gestor de dependencias
* Un fichero "composer.json" general:
  * Definen las dependencias de todos los contextos
  * Esta en el primer nivel
  * Pero permite gestionar todas las dependencias desde un mismo sitio
  * El problema es que las dependencias se cargarán en cada contexto, las necesite o no
  * Pero evitamos que el IDE se vuelva loco buscando la implementación correcta
* Un fichero composer.json por contexto
  * La actualización de piezas de nuestra aplicación es independiente entre contextos
  * En cada contexto se cargarán solo las dependencias que utiliza
* Directorios:

```
src
|--Shared
    |--Infrastructure
        |--Bundle
            |--DependencyInjection
            |   |--Compiler
            |   |--Resources
            |   |   |--infrastructure_config.yml
            |   |   |--...
            |   |   |--infrastructure_services.yml
            |   |--CodelyTvInfrastructureExtension.php
            |--CodelyTvInfraestructureBundle.php
```

* El framework es parte de la infraestructura
  * Por ello esta dentro del directorio
* Por ejemplo:

```php
final class CodelyTvInfrastructureExtension extends Extension
{
    public function load(array $config, ContainerBuilder $container): void
    {
        $loader = new YamlFileLoader($container, new FileLocator(__DIR__ . '/Resources'));
        $loader->load('infrastructure_extension.yml');
        $loader->load(sprintf('infrastructure_config_%s.yml', $container->getParameter('kernel.environment')));
    }
}
```

* El fichero de extensión del Bundle nos permitirá cargar aquellos recursos .yml que necesitamos.
* Una de las características de Symfony es que cuando tenemos un Bundle, buscará en ese nivel de directorio la carpeta DependencyInjection/ y dentro de esta un fichero con igual nombre pero acabado en ‘Extension’ para cargarlo auto-mágicamente
* Definicion bunble:

```yaml
services:
  _defaults:
    autoconfigure: true
    autowire: true

  CodelyTv\Shared\:
    resource: '../../../../../*'
    exclude:
      - '../../../../../utils.php'
      - '../../../../../Infrastructure/Api/*'

  CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventMapping:
    arguments: [!tagged codely.mooc.subscriber]

  CodelyTv\Shared\Infrastructure\RabbitMQ\RabbitMQConnection:
    arguments:
      - '%rabbitmq_connection_parameters%'

  codely.infrastructure.async_command_bus:
    class: CodelyTv\Shared\Infrastructure\Bus\Command\CommandBusAsync
    arguments:
      $pendingRequestsFilePath: '%async_command_bus_pending_requests_file_path%'
    lazy: true
```

* Dentro de estos ficheros de configuración que estamos cargando, infrastructures_services.yml es el que nos va a permitir hacer el autowiring de todas las clases que le especifiquemos.
* En este caso aquellas con el prefijo CodelyTv\Shared y que se encuentren dentro del directorio indicado.
* Esta configuración afecta a los servicios declarados en este fichero, pero si tenemos otro Bundle en otro Bounded Context tendremos que repetir la configuración definida en _services: defaults si queremos que también haya autowiring
* Aunque con este procedimiento de base cargará como servicios clases que no lo son, Symfony en la fase de “compilación” comprueba qué clases no se están inyectando para eliminarlas
  
  
