# CQRS en DDD

## Flujo petición CQRS vs Hexagonal

* Repaso capas arquitectura hexagonal
  * Infraestructura: recibe peticiones HTTP/BBDD
    * Ahora mismo instancia los VO para pasarselos a los casos de USO
    * Accede a capa aplicacion y dominio (repositorio, VO)
  * Aplicacion: Casos de uso
    * Accede a capa de dominio
  * Dominio: mi dominio 
    * Se comunica consigo mismo
* Flujo:

```
-> Controller -> Application Service -> Services
                                     -> Models
                                     -> Repos    <--- Implementation
```

* Arquitectura CQRS
  * Nuvos compoenentes:
    * Command/query: para modificar estado y realizar consutlas (Capa de aplicacion)
    * BUS: Donde se envian los comandos/queries (Capa infraestructura)
    * Handler: (ESTA EN CAPA DE SERVICIO)
      * Recibe el command/query instancia valueobjects
      * Tiene inyectados los casos de uso y
      * Llama al caso de uso
  * Al lanzar una query (querybus) nos devuelve un objeto response
    * El caso de uso para la vuelta podria tener el serializador de vuelta
  * El controller ya no llama directamente al App.Service
    * Sino con el BUS
    * Se simplifica el controller
```
    /----> COMMAND/QUERY
    |
-> CTRL -> BUS -> HANDLER -> APP. SERVICE -> SERVICES
                                          -> MODELS
                                          -> REPOS   <----- IMPL.
```

## Comunicar modules y Bounded Contexts: Application Service vs Query Bus

* En el ejemplo (inicial de arquitectura hexagonal con DDD) que enseñan
  * En el controller se inyecta el caso de uso
  * Se instancian los value objects
  * Y se llama al caso de uso
* Para el caso de CQRS
  * En el controller se crea el comando y se inicializa con los datos primitivos
    * En el comando se inicializa un campo request_ID (UUID) con el request_id de la peticion HTTP
      * Esto se usa para el flujo asincrono **[1]**
    * Es el cliente el que crea el id del recurso (id)
  * Luego este comando se lanza al commandbus
     * el dispatch del commandbus no devuelve nada (void)
     * El commandbus mapea los commands con los handlers
     * Ademas tiene registrado las excepciones de dominio que va a capturar para convertirlas a codigos HTTP
     * El commandbus es una interfaz, pueden haber varias implementaciones (sincrona/asincrona)
  * El handler recupera el command
    * Y pasa los parametros a VO y llama al caso de uso.
  * Que pasa si queremos realizar una consulta de un BC a otro? (por ejemplo en el de comentarios comrpobar si un video existe)
    * En el caso de uso de "VideoCommentPublisher" (cuando se publica comentario de un video)
    * Queremos comprobar si el video existe antes de insertar el comentario
    * Se inyecta el querybus
    * En "ensureVideoExist" lanza una query al querybus preguntando el video "FindVideoQuery"
    * Este devuelve un "VideoResponse" o lanza una excepcion
    
**[1]**
Por ejemplo, para crear un recurso de forma asincrona:

1. Cliente hace una request al endpoint de registrar un usuario.
  1. En esta petición además de los valores para registrar un usuario el cliente manda un "request_id"
2. El controller hace una validación simple de la request
  1. Si no cumple el formato devuelve un 400 Bad Request y se corta el flujo
  2. Si todo va bien seguimos
3. El controller publica el Comando de registrar el usuario al bus asíncrono y devuelve un 202 Request Accepted (que no es lo mismo que un 200 todo OK)
4. A partir de ahora depende un poco de cómo tengamos montado el cliente:
  1. Podemos tener un endpoint que sea `/command/status/{request_id}` al cuál cada X timepo le vamos preguntando por la llamada que hemos hecho antes para saber su estado
  2. Lo mismo pero en lugar de un endpoint utilizando un socket o mercure.
