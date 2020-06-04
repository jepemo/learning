# Implementación a nivel de infraestructura con RabbitMQ y AWS

## Cómo definir la estructura de colas usando RabbitMQ

* Propuesta:
  * 1 exchange por servicio (publisher)
    * No deberemos añadir nueva infraestructura el crear nuevos eventos
    * Utilizar exchange "Topic": Permitir filtrar por tipo de evento, incluyendo wilcards.
  * 1 cola por caso de uso, consumer y evento
    * Permite optimizacion de coste al consumir solo el tipo de evento que nos interese (sino tendriamos que filtrar en la aplicacion los eventos que no queremos procesar)
    * Ejecutar todos los casos de uso de todos los comsumers (no "robar" eventos)
    * Posibilidad de re-encolar eventos por haber fallado 1 caso de uso concreto.
  * OCP: Este enfoque evita modificar publisher por el hecho de añadir un consumer
* Optimizacion
  * 1 cola por consumer y N eventos
    * Siempre y cuando la accion sea unica (actualizar el estado de un usuario)
    
### Nomenclatura routing keys

* Nombres de los eventos al publicarse
* Routing key debe ser igual al "type" del mensaje
* Ejemplo: 
  * Empresa
  * Servicio o nombre bounding context
  * Version Evento: se cambia si la nueva no es retrocompatible con la anterior.
  * Tipo de mensaje: por si es un command, evento, etc.
  * Entidad: El servicio de video podira publicar entidades como: Video, VideoComment, etc.
  * Accion: en pasado

```
codelytv.video.1.event.video.published

empresa.servicio_o_boundingcontext.version_evento.tipo_de_mensaje.entidad.accion
```
* Recurso (de formato): https://github.com/asyncapi/topic-definition

### Nomenclatura colas

* Ejemplo: user.notification.nofity_user_on_video_published
* Formato:
  * servicio
  * entidad
  * accion_on_evento
  
## Implementación con AWS SNS y SQS

* Exchange = SNS (Simple notification service)
* Colas = SQS (Simple queues)
* Seguir las mismas indicaciones que en RMQ de un exchange por servicio y 1 cola por consumer/casouso/evento
* Pero, en las colas hay que filtrar los eventos que se quieren para esa cola.
  * En el payload del mensaje se crea un campo nuevo que es "event_type"
  
```json
...
  "MessageAttributes" : {
    "event_type" : {"Type": "String", "Value": "domain_event"}
  }
}
```

  * Este ultimo campo se añade con la libreria:
  
```php
$this->cliente->publish(
    [
     'TopicArn' => $topicArn,
     'Message' => apply($this->serializer, [$event]),
     'MessageAttributes' => [
       "event_type" => [
         "DataType" => "String",
         "StringValue" => $event::eventName(),
       ],
     ],
    ]
);
```

 * En rabbitMQ al publicar hay un campo que le especificas la "routingKey". En AWS SNS, hay que poner este campo dentro del mensaje.
 
* Para la cola, para que filtre los eventos que le interesen hay que definir el filtro (en la consola de amazon):

```json

{
  "event_type": [
    "some_domain_event_name",
    "another_domain_event_name"
  ]
}
```

###  Por qué no Kafka/Kinesis?

* No permite (facilmente) hacer un enrutado 1 a N.
  * Solo publican a un sitio y los consumers tienen un puntero y recorren los distintos mensajes.
* Se complica la gestion de erroes (no hay forma facil de hacer dead letters, hay que gestionarlo todo a mano)
* Son buenos para analisis de datos/bussines intelligense, no para colas



           


