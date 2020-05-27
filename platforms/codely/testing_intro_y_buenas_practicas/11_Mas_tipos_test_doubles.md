# Mas tipos de test doubles

## Cumpliendo firmas de metodos: Dummy

* Una clase que implementa una interface pero cuyos métodos *no hacen nada o lo mínimo posible* para simplemente cumplir con el contrato.
* Ejemplo:

```php
// El codigo que tiene los colaboradores
public function __construct(VideoCommentRepository $repository, QueryBus $bus, DomainEventPublisher $publisher)
{
    $this->repository = repository;
    $this->bus        = bus;
    $this->publisher  = publisher;
}

// Implementamos un dummy para el domaineventpublisher. Esto es sin utilizar una libreria de mock. Se haria la clase a mano.
final class DummyDomainEventPublisher implements DomainEventPublisher {
    //...
    public function record(DomainEvent ...$domainEvents):void
    {

    }
    public function publishRecorded():void
    {

    }
    //...
}
```

* Usar un mock como dummy, es que en la libreria de mock implemente la interfaz, pero no implemente nada. Es decir, no tenga comportamiento.
* Si no se utiliza una libreria de mock, se implementaria  a mano como el ejemplo de antes.

## Espiando nuestro propio comportamiento: Spy

* Son otro tipo de test doubles, similares a los mocks
* Te dicen que metodos han sido llamados por dentro.
* No implementan comportamiento
* Ejemplo:

```php
final class SpyDomainEventPublisher implements DomainEventPublisher
{
    // Nos guardamos si el metodo publish ha sido llamado
    public $hasBeenCalledPublish = false;
    // ...

    public function publish(DomainEvent ...$domainEvents):void
    {
        $this->hasBeenCalledPublish = true;
    }
}
```

Y el test:

```php
// ...
public function it_should_publish_a_video_comment():void
{
    $command = PublishVideoCommentCommandMother::random();
    //...
    $this->dispatch($command, $this->handler);

    $this->shouldSpyPublishDomainEvents();
}

public function shouldSpyPublishDomainEvents()
{
    if(!this->spyPublisher->hasBeenCalledPublish)
    {
        throw new \Exception("Publisher not called");
    }  
}
```

* El test debe asegurarse de que internamente se ha llamado al metodo publish del publisher.
* En este caso, la "expectacion" esta despues de realizar la accion.
  * Mientras que si se realiza con un mock, es este el que define el comporamiento "esperado" antes de ejecutar la accion.

## Test

A diferencia de los Mocks, los tests Dummy tienen comportamiento además de cumplir con la firma de los métodos
- [x] Mentira, son los Mocks quienes tienen comportamiento
- [ ] Mentira, ambos tienen comportamiento
- [ ] Cierto

(Lo que caracteriza a un Dummy es precisamente que no hace nada más allá de cumplir con la firma de los métodos)

El objetivo de un Spy es...
- [ ] Comprobar si el test se ha ejecutado
- [x] Comprobar si un método de un colaborador ha sido llamado
- [ ] Comprobar los argumentos que se pasan al método de un colaborador

(Este tipo de test nos sirven para saber si se ha llamado a un método, sin importar que los argumentos que le pasemos sean o no correctos)
