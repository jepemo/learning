# Implementando Queries

## Teoria

* Query: peticion para recoger datos
* Flujo:
  * Peticion GET al controlador, que esperara una respuesta (json)
  * El controlador construye la query
  * Esta se lanza al QueryBus
  * Este BUS si que devuelve datos
  * La query es recibida en el Handler
      * Recibe primitivos y converte a ValueObjects
  * El handler lo pasa al UseCase (VideoFinder)
  * El UseCase consulta el Agregado para devolver la respuesta
  * Y despues convierte al formato de la respuesta de la query (VideoResponse)  
  * Finalmente llega al controlador que convierte el "VideoResponse" a json
* Codigo:

```php

// En el controlador
...
public function __invoke(string $id)
{
    // ask llama al QueryBus
    return $this->ask(new FindVideoQuery($id));
}
...

// En el handler
public function __construct(VideoFinder $finder)
{
   // Esto es para automaticamente, cuando se llame al finder, lo que devuelva este, lo convierta al VideoResponse con este converter.
   $this->finder = pipe($finder, new VideoResponseConverter());
}

public function __invoke(FindVideoQuery $query)
{
    // Convierte del primitivo al valueobject
    $id =  new VideoId($query->id());
    return apply($this->finder, [$id]);
}

// En VideoFinder
public function __invoke(VideoId $id)
{
    $video => $this->repository->search($id);
    // Esto comprueba que $video no es nulo. Si lo es lanza excepcion diciento que "$id" es incorrecto.
    $this->guard($id, $video); 
    return $video;
}
```

## Implementando nuestra primera Query

* Pasos (casos de uso para obtener los comentarios de un video):
  * Peticion GET "/videos/x/comments"
  * VideCommentsGetController
    * La query seria: FindVideoCommentsQuery
  * La query se envia al QueryBus
  * Crear un nuevo QueryHandler: FindVideoCommentsQueryHandler
  * Nuevo caso de uso: VideoCommentsFinder
    * Llama al servicio de dominio VideoComments que devuelve un VideoComments
  * El handler lo convierte al VideoCommentsResponse
* Implementacion:

```php
//...
final class VideoCommentsGetController extends ApiController
{
    // videoId de la request
    public function __invoke(string $videoId)
    {
        // Llama al querybus
        return $this->ask(new FindVIdeoCommentsQuery($videoId));
    }
}

// Ya en el codigo de aplicacion, es donde iria la query:
// En module/videoComment/application/FindAll

final class FindVideoCommentsQuery implements Query
{
    private $videoId;
    
    public function __construct(string $videoId)
    {
        $this->videoId = $videoId;
    }
    
    public function videoId() : string
    {
        return $this->videoId;
    }
}

// En el mismo directorio de "module/videoComment/application/FindAll" iria tambien el handler

final class FindVideoCommentsQueryHandler
{
    private $finder;

    public function __construct(VideoCommentsFinder $finder)
    {
        $this->finder = pipe(new VideoCommentsReponseConverter(), $finder);
    }
    
    public function __invoke(FindVideoCommentsQuery $query)
    {
        $id = new VideoId($query->videoId());
        return apply($this->finder,  [$id]);
    }
}

// Tambien en el mismo directorio iria el caso de uso
final class VideoCommentsFinder
{
    private $repository;
    
    public function __construct(VideoCommentsRepository $repository)
    {
        $this->repository = $repository;
    }
    
    public function __invoke(VideoId $id) : VideoComments
    {
        // Usamos un search porque puede que no haya comentariso
        return $this->repository->searchAll($id);
    }
}

// El converter de la "lista" (tambien estaria en \Aplication\FindAll
final class VideoCommentsResponseConverter
{
    public function __invoke(VideoComments $comments)
    {
        return new VideoCommentsResponse(
            map(new VideoCommentReponseConverter(), $comments->values())
        );
    }
}

// Y el converter 
final class VideoCommentReponseConverter
{
    public function __invoke(VideoComment $comment)
    {
        return new VideoCommentResponse(
            $comment->id()->value(),
            $comment->body()->value(),
            $comment->videoId()->value()
        );
    }
}
```

## Test

¿Qué debe hacer QueryHandler?
- [ ] Recibir petición y ejecutar la lógica del caso de uso (VideoFinder)
- [ ] Recibir petición, modelar value objects de dominio (VideoId, VideoTitle, etc) e invocar al caso de uso
- [ ] Recibir query, modelar value objects de dominio e invocar al caso de uso
- [x] Recibir query, modelar value objects de dominio, invocar al caso de uso, y traducir su respuesta en un objeto DTO para devolverla al bus (VideoResponse)
- [ ] Recibir query, modelar entidades del dominio (Video), invocar al caso de uso, y traducir su respuesta en un objeto DTO para devolverla al bus

Si cambian los datos a retornar y tenemos que incorporar algún otro atributo del Video, ¿qué deberíamos modificar?
- [ ] El Controller
- [ ] La Query
- [ ] La implementación del QueryBus
- [ ] La implementación de QueryBus que inyectamos en el Controller
- [ ] El QueryHandler
- [ ] El caso de uso
- [ ] La entidad Video
- [ ] El VideoResponseConverter
- [ ] La respuesta VideoResponse
- [ ] Todas las anteriores son correctas
- [ ] De la 1 a la 5 son correctas
- [ ] De la 5 a la 8 son correctas
- [ ] 1, 2, 7, 8 y 9 son correctas
- [x] 7, 8 y 9 son correctas
- [ ] 2, 7, 8 y 9 son correctas
