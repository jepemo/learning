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

* Se utiliza un "supervisord", que se encarga de leer los mensajes y llamar al consumer.
   * Define el comando para llamar al consumer (nombre cola, entorno, parametros, etc.), tambien el numero de eventos que vamos a procesar (luego el proceso termina) y supervisord lo volvera a levantar de forma indefinida.
    * Cada cuanto se levanta el proceso, etc.
    * Se define un fichero de configuracion:
       * En su ejemplo lo generan de forma dinamica: https://github.com/CodelyTV/php-ddd-example/blob/master/apps/mooc/backend/src/Command/DomainEvents/RabbitMq/GenerateSupervisorRabbitMqConsumerFilesCommand.php
       
* El consumer (en este caso, implementacion de RabbitMQ):
  * Inyecta la interfaz del consumer de infraestructura para leer los mensajes
  
```php
// ...
public function __invoke(callable $subscriber, string $name)
{
    $queueName = RabbitMQQueueNameFormatter::format($name);
    $queue     = $this->queue($queueName);
    
    $queue->consume(
        new RabbitMQConsumer($subscriber, $this->mapping, $this->logger)
    );
}
```
