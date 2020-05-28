# ¿Qué es una Query en CQRS?

## ¿Qué es una Query?

* No es una Query de BBDD
* Es un DTO
* Si devuelve una Respuesta a diferencia del Command
* Utilizan el sufijo Query
* Se utiliza para pedir información
* Se procesa en un QueryHandler
* No hay side-effects (a diferencia del Command)
* En una API/REST se corresponderia con el metodo GET (Cacheable)
* Ejemplo (casi siempre se modelo para que solo pida un ID):

```php
final class FindVideoQuery implements Query
{
    private $id;
    public function __construct(string $id)
    {
        $this->id = $id;
    }
    public function id(): string
    {
        return $this->id;
    }
}
```

* Esta Query nos llegaría a nuestro QueryHandler, el cuál crearía el Value Object de VideoId (de esta forma estaríamos validando que la Query cumpla con los requisitos de nuestro dominio).
* Luego el QueryHandler enviaría estos datos al caso de uso (VideoFinder), el cuál ya se encargaría de ir al Repositorio para recuperar el vídeo, devolverlo y transformarlo en un VideoResponse.
* El trabajar con Queries nos ayuda a separar mejor nuestro dominio, también nos permite cachear muy fácilmente (al no tener side-effects).
* Se utilizan proyecciones para que las Queries sean más simples, veloces y eficaces.

## Test

En CQRS una Query es:
- [ ] Una utilidad para lanzas consultas a base de datos
- [x] La intención de realizar una petición sin side-effects a nuestro sistema
- [ ] Una forma de no escribir SQL
- [ ] El patrón DataMapper de los ORM's

¿Quién tiene el mapeo de qué Query va a qué QueryHandler?
- [ ] El QueryHandler
- [ ] La Query dentro de sí
- [x] El QueryBus
- [ ] El QueryMapper

Si quiero modificar el nombre de un usuario lanzaré:
- [ ] Una Query
- [ ] Una Query asíncrona
- [x] Un Command
- [ ] Todas las anteriores son correctas

¿Cuántos side-effects produce una Query?
- [ ] Muchos
- [ ] Pocos
- [x] No los produce
- [ ] Depende de si es síncrona o asíncrona
