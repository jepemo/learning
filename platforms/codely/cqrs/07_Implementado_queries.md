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

