# Principio de segregación de interfaces

## Teoria
* Ningún cliente debería verse forzado a depender de métodos que no usa
* Definir contratos de interfaces basándonos en los clientes que las usan y no en las implementaciones que pudiéramos tener (**Las interfaces pertenecen a los clientes**)
* Para ello es mejor siempre partir desde el caso de uso para "definir las interfaces".
* Esto es para evitar *Header Interfaces* y promover las *Role Interfaces*.
* Con esto se consigue una alta cohesión y un bajo acoplamiento estructural

## Ejemplo
Por ejemplo, si se quiesiera enviar una notificacion por slack, mail o fichero. Cual seria el mejor metodo para la interfaz?
```php
$notifier($content)
$notifier($slackChannel, $messageTitle, $messageContent, $messageStatus)
$notifier($recieverEmail, $emailSubject, $emailContent)
$notifier($destination, $subject, $content)
$notifier($filename, $tag, $description)
```
* Las opciones 2, 3, 5 quedan descartas ya que representan detalles que el cliente no quiere acoplar.
* La opcion 4 representa un intento de abstracción, pero es confuso ya que no se sabe que puede ser "destination" o "subject" según el caso.
* Entonces el mejor podria ser el primero "$notifier($content)" ya que todos lo van a tener y los demás parametros (segun el tipo) deberian estar en el contructor cuando cree el objecto de notificaciones. Pero en el caso de notificaciones variables, es decir que solo las sabemos en tiempo de ejecución, depender del constructor tendria limitaciones, ya que estariamos acoplando el tipo de notificacion al momento del envio para el cliente.
* Una opción mas modular serian varios subscribers diferentes (email, slack, etc.) que estan escuchando el evento de "elemento creado,etc." para enviar la notificacion segun el tipo.

## Keep it real


