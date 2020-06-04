# Implementación a nivel de aplicación con PHP y Scala

## Publicando eventos con Scala en RabbitMQ

* Ejemplo:

```scala
final class VideoCreator(repository: VideoRepository, publisher: MessagePublisher)
{
  def create (
      // ...
  ) : Unit = {
      //...
      publisher.publish(VideoCreated(video);
  }
}

// Publisher
// Interfaz, publish no devuelve nada
trait MessagePublisher {
    def publish[T <: Meesage](message: T): Unit
}

// Implementacion de RabbitMQ (del Message publisher)
final class RabbitMQMessagePublisher(channelFactory: RabbitMQChannelFactory) extends MessagePublisher
{
    // Crea la cola si no existe
    // ...
    
    // Implementacion publish
    override def publish[T <: Message](message: T) : Unit = {
      val routingKey = message.`type`
      //...
      createQueueIfNotExists(name = message.`type`)
      channel.basicPublish(exchange, routingKey, persistToDisk, messageBytes);
    }
}
```

## Consumiendo eventos con PHP desde RabbitMQ

* 
