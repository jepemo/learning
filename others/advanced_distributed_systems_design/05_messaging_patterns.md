# Messaging Patterns

## Dealing with out of order messaging

## Request-Response

## Publish-Suscribe

## Publish-Suscribe: Topics

Un "topic" (tema/asunto) representa una familia de conjuntos de mensajes. Por ejemplo:

* "Product"
* "Product.Created"
* "Product.Updated"
* "Product.Created.Billing"

Suscribirte a "Product" incluye a todos los demas. Suscribirte a "Producto.Created" incluye tambien a "...Billing".

A nivel de codigo, es mejor utilizar mecanismos de tipado fuerte como herencia o interfaces para "suscribirte" a conjuntos  de tipos de mensajes.


## Exercise: Dealing with out of order messages- overview

Que pasa si "Order billed" llega antes que "Order accepted" a Shipping?
```
| Sales | ----- Order accepted ------> | Billing |  ----> Order billed ----> | Shipping |
    |                                                                            ^
	\---------- Order accepted --------------------------------------------------|
```

En el orden normal, el mensaje "order accepted" crearia un registro en "Shipping" indicando que la orden se ha "creado" pero aun no esta pagada. Luego "Order billed" recuperaria este registro y actualizaria el estado a "Pagado" y se procesaria el envio.

El problema, es que si esto ocurre al revés, el mensaje "Order billed" no encontraria la orden creada en "shipping".

## Exercise: Dealing with out of order messages- solutions

* La solución podria ser: volver a enviar el mensaje ("order billed") a la cola para que lo procese después. 
  * Para reintentar el mensaje normalmente se lanza una excepcion (o hacer que falle para que lanze una excepcion) 
  * El reintento solo tendra exito si "Order accepted" llega alguna vez o si no se ha producido ningun error. 
  * Se puede poner un contador en los reintentos del mensaje para enviarlo a la "cola de errores" al "n intento". 
  * Puede ser util logear estas excepciones como:
    * INFO en el primer reintento
    * WARNING en las siguientes
    * ERROR cuando pasa el umbral y va a la cola de errores.
	
Lo importante es que es la infraestructura (sistema de mensajes) la que deberia gestionar estos errores/reintentos, no la logica de negocio.
	
## Visualization
  
## Mesagging patterns: summary



