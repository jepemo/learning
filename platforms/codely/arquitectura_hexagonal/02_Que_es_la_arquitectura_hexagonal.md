# Qué es la Arquitectura Hexagonal ?

## Watch: Qué es la Arquitectura Hexagonal?

* Es un tipo de arquitectura limpia
  * Hay capas en nuestra aplicacion y las dependencias entre estas es desde fuera hacia adentro.
  * Ejemplo: UI -> Controllers -> Use Cases -> Entities
  * Esto permite cambiar algun componente de "fuera" sin que lo de "dentro" se entere. Ejemplo: Cambiar la UI sin tocar la BLL.
* Tambien llamada arquitectura de "Puertos" y "Adaptadores".  
  * Los **puertos** son las interfaces definidas en la capa de dominio para desacoplarnos de nuestra infraestructura. Ejemplo: UserRepository
  * Los **adaptadores** son las implementaciones posibles de esos puertos. Estas implementaciones traducirán esos contratos definidos en la interfaz a la lógica necesaria a ejecutar en base a un determinado proveedor. Ejemplo: MySqlUserRepository
* Capas de la arquitectura HEXAGONAL: **Infraestructura -> Aplicacion -> Dominio**
  * Dominio: Conceptos que están en nuestro contexto (Usuario, Producto, Carrito, etc), y reglas de negocio que vienen determinadas en exclusiva por nosotros (servicios de dominio). Tambien las interfaces de la infraestructura?
  * Aplicacion: La capa de aplicación es donde viven los **casos de uso** de nuestra aplicación (registrar usuario, publicar producto, añadir producto al carrito, etc). 
  * Infraestructura: **I/O**. Código que cambia en función de decisiones externas. En esta capa vivirán las implementaciones de las interfaces que definiremos a nivel de dominio. Es decir, nos apoyaremos en el DIP de SOLID para poder desacoplarnos de las dependencias externas. También estaran las llamadas a librerias externas.
* En el caso de la arquitectura "en capas" de siempre seria: Presentacion -> Dominio -> BBDD
  * Modelo y DDBB junto. Por ejemplo ActiveRecord
  * Existe acoplamiento y no es posible intercambiar componentes de capas.
* Para testar la arquitectura:
  * Test unitarios: Capa de Aplicación y Dominio
  * Test de integración: Capa de Infraestructura
  * Test de Aceptación: Todas las capas
* Flujo y tests:
```
|- Infraest. ---|------- Aplicacion ----------------|-- Dominio ---|-- Infraest. -----------|
 -> Controlador -> ApplicationService (Caso de Uso) -> Servicios
                                                    -> Modelos
                                                    -> Repos  
                                                          ^---------- Implementacion
                                                           
                    | ------ Test Unitario ------------------------|--- Test Integracion ---|
|----------------------- Test de Aceptacion ------------------------------------------------|
```
 
## Test
¿Cuál es la regla de dependencia?
- [ ] Aplicación -> Infraestructura -> Dominio
- [ ] Aplicación -> Dominio -> Infraestructura
- [ ] Dominio -> Aplicación -> Infraestructura
- [ ] Dominio -> Infraestructura -> Aplicación
- [ ] Infraestructura -> Dominio -> Aplicación
- [x] Infraestructura -> Aplicación -> Dominio

Dónde ubicaremos el caso de uso de registrar usuario
- [ ] Modelo de domino User
- [ ] Servicio de Dominio RegisterUser
- [x] Servicio de Aplicación RegisterUser
- [ ] Repositorio UserRepository

¿Qué pasaría si no definiéramos una interface en dominio y atacásemos directamente a la implementación en infraestructura?
- [ ] El caso de uso pasaría a ser asíncrono y resolvería las dependencias a través del handler
- [x] Si tenemos que cambiar la implementación a usar de infraestructura deberíamos de ir a todas las clases de aplicación que usaban la anterior haciendo los cambios pertinentes
- [ ] Deberíamos modificar nuestra regla de dependencia para poder seguir cumpliéndola y así asegurar la cambiabilidad

## To-Do: A practicar

* A partir de una MV de VBox con Debian 10.4
* Se han seguido las instrucciones oficiales para instalar docker: https://docs.docker.com/engine/install/debian/
* Luego se ha hecho un fork de ambos proyectos y se han seguido las instrucciones.
* El caso del proyecto de Scala ha sido un poco mas complejo ya que se ha tenido que instalar el paquete openjdk y sbt.
