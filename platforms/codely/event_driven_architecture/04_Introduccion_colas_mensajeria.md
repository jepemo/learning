# Introducción a las colas de mensajería

Veremos los distintos elementos que componen un sistema de mensajería: Publisher, Exchange, Queue, y Consumer. Entraremos en detalle de los tipos de Exchange, y aprenderás a definir tu propia arquitectura de colas.

## Introducción a las colas de mensajería

* **Broker** de mensajes: Sistema de mensajeria
* **Producer**: publica eventos/mensajes que van a la cola de mensajes
* **Exchange**: Evento va a parar a un exchange (no va directamente a la cola) que lo enruta a las n colas que pertoque
  * Esto es algo de infraestructura
* **Consumer/worker**: Le pide a la cola los mensajes y esta se lo devuelve (y desaparece de la cola)

### Tipos de exchange

* Fanout: Duplica el evento recibido por cada cola suscrita al exchange
* Direct: Permite definir un binding key a la hora de suscribir una cola al exchange. Envia el evento a la cola si hay binding key de la cola == routing key del evento. El exchange lleva el mensaje a las n colas que cumplan el "bindingkey".
* Topic: Igual que Direct, pero permitiendo wildcards en binding keys.


### Protocolos

* AMQP: Advanced Message Queuing Protocol (Es el que usa el message broker RabbitMQ)
* MQTT: Message Queuing Telemetry Transport
* STOMP: Simple (or Streaming) Text Oriented Message Protocol
* ...

### Ventajas

* Consumer saturado: Se publican mas de los que se pueden procesar. 
  * Las colas pueden almacenar los eventos para que se puedan procesar cuando se puedan.
  * tryrabbitmq.com (Simula tu arquitectura)

