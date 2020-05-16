# Principio de inversión de dependencias

## Teoria

* Los modulos (clases/componentes/loquesea) no deberian depender de los de bajo nivel.
* La dependencia deberia estar entre "abstracciones"
* Por ejemplo la clase "Enviar notificacion" deberia depender de la interfaz de notificaciones, no del enviador de notificaciones de "slack".
* Los parametros (dependencias) de pasan por constructor
* Se depende de las interfaces (contratos)
* Utilizar como base el principio de Liskov

## Ejemplo

- Este primer ejemplo no utiliza DI ya que "UserSearcher" utiliza la implementacion concreta "HardcodedInMemoryUsersRepository".
- Además, se esta instanciando en el que la usa.

```java
final class UserSearcher {
    private HardcodedInMemoryUsersRepository usersRepository = new HardcodedInMemoryUsersRepository();

    public Optional<User> search(Integer id) {
        return usersRepository.search(id);
    }
  }
  
final class HardcodedInMemoryUsersRepository {
    private Map<Integer, User> users = Collections.unmodifiableMap(new HashMap<Integer, User>() {
        {
            put(1, new User(1, "Rafa"));
            put(2, new User(2, "Javi"));
        }
    });

    public Optional<User> search(Integer id) {
        return Optional.ofNullable(users.get(id));
    }
}

final class UserSearcherShould {
    @Test
    void find_existing_users() {
        UserSearcher userSearcher = new UserSearcher();

        Integer existingUserId = 1;
        Optional<User> expectedUser = Optional.of(new User(1, "Rafa"));

        assertEquals(expectedUser, userSearcher.search(existingUserId));
    }

    @Test
    void not_find_non_existing_users() {
        UserSearcher userSearcher = new UserSearcher();

        // We would be coupled to the actual HardcodedInMemoryUsersRepository implementation.
        // We don't have the option to set test users as we would have to do if we had a real database repository.
        Integer nonExistingUserId = 5;
        Optional<User> expectedEmptyResult = Optional.empty();

        assertEquals(expectedEmptyResult, userSearcher.search(nonExistingUserId));
    }
}

```

Desde el propio Test ya se observa este acoplamiento, obligando a saber, en este caso, que el usuario tiene que existir en el HashMap (caso de find_existing_users) o que no va a existir un usuario con un id concreto (caso de not_find_non_existing_users).

Mientras que este otro ejemplo, se esta inyectando la dependencia por el constructor.

```
final class UserSearcher {
    private HardcodedInMemoryUsersRepository usersRepository;

    public UserSearcher(HardcodedInMemoryUsersRepository usersRepository) {
        this.usersRepository = usersRepository;
    }

    public Optional<User> search(Integer id) {
        return usersRepository.search(id);
    }
}
```

En el test hay que instanciar el objecto:

```java
final class UserSearcherShould {
    @Test
    void find_existing_users() {
        // Now we're injecting the HardcodedInMemoryUsersRepository instance through the UserSearcher constructor.
        // 👍 Win: We've moved away from the UserSearcher the instantiation logic of the HardcodedInMemoryUsersRepository class allowing us to centralize it.
        // 👍 Win: We're exposing the couplings of the UserSearcher class.
        HardcodedInMemoryUsersRepository usersRepository = new HardcodedInMemoryUsersRepository();
        UserSearcher userSearcher = new UserSearcher(usersRepository);

        Integer existingUserId = 1;
        Optional<User> expectedUser = Optional.of(new User(1, "Rafa"));

        assertEquals(expectedUser, userSearcher.search(existingUserId));
    }

    @Test
    void not_find_non_existing_users() {
        HardcodedInMemoryUsersRepository usersRepository = new HardcodedInMemoryUsersRepository();
        UserSearcher userSearcher = new UserSearcher(usersRepository);

        Integer nonExistingUserId = 5;
        Optional<User> expectedEmptyResult = Optional.empty();

        assertEquals(expectedEmptyResult, userSearcher.search(nonExistingUserId));
    }
}
```

Con esto estamos viendo el acoplamiento de nuestras clases.

Aunque estos ejemplo son de inyeccion de dependencias. Para realizar la inversion hay que utilizar interfaces.

```java
final class UserSearcher {
    private UsersRepository usersRepository;

    public UserSearcher(UsersRepository usersRepository) {
        this.usersRepository = usersRepository;
    }

    public Optional<User> search(Integer id) {
        return usersRepository.search(id);
    }
}

public interface UsersRepository {
    Optional<User> search(Integer id);
}

final class UserSearcherShould {
    @Test
    void find_existing_users() {
        // Now we're injecting to the UserSearcher use case different implementation of the new UserRepository interface.
        // 👍 Win: We can replace the actual implementation of the UsersRepository used by the UserSearcher.
        // That is, we'll not have to modify a single line of the UserSearcher class despite of changing our whole infrastructure.
        // This is a big win in terms of being more tolerant to changes.
        // 👍 Win: It also make it easier for us to test the UserSearcher without using the actual implementation of the repository used in production.
        // This is another big win because this way we can have test such as the following ones which doesn't actually go to the database in order to retrieve the system users.
        // This has a huge impact in terms of the time to wait until all of our test suite is being executed (quicker feedback loop for developers 💪).
        // 👍 Win: We can reuse the test environment repository using test doubles. See CodelyTvStaffUsersRepository for its particularities
        UsersRepository codelyTvStaffUsersRepository = new CodelyTvStaffUsersRepository();
        UserSearcher userSearcher = new UserSearcher(codelyTvStaffUsersRepository);

        Optional<User> expectedUser = Optional.of(UserMother.rafa());

        assertEquals(expectedUser, userSearcher.search(UserMother.RAFA_ID));
    }

    @Test
    void not_find_non_existing_users() {
        // 👍 Win: Our test are far more readable because they doesn't have to deal with the internal implementation of the UserRepository.
        // The test is 100% focused on orchestrating the Arrange/Act/Assert or Given/When/Then flow.
        // More info: http://wiki.c2.com/?ArrangeActAssert and https://www.martinfowler.com/bliki/GivenWhenThen.html
        UsersRepository emptyUsersRepository = new EmptyUsersRepository();
        UserSearcher userSearcher = new UserSearcher(emptyUsersRepository);

        Integer nonExistingUserId = 1;
        Optional<User> expectedEmptyResult = Optional.empty();

        assertEquals(expectedEmptyResult, userSearcher.search(nonExistingUserId));
    }
}

```

Es decir, la clase no define que dependencia utiliza, simplemente que contrato requiere. Desde fuera es desde donde le pasamos la dependencia.

## Keep It Real

## Test
