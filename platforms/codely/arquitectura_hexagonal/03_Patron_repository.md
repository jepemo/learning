# ¡Nuestro primer puerto y adaptador! Patrón Repository

## Read
* ActiveRecord, la entidad sabe como guardar en BBDD.
  * Por ejemplo: User (al entidad) tiene un save.
  * En aplicaciones pequeñas esta bien. Pero no escala si la aplicación crece.
  * Ya que normalmente hay un monton de "convenciones" para que todo sea medio-automatico.
* Datamapper:
  * Le dices como se mapea la entidad a BBDD de forma externa (Fichero de infraestructura). Entonces la entidad no sabe nada de la BBDD.
* DAO:
  * Dice que el DAO normalmente implementa las operaciones CRUD de una entidad
  * Pero con el paso del tiempo se acaban anyadiendo metodos para cada una de las busquedas: "getAccountByLastName", etc.
  * Se entiende que en el DAO se implementan todas las llamadas a BBDD...sin restriccion
  ```java
  public interface BloatAccountDAO {

      Account get(String userName);
      void create(Account account);
      void update(Account account);
      void delete(String userName);

      List getAccountByLastName(String lastName);
      List getAccountByAgeRange(int minAge, int maxAge);
      void updateEmailAddress(String userName, String newEmailAddress);
      void updateFullName(String userName, String firstName, String lastName);

  }
  ```
* Repository:
  * Definicion: "A Repository represents all objects of a certain type as a conceptual set. It acts like a collection, except with more elaborate querying capability."
  * Es decir: Es una abstraccion que representa una coleccion de objetos. Con las operaciones de: insercion, borrado, actualizacion, consulta.
  * La diferencia principal es que todos los metodos (excepto el de busqueda) tienen de entrada a la entidad. Con lo que aislamos el "PK" de la entidad.
