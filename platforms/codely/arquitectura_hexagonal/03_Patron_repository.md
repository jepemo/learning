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
 ```java
 public interface AccountRepository {

     void addAccount(Account account);
     void removeAccount(Account account);
     void updateAccount(Account account); // Think it as replace for set

     List query(AccountSpecification specification);
 }
 ```
  * A diferencia de las colecciones normales. Se implementa un metodo de busqueda, con el patron Criteria. El cual permite flexibilizar esas busquedas, aunque aumenta la complejidad.
  * Mas información: https://thinkinginobjects.com/2012/08/26/dont-use-dao-use-repository/
  
Ejemplo:
* En la capa de aplicacion (caso de uso), se instancia la entidad de dominio y se llama al repositorio para que la guarde. 
* La interfaz del repositorio esta en el DOMINIO.
* Capa de aplicacion solo tiene "imports" de dominio.
* La clases del caso de uso (servicio de aplicacion) tiene como dependencia en el constructor el repositorio.

## Test
Para implementar una Arquitectura Hexagonal, ¿Qué patrón de diseño a nivel de repositorio deberemos usar?
- [ ] ActiveRecord
- [x] DataMapper

¿En qué capa de la Arquitectura Hexagonal ubicaremos las interfaces de nuestros repositorios (puertos)?
- [ ] Infraestructura
- [ ] Aplicación
- [x] Dominio
- [ ] Tanto Infraestructura como Aplicación son válidas
- [ ] Tanto Infraestructura como Dominio son válidas
- [ ] Tanto Aplicación como Dominio son válidas
- [ ] Tanto Aplicación como Infraestructura son válidas

¿En qué capa ubicaremos las implementaciones de los repositorios (adaptadores)?
- [x] Infraestructura
- [ ] Aplicación
- [ ] Dominio
- [ ] Tanto Infraestructura como Aplicación son válidas
- [ ] Tanto Infraestructura como Dominio son válidas
- [ ] Tanto Aplicación como Dominio son válidas
- [ ] Tanto Aplicación como Infraestructura son válidas

¿Por qué ubicar cada componente (puertos y adaptadores) en las dichas capas?
- [ ] Por que así tendremos todo más organizado
- [x] Porque gracias a la regla de dependencia, garantizaremos la tolerancia al cambio aislando conceptos externos
- [ ] Porque lo dice CodelyTV
- [ ] Porque gracias a la regla de dependencia, la capa de Aplicación sólo conocerá aquella implementación que use y no todo el resto del sistema
- [ ] Porque gracias a la regla de independencia, la capa de aplicación tendrá derecho a decidir
