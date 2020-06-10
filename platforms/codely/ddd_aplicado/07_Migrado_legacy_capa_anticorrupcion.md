# Migrando desde sistemas legacy gracias a la Capa Anticorrupción

## Definiendo contratos a nivel de interfaces de dominio

* Se tiene que hacer paso a paso
* Se define la capa a nivel de contrato (En este caso el repositorio)
* En este caso se utilizara la CAPA de dominio como lo nuevo y que sera la capa a ADAPTARSE.
* Sera la infraestructura la que se conectara a lo viejo y tendra que comunicarse con lo nuevo
* Porque las tablas de BBDD deberian adaptarse a los nuevos agregados y no crear agregados para las tablas existentes.
* Ejemplo:

```
-> VideoGetController -> VideoFinder -> Video
                                     -> VideoRepository  <---- LegacyVideoRepository (Lee de las tablas viejas)
```

* Una vez hecha esta parte, lo siguiente seria migrar los datos a un nuevo esquema de BBDD.

## Definiendo contratos a nivel de eventos de dominio

* Tenemos un sistema (legacy) monolitico (con su BBDD) al que atacan todas las peticiones: videos, usuarios, etc.
* El problema que no escala.
* En este caso, la solucion, seria sacar un servicio (usuarios) con su BBDD.
  * Para que a partir de ahora todas las peticiones de usuarios vayan a este servicio
* El problema es que habia logica sobre los usuarios y los videos
  * Por ejemplo en la suscripcion de usuarios y videos.
* Habria que modificar el sistema legacy, para que al crear un video:
  * **Publique un evento de dominio** (video_created)
* El servicio de usuarios estaria suscrito a este evento y actualizaria su BBDD.
* El problema son los datos que ya habia antes.
  * Habria que hacer una migracion desde la BBDD del monolito a la BBDD del servicio de usuarios.
* Por ejemplo si el sistema legacy no se pudiera tocar, porque es complejo (por ejemplo hay varios puntos de creacion, etc)
  * Se podria tener un trigger en la BBDD para que cuando se modifique la tabla Videos se lanze el evento.
* Es importante entender que estos eventos que publiquemos no son eventos de dominio como tal, realmente son mensajes que publicaremos en una cola y que consumiremos para sincronizar el nuevo sistema, respondiendo a una estructura de BD (lo que nos está indicando es que se ha insertado, modificado o borrado un registro en una tabla determinada)
  * Es decir, son como eventos de migracion de datos
  * Por lo que cuando se termine el sistema legacy, podria interesar quitar estos eventos.
  
## Implementando eventos de dominio

* Un evento de dominio es una accion que ya ha pasado (mutacion del estado de nuestra aplicacion)
* El evento es como un JSON, con un formato (id, type, ocurred_on, attributes, meta) (curso de comunicacion de microservicios)
  * correlation_id: sirve para trazar
* Ejemplo:

```java
public class SendPushToSubscribersOnVideoPublished implements DomainEventSubscriber
{
  public void comsume(VideoPublished event) {
    // Publica un evento push para cada usuarios
    // ...
  }
}
```

* Los "subscribers" son iguales que los "controlers"
  * Mapean los datos de entrada a value objects
  * Llaman al caso de uso 
* Han enseñado la implementacion del ReactorBus
  * Relaciona los eventos con los consumers
  * Puede tener varias implementaciones (sincrona/asyncrona, etc)
  * Puede estar en un sistema externo o en una cola en memoria con la aplicacion



