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
  
##  Monorepo en Java

* Repositorio ejemplo: https://github.com/CodelyTV/java-ddd-example/
* Utilizan Gradle como gestor de dependencias

### Gradle

* Se puede definir un multiproyecto (subprojects)
* En settings.gradle estan definidos todos los "subproyectos" como includes
* Se define en el fichero "build.gradle":

```groovy
buildscript {
    repositories {
        mavenCentral()
        jcenter()
    }
}

allprojects {
    apply plugin: 'java'

    sourceCompatibility = 11
    targetCompatibility = 11

    repositories {
        mavenCentral()
    }

    sourceSets {
        main {
            java { srcDirs = [ 'main' ] }
        }
        test {
            java { srcDirs = [ 'test' ] }
        }
    }

    task hello {
        doLast { task ->
            println "I'm $task.project.name"
        }
    }
}

subprojects {
    group = "tv.codely.${rootProject.name}"

    dependencies {
        // Prod
        implementation 'io.projectreactor:reactor-bus:2.0.8.RELEASE'

        // Test
        testCompile "org.mockito:mockito-core:2.+"
        testCompile 'org.junit.jupiter:junit-jupiter-api:5.+'
        testRuntime 'org.junit.jupiter:junit-jupiter-engine:5.+'
    }

    // ...
}
```

* allprojects: en este bloque se recoge aquello que se aplicará a este y todos los proyectos que haya (en general todas aquellas cláusulas normales de configuración)
* subprojects: en este bloque encontramos especificaciones para los diferentes proyectos de nuestro multiproyecto
* Además del fichero principal, dentro de cada contexto tendremos un fichero build.gradle que inclurá las dependencias que necesite
* Que una aplicacion tenga como dependencia de otra no significa que tenga como dependencias a todas las dependencias de la otra
  * Puede acceder a todas las clases compiladas de la dependencia.
* A la hora de indicar directorios dentro de nuestros ficheros de configuración en gradle, debemos sustituir el caracter “\” por “:”
  * include 'src:mooc'
* La tarea "check" en gradle es ejecutar todos los tests
  * Se puede ver en el script de  ".travis.yml"

## Monorepo en Scala

* Repositorio ejemplo: https://github.com/CodelyTV/scala-ddd-example/
* Utilizan "SBT" (Scala Build Tool)

### SBT

* Fichero build.properties define que version de *sbt* se esta utilizando

```properties
sbt.version=1.2.8
```

* El fichero build.sbt:

```scala
name := "CodelyTV Scala HTTP API"
version := "1.0"

disablePlugins(AssemblyPlugin)

lazy val root = (project in file(".")).aggregate(app, shared, mooc, backoffice)

lazy val app = Project(id = "app", base = file("app/"))
               .dependsOn(mooc % "compile->compile;test->test")
               .dependsOn(backoffice % "compile->compile;test->test")
               .dependsOn(shared % "compile->compile;test->test")

lazy val shared = Project(id = "shared", base = file("src/shared"))

lazy val mooc = Project(id = "mooc", base = file("src/mooc")).dependsOn(shared % "compile->compile;test->test")
lazy val backoffice =
  Project(id = "backoffice", base = file("src/backoffice")).dependsOn(shared % "compile->compile;test->test")

addCommandAlias("t", "test")
addCommandAlias("to", "testOnly")
addCommandAlias("tq", "testQuick")
addCommandAlias("tsf", "testShowFailed")

addCommandAlias("c", "compile")
addCommandAlias("tc", "test:compile")

addCommandAlias("f", "scalafmt")             // Format production files according to ScalaFmt
addCommandAlias("fc", "scalafmtCheck")       // Check if production files are formatted according to ScalaFmt
addCommandAlias("tf", "test:scalafmt")       // Format test files according to ScalaFmt
addCommandAlias("tfc", "test:scalafmtCheck") // Check if test files are formatted according to ScalaFmt

// All the needed tasks before pushing to the repository (compile, compile test, format check in prod and test)
addCommandAlias("prep", ";c;tc;fc;tfc")

lazy val pack = taskKey[Unit]("Packages application as a fat jar")
pack := {
  (assembly in app).toTask.value
}

test in assembly := {}
```

* Los proyectos que definimos en este fichero son equiparables a los subprojectos que vimos en Gradle para el ejemplo de monorepo en Java. 
  * Podemos ver en cada uno de ellos cómo se especifica el directorio donde se encuentran sus respectivos ficheros build.sbt propios y las dependencias que puedan tener.
* Dentro de los build.sbt de cada sub-proyecto podremos definir también tareas custom que queramos que apliquen sólo a éstos
* Otro aspecto interesante es que para evitar tener varios jar que tengamos que deployear después en otro jar que los contenga lo que hacemos es utilizar un fat jar que funciona como un ‘maestro de jars’.
  * sbt-assembly es la librería que nos permite trabajar con fat jars
* En el fichero Dependencies, incluído dentro del build.sbt, se definen las dependencias comunes y de cada Bounded Context.
* Por otra parte, en el fichero Configuration encontramos el objeto con toda la configuración de scala necesaria en nuestra aplicación
* Ejemplo "/app/build.sbt":

```scala
Configuration.commonSettings

scalaSource in Compile := baseDirectory.value / "main/"
scalaSource in Test := baseDirectory.value / "test/"
resourceDirectory in Compile := baseDirectory.value / "conf"

libraryDependencies ++= Dependencies.shared

fork in run := true
connectInput in run := true

// Assembly
mainClass in assembly := Some("tv.codely.Launcher")
assemblyJarName in assembly := "codelytv.jar"
assemblyOutputPath in assembly := baseDirectory.value / ".." / "package" / (assemblyJarName in assembly).value
test in assembly := {}
```

* Otro aspecto de la configuración a tener en cuenta es la especificación de directorios, puesto que estamos saltándonos la convención de estructura de carpetas y debemos ‘explicárselo’ a sbt
* A la hora de querer interaccionar entre nuestros sub-proyectos y sbt, es muy importante tener en cuenta que deberemos hacer el ‘run’ dentro del subproyecto para que sepa que main class debe ir a buscar
  * *app/run mooc-api*
