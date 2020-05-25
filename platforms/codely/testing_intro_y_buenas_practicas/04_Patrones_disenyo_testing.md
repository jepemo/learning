# Patrones de diseño aplicados a testing

## Evitando instanciaciones complejas: ObjectMother

### Tradicional

* El ejemplo base, partiendo de una clase "User" con este metodo, para probarlo seria:

```php
//...
public function canEditVideos(): bool
{
    return $this->accessLevel() >= self::MIN_LEVEL_TO_EDIT_VIDEOS;
}
//...
function test_user_is_able_to_edit_video_with_enough_access_level(): void
{
    // El 3 es el "accesslevel" que se pasa por parametro
    $user = new User('some-id', 'some-name', 3);

    assertThat(true, $user->canEditVideos());
}
```

* El problema, es que cada vez que se hace un test, hay que instanciar el "user". Asi que si anyadieramos un nuevo parametro, habria que modificar todos los tests.

### Builder pattern

* Una idea, seria utilizar el "Builder Pattern":
* Es una clase, con los mismos atributos que User, que se encaga de crear el objeto.
* En el constructor habrá definidos unos valores por defecto para todos los atributos, los cuales podremos modificar con unos ‘setters’ semánticos (Ej. withName, withAccessLevel…) antes de hacer el build del objeto
* POr lo que el ejemplo cambiaria:

```php
//...
public function withAccessLevel(int $accessLevel)
{
    $this->accessLevel = $accessLevel;

    return $this;
}
public function build()
{
    return new User($this->id, $this->name, $this->accessLevel);
}
//...
function test_user_is_able_to_edit_video_with_enough_access_level(): void
{
    $user = (new UserBuilder())->withAccessLevel(3)->build();

    assertThat(true, $user->canEditVideos());
}
```
* En este caso, al crear el usuario, se muestran las propiedades relevantes de este test (accessLevel) y no las otras
* Pero es muy boiler-plate. Mucho codigo que escribir y mantener.

### Object mother

* En este ejemplo el objeto mother
* En el ejemplo se utilizan "ValueObjects" en vez de datos primitivos.

```php

//...
public static function withAccessLevel(int $accessLevel)
{
    public static function create(UserId $id, UserName $name, AccessLevel $accessLevel)
    {
        return new User($id, $name, $accessLevel);
    }
    return self::create(UserIdMother::random(), UserNameMother::random(), 
    AccessLevelMother::create($accessLevel));
}

// ...

// El test
function test_user_is_able_to_edit_video_with_enough_access_level() : void
{
    $user = UserMother::withAccessLevel(3);
    assertThat(true, $user->canEditVideos());
}

```

* Nos permite trabajar con una clase "factoría" que contiene una serie de métodos estáticos que nos permiten instanciar la clase con mayor semántica (Ej. UserMother::withName('Rafa')). 
* A diferencia de lo que veíamos en la alternativa anterior, los demás atributos se generan de forma aleatoria y no de forma fija en el constructor, con lo que además estamos ganando en aleatoriedad de las casuísticas que tendrán que pasar los tests

### Named arguments

* El patron anterior, tiene el problema que habria que crear un metodo  para cada combinacion de valores que quisieramos modificar.
  * withAccessLevelAndName(3, "nombre"), etc.
* Se puede utilizar el patron "named arguments", si el lenguaje lo permite, que permite solo inicializar los argumentos que se quieran:
* Ejemplo:

```scala
object UserMother {
  def apply(
    id: String = UserIdMother.random.value.toString,
    name: String = UserNameMother.random.value,
    accessLevel: Int = UserAccessLevelMother.random.value
  ): User = User(id, name, accessLevel)

  def random: User = apply()
}

// Test

"test user is able to edit video with enough access level" in {
  val user = UserMother(accessLevel = 3)

  user.canEditVideos shouldBe true
}
```

## Cómo evitar tests lentos y acoplados: Fakes, Stubs y Mocks

* Test doubles (dobles (de actor doble) de test): fake, stubs, mocks
* Las librerias suelen utilizar el termino "mock" siempre. Aunque es el concepto mas general. Pero es interesante tambien utilizar los otros terminos.
* SUT (Subject under test) es lo que queremos abarcar en el test.
### FAKE
  * Implementacion falsa de algo de verdad
  * Repositorio: RepositorioFake, copia en memoria
  * Ejemplo:
  
 ```java
 final class HardcodedInMemoryUsersRepository {
    private Map<Integer, User> users;

    public HardcodedInMemoryUsersRepository(Map<Integer, User> users) {
        this.users = users;
    }

    public Optional<User> search(Integer id) {
        return Optional.ofNullable(users.get(id));
    }
}
 ```
 * Es diferente a un "dummy" porque el "search" si que implementa cierta logica. Por ejemplo search busca en un mapa de elementos.
 * Se utilizan para consultar los datos con lo que se ha interaccionado. Los datos que se han insertado en memoria en este caso
 * El problema, es que tiene logica y eso se tiene que mantener. A veces es mejor utilizar un mock.
 
 ### Stubs
 
 * Parecido al Fake, pero tiene valores predefinidos. No se pasan por el test.
 * Ejemplo:
 
 ```java
 private Map<Integer, User> users = Collections.unmodifiableMap(new HashMap<Integer, User>() {
    {
        put(UserMother.RAFA_ID, UserMother.rafa());
        put(UserMother.JAVI_ID, UserMother.javi());
    }
});
 ```
 
 * Podria tener varias implementaciones del stub para distintos casos de datos distintos: repositorio sin datos, con un dataset concreto, etc.
 
 ### Mocks
 * 
 * Ejemplo:
 
 ```php
 //...
$video = VideoMother::random();

// Aqui se define el mock
$this->repository()
    ->shouldReceive('save')
    ->with(similarTo($video))
    ->once()
    ->andReturnNull();
 ```
 * La diferencia con el stub, es que aparte de definir lo que devolvera, tambien se define su comportamiento.
 * Por ejemplo, el anterior dice que debera llamar al metodo save, con un paraemtro parecido a "video", una vez y devolver null.

## Test

Un handicap de los 'Fakes' es el coste de mantenimiento
- [x] Eso es correcto
- [ ] Eso es falso

(Al tratarse de otra implementación funcional más, tendremos que invertir más tiempo en desarrollarla y mantenerla)

El uso del Patrón Builder en nuestras pruebas nos permite extraer fuera del propio test la responsabilidad de..
- [ ] Testear la implementación de la infraestructura
- [x] Instanciar las entidades
- [ ] Mockear las implementaciones de la infraestructura

(Este patrón supone tener un elemento 'builder' encargado de construir e instanciar nuestra clase)
