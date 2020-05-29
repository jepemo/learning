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
        $this->finder = $finder;
    }
    
    public function __invoke(FindVideoCommentsQuery $query)
    {
        $id = new VideoId($query->videoId());
        return $this->finder->__invoke($id);
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
    
    public function __invoke(VideoId $id)
    {
        $this->
    }
}
```
