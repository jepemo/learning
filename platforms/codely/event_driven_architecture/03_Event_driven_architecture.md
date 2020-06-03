# Solución: Event-Driven Architecture

Repasaremos conceptos de SOLID aplicado al diseño a micro-nivel, y nos los llevaremos a nivel de arquitectura de servicios gracias a los Eventos de Dominio. También veremos cómo definir la estructura de éstos a nivel de implementación.

## Repaso: SOLID a nivel micro-diseño

* Hay un paralelismo entre la aplicacion de SOLID a nivel micro y macro.
* Viendo posibles etapas en la implementacion.
* Etapa 1 (estado inicial)

```scala
final class VideoCreator(repository: MySqlVideoRepository) {
    def create(id: VideoId, title: VideoTitle): Unit = {
        val video = Video(id, title);
        repository.save(video);
    }
}
```
    
    * El problema es que VideoCreator sabe demasiado (la implementacion de MySql). Si se quisiera cambiar la implementacion tendriamos problemas.
    * (+) Codigo facil de trazar
    * (-) Problemas de tolerancia al cambio
    * (-) Dificil de testear
    
* Etapa 2: Aplicamos DIP

```scala
// Se inyecta una interfaz
final class VideoCreator(repository: VideoRepository) {
    def create(id: VideoId, title: VideoTitle): Unit = {
        val video = Video(id, title);
        repository.save(video);
    }
}

trait VideoRepository {
    def save(video: Video) : Future[Unit]
}
```

  * Hemos desacoplado VideoCreator de la implementacion (añadiendo un nivel de indirección)
  * (+) Es mas facil añadir nueva implementacion
  * (+) Cumple el Open/Closed principle (Se puede añadir nueva implementacion, sin tocar la clase VideoCreator)
    
* Etapa 3: Arquitectura Hexagonal
  * Tres capas (Aplicacion, Infraestructura, dominio)
  * VideoCreator (Aplicacion), VideoRespository (Dominio), MySqlVideoRepository (Infraestructura)
  * CQRS (desacoplamiento):
    * VideoPostController -> CreateVideoComment -> CommandBus -> CreateVideoCommandHandler -> (valueobjects) -> VideoCreator -> VideoRepository <- MySqlVideoRepository
    
## Solución - Eventos de dominio (SOLID a nivel macro-diseño)

* El caso de uso que teniamos:
   * VideoService -> UsersService
* Queremos ir a:
  * VideoService -> ???? <- UsersService
  * ???? sera un evento de dominio (video_created)
* Por lo que el flujo seria:
  * Se crea un video
  * Se publica un evento de "video_creado"
  * El servicio de usuarios, esta suscrito a ese evento
  * Este servicio tiene un "read_model" que es actualizado por el evento (por lo tanto el dato esta duplicado)
    * Pero los datos duplicados estan optimizados para el caso de uso. En este caso un contados de videos.
* Si el servicio de videos falla o esta saturado, el de usuarios seguira funcionando y tendra datos correctos que devolver.
* changelog
  * (+) Reducimos lantecias  a 0 (no caching) y evitamos efecto domino sin CB (circuit breaker)
  * (+) Escalabilidad implementación (consumidores NO condicionan definicion OCP)
  * (+) Reactive Manifesto certified
  * (-) Consistencia eventual (Tarde o temprano el dato estara bien): los datos ya no estan en un unico punto de verdad, por lo que pueden ser diferentes :/ )
  * (-) Mantener distintas representaciones de la misma informacion (proyecciones): Más código que implementar
  * (-) Gestionar eventos duplicados
  * (-) Gestionar eventos desordenados
  * (-) Implicaciones a nivel de testing
    * Habra que suponer que cada servicio funciona bien a nivel individual y testar servicio por servicio.
    * Se asume la perdida de control de poder probar todo el ciclo completo
    * Se testea a nivel, si lleva un evento X a mi sistema entonces....
