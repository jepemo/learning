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

* 
