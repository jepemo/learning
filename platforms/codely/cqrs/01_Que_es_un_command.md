# ¿Qué es un Command en CQRS?

## ¿Qué es un Command?

* Existe también el patrón "Command" en GoF.
  * No es lo mismo
  * El de GoF es un contrato (con varias implementaciones), autoencapsulado (que implementa el comportamiento), que se ejecuta
* El "Command" de CQRS es un DTO
  * Sirve para transferir los datos de un sitio a otro (Capas diferentes de la aplicacion)
  * Solo tiene datos, porque tiene que serializarse para pasarse con el BUS.
  * Es Immutable.
* Todas las acciones que modifiquen algo en nuestro sistema, seria Commands.
* Sincronos/Asincronos:
  * Acciones que tarden poco, podrian ser sincronas
  * Acciones que tarden mas deberian ser asincronas.
    * Como el cliente sabe que ha terminado?
    * Es trabajo del cliente enterarse que ha terminado o desde el servidor con un websocket.
* Ejemplo (Para cambiar el nombre del usuario):

```php
final class RenameUserCommand extends Command
{
    private $userId;
    private $newName;
    public function __construct(string $userId, string $newName)
    {
        $this->userId  = $userId;
        $this->newName = $newName;
    }
    public function userId(): string
    {
        return $this->userId;
    }
    public function newName(): string
    {
        return $this->newName;
    }
}
```

* Este Command nos llegaría a nuestro CommandHandler, el cuál crearía dos Value Objects: UserId y UserName (de esta forma estaríamos validando que los valores del Command cumplen con los requisitos de nuestro dominio).
* Luego el CommandHandler enviaría estos datos al caso de uso, el cuál ya se encargaría de ir al Repositorio para recuperar el usuario, cambiarle el nombre, volverlo a persistir y luego lanzar el evento de nombre modificado.

## Test

En CQRS un Command es:
- [ ] Un DTO
- [ ] Algo que representa la intención de realizar una acción
- [ ] La C de CQRS
- [x] Todas las anteriores son correctas

El Command se lanza al:
- [ ] Command Handler
- [ ] Command Manager
- [x] Command Bus
- [ ] Caso de uso

En programación, un DTO significa:
- [x] Data Transfer Object
- [ ] Discount
- [ ] Do The Object
- [ ] Data Transformation Object

Un CommandHandler asíncrono nos permite:
- [ ] No tener que gestionar los identificadores de recursos desde fuera
- [x] Realizar la operación de fondo mientras se realizan otras
- [ ] Hacer que el Command devuelva una respuesta

Normalmente, el Command se lanza desde:
- [ ] El CommandHandler
- [x] Los puntos de entrada de nuestra aplicación
- [ ] El caso de uso
- [ ] Desde el mismo Command
