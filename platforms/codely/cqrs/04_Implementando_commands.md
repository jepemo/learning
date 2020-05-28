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

* 
