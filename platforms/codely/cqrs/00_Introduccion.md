# Introducción

## Introducción a CQRS

* Patron de diseño que nos sirve para definir una arquitectura para nuestra arquitectura
* Comunicacion asyncrona (mejorar rendimiento)
* Equipos trabajar de forma desacoplada
* Flujo:
  * Usuario hace pedicion HTTP a URL (Videos) con los datos necesarios
  * La peticion le llega al controlador (VideoPostController)
  * Este crea un comando (un DTO) (CreateVideoCommand)
    * Los tipos del DTO son datos primitivos
  * Lo envia por el "CommandBus"
  * Este lo envia al Handler que toque (CreateVideoCommandHandler)
    *  Estos datos del command, si que se mapean a ValueObjects
    * Esta es la capa de servicio (caso de uso)
  * A partir de aqui es como la arquitectura Hexagonal
     * Se llama al repository, etc.
  
* Diagrama ejemplo:

```
                             +----------------------+
                             |                      |
                         +-->+  CreateVideoCommand  +------+
                         |   |                      |      |
                         |   +----------------------+      |                +---------------------------------+
                         |                                 v                |                                 |
             +-----------+---------------+       +---------+-------+        + +----------------------------+  |
             |                           |       |                 |          |                            |  |
+----------->+   VideoPostController     +------>+   CommandBus    +--------->+ CreateVideoCommandHandler  |  |
             |                           |       |                 |          |                            |  |  Como la arquitectura
             +---------------------------+       +----------+------+          +-------------+--------------+  |
                                                            |                               |                 |       HEXAGONAL
                                                            |                               |                 |
                                                            |                               v                 |
                                                            |                  +------------+-------------+   |
                                                 +----------+------------+     |                          |   |
                                                 |                       |     |   VideoCreator           |   |
                                                 |  SyncCommandBus(Impl) |     |                          |   |
                                                 |                       |     +------------+-------------+   |
                                                 +-----------------------+                  |                 |
                                                                            +               |                 |
                                                                            |               v                 |
                                                                            |                                 |
                                                                            |            etc.                 |
                                                                            |                                 |
                                                                            +---------------------------------+

```

*   `POST /videos/`
    *   Responsabilidad: Servir de protocolo de comunicación con los clientes. Petición a través del protocolo de comunicación HTTP revelando la intención de crear un nuevo recurso bajo la colección de recursos videos.
*   `VideoPostController`
    *   Responsabilidades:
        *   Recibir la petición HTTP
        *   Recuperar los datos necesarios para la creación del vídeo y encapsularlos en el Comando correspondiente
        *   Enviar el comando al bus
    *   Capa: Infraestructura
*   `CreateVideoCommand`
    *   Responsabilidades:
        *   Encapsular los datos necesarios para la creación de un vídeo
        *   Permitir su fácil transporte entre capas y serialización
    *   Capa: Aplicación
    *   Consideraciones:
        *   Para garantizar el propósito de este elemento (fácil transporte y serialización de datos), los datos que contiene deberían ser primitivos o escalares. En resumen, podremos almacenar cualquier tipo de dato que podamos meter en un JSON (string, int, bool, array, etc)
        *   Aquí vemos una aplicación del patrón de diseño Data Transfer Object (DTO)
*   `CommandBus`
    *   Responsabilidades:
        *   Transportar un determinado Command a su CommandHandler correspondiente
        *   Almacenar por tanto el mapeo 1 a 1 entre commands y command handlers
    *   Beneficios:
        *   Al ser un punto de indirección introducido entre la recepción de la petición y la ejecución de la lógica de negocio asociada, permitirá por tanto cortar el flujo de ejecución y por tanto procesar peticiones de forma asíncrona
        *   Al tratarse de un mapeo entre intención de realizar una acción, y la propia ejecución de esa acción con su lógica de negocio pertinente, permite ser reutilizado por cualquier pieza que necesite ejecutar dicha lógica de negocio. Esto es, podremos tirar comandos desde distintos puntos de nuestro sistema y tendremos un único punto de cambio en caso de necesitar modificar cómo deberían tratarse estos comandos (los handlers).
    *   Capa: Dominio (esto representaría el contrato, la interface)
*   `SyncCommandBus`
    *   Responsabilidad:
        *   Implementación concreta de la interface de dominio anteriormente descrita.
        *   En este ejemplo se trata de una implementación síncrona. Bloqueará por tanto el hilo de ejecución desde que recibe el command hasta que obtiene una respuesta que permita liberar el hilo de ejecución.
    *   Capa: Infraestructura
*   `CreateVideoCommandHandler`
    *   Responsabilidades:
        *   Recibir Command a través del bus
        *   Transformar datos del Command a tipos del dominio (value objects, nunca instanciará entidades, de eso se encargará el propio caso de uso).
        *   Invocar al caso de uso pasándole los parámetros recibidos ya mapeados a Value Objects.
    *   Capa: Aplicación
*   `VideoCreator`
    *   Responsabilidades:
        *   Encapsular la lógica de negocio asociada a un determinado caso de uso
        *   Recibir los datos necesarios para ejecutar los casos de uso
        *   Orquestar las llamadas a los distintos elementos que deberán entrar en acción para la consecución del caso de uso (repositorios, servicios de domino, modificaciones en entidades, etc)
    *   Capa: Aplicación
    *   Consideraciones:
        *   Este tipo de elementos son denominados “Application Services” en el libro “Implementing Domain-Driven Desing” (DDD). No obstante, Sandro Mancuso también los denomina “Actions” en sus charlas sobre “Interaction Driven Design”
*   `Video`
    *   Responsabilidad: Representar un determinado concepto de dominio. Se puede entender como Entidad o, en términos de DDD, como Aggregate. Más concretamente, en este caso estaríamos hablando de la Entidad que adopta el rol de Aggregate Root dentro del agregado.
    *   Capa: Dominio
*   `VideoRepository`
    *   Responsabilidad:
        *   Expresar el contrato de dominio para la interacción con la capa de persistencia.
        *   Guardar, actualizar, y eliminar recursos de tipo video
    *   Capa: Dominio
    *   Consideraciones:
        *   Implementa el patrón de diseño “Repository”.
        *   Patrón de diseño que nos interesará evitar: Data Access Objects (DAO). Motivo: Forzar a que nuestra lógica de negocio se encuentre en los casos de uso o servicios de dominio. Evitar la explosión de métodos en nuestras interfaces de interacción con la persistencia.
*   `MySqlVideoRepository`
    *   Responsabilidad:
        *   Implementación concreta de la interface antes descrita. Proveer de la lógica necesaria para interaccionar con la base de datos MySQL.
    *   Capa: Infraestructura

## Unas preguntillas...

## TODO

...
