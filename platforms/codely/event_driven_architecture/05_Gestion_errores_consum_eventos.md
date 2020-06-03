# Gestión de errores consumiendo eventos

## Eventos desordenados

* Orden no garantizado
* Ejemplo (real de sistema legacy para instroducir colas):

```
[Servicio1 (scala)]       [Exchange]    [Queue]      [Consumer(php)]        [Api(synphpony)]
     |                       |             |               |                       |
     |  Convers. created     |             |               |                       |
     | --------------------> | Conv. creat.|               |                       |
     |                       |------------>|               |                       |
     | message sent          |             |               |                       |
     | --------------------> | Msg. sent.  |               |                       |
     |                       | ----------->|   Consume     |                       |
     |                       |             |<--------------|                       |
     |                       |             |   Msg. sent.  |                       |
     |                       |             | ------------->|                       |
     |                       |             |  Conv. creat. |                       |
     |                       |             | ------------->|     Send msg? (peta)  |
     |                       |             |               | --------------------> |
```

* Una solucion podria ser, que si la API devuelve un error, que el consumer volviera a encolar el mensaje para intentarlo mas tarde.
   * Entonces el siguiente mensaje seria el de "Conversacion creada" y devolveria OK
   * Despues volveria a llegar el msnaje de "Msg sent" y al llamar esta vez a la API si que no daria error.
   * Se tendria que definir un numero maximo de reintentos para evitar bucles infinitos
   * Si se llega a este punto, el mensaje se pondria en una cola especial llamada dead letter, para no perderlo.
   * La aplicación es responsable de toda esta logica.
* Otra solución, si falla el "send msg", podria ser que el consumer al leer el mensaje de la cola, no devolverle el ACK para que no lo borre si falla al llamar la API.
  * Entonces, cuando a la cola le salte el timeout, lo volveria a intentar.
  * En ese tiempo, se consumiria el de la conversacion creada y luego se procesaria el otro.
  * Se tendria que definir un numero maximo de reintentos para evitar bucles infinitos, también (pero como parametro interno de la cola, no en nuestra aplicacion)
  * Encolar en el dead letter para no perderlo, tambien lo haria la infraestructura.
  * Por lo tanto, la infraestructura es responsable de esta logica.
  
## Eventos duplicados

* 
