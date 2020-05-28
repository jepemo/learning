# Implementando Commands

## Ejemplo de implementación de Command

* Lo primero seria implementar el test de aceptacion de la API/etc.
* Luego en el controlador (que tiene inyectado el queryBus/commandBus) crea el command y lo envia al commandBus.
  * dispatch -> LLama al commandBus
  * ask -> Llama al query bus
* El commandBus (interface) es implementada por (por ejemplo) "CommandBusSync" que puede utilizar un bus externo (rabbitMQ, etc)
  * Este implementa todas las relaciones entre commands y los commandHandlers.
* El handler extraer los datos del commando y los converte a ValueObjects
  * Este inyecta el caso de uso (VideoCreator)
  * Y despues llama al caso de uso con todos los valueObjects.
* En el caso de uso
  * Crea el Video (a partir de los valueObjects)
  * Luego llama al repository para guardar el video
  * Publica los posibles eventos creados en la entidad (agregado?)
  
## Implementando nuestro primer Command

* Diseño de un "VideoLike":
  * POST /videolike/
    * idvideolike
    * idvideo
    * iduser
  * Controlador que instancia el command que le pasamos con primitivos los parametros
  * Se envia al bus y este al commandhandler
  * Este crea los valueobjects a partir de los parametros
  * Le pasa estos parametros al UseCase
* Codigo:

Controlador:

```php
class VideoLikePostController extends ApiController
{
    public function __invoke(Request $request)
    {
        $command = new CreateVideoLikeCommand(
        
        );
        // cargamos parametros (idvideolike, idvideo, iduser) en el command
        
        $this->dispatch($command);
        return new ApiHttpCreatedResponse();
    }
}

// En el contexto de videos
// En directorio: VideoLike/Application/Create/
public class CreateVideoLikeCommand extends Command
{
 //...
 public function __construct(Uuid $commandId, string $videoLikeId, string $videoId, string $userId)
 {
  super($commandId);
  //...
 }
}

// En el mismo directorio se pone el handler
final class CreateVideoLikeCommandHandler
{
 public function __invoke(CreateVideoLikeCommand $command) : void
 {
   // Se mapea a los valueobjects
  $id = new VideoLikeId($command->videoLikeId());
  $videoId = new VideoLikeId($command->videoId());
  $userId = new VideoLikeId($command->userId());
  
  $this->creator->create($id, $videoId, $userId);
 }
}

// En el mismo directorio ponemos el caso de uso
final class VideoLikeCreateor
{
    public function __contruct(VideoLikeRepository $repository)
    {
        $this->repository = $repository;
    }
    
    public function create(VideoLikeId $id, VideoId $id, UserId $userId)
    {
        $videoLike = VideoLike::like($id, $videoLike, $userId);
        
        $this->repository->save($videoLike);
        
        $this->publisher->publish(...$videoLike->pullDomainEvents());
    }
}
```
