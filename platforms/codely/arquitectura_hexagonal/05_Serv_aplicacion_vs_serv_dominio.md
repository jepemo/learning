# Servicios de Aplicación vs. Servicios de Dominio

## Teoria

* Servicio de aplicacion
  * Puntos de entrada
  * Suele realizar la gestión de errores. Ejemplo: Servicio de dominio devuelve "nulo" (si buscamos). Desde aqui podemos lanzar excepcion.
  * Estos son los que realizan las transacciones, de lo que pueda pasar en las diferentes llamadas de dominio.
  * Al utilizar los servicios de dominio en los de aplicaciones, podemos instanciarlos directamente, es decir, no utilizar interfaces, ya que normalmente del dominio no nos queremos desacoplar.
  * Publicarán los eventos de dominio respectivos.
  * Coordinan las llamadas a los distintos elementos de nuestro sistema para ejecutar un determinado caso de uso.
  * Les llamaremos indistintamente Servicio de Aplicación como caso de uso.
* Servicio de dominio
  * Suele ser logica que puede que estviera implementada en un servicio de aplicación. Pero como necesitamos invocarla desde otro servicio, la movemos al dominio para que se pueda llamar desde los dos servicios de aplicacion.
  * Ejemplo de lo anterior, podria ser un servicio de busqueda de una entidad, que necesitariamos utilizar en el "find" y el "update" en aplicacion.
  * Estos servicios nunca finalizaran transacciones
  * No publican eventos de dominio
  
## Test

Si tenemos un caso de uso tal que "AddProductToCart" que hace uso de un servicio de dominio "ProductToCartAdder", ¿Quién publicará el evento de domino "ProductAddedToCart"?
- [ ] Product (modelo de dominio)
- [ ] Cart (modelo de dominio)
- [ ] MySqlCartRepository (repositorio de infraestructura)
- [ ] ProductToCartAdder (servicio de dominio)
- [x] AddProductToCart (servicio de aplicación)
- [ ] AddProductToCartCliController (controlador)

¿Es necesario definir una interface para nuestros servicios de dominio?
- [ ] Sí. Los servicios de dominio son un punto crítico que puede cambiar por decisiones externas a nuestro negocio y queremos evitar el acoplamiento
- [ ] Sí. Cuando ejecutemos nuestros tests nos interesará que no se use la implementación real del servicio de dominio para que se ejecuten más rápido.
- [x] No. Los servicios de dominio sólo deben cambiar por cambios de nuestra lógica de negocio, y queremos que se testeen siempre de forma indirecta al testear nuestros casos de uso.

¿Encapsularemos siempre nuestra lógica de negocio en servicios de dominio?
- [x] No. Sólo si es necesario reutilizarla desde múltiples casos de uso, o si queremos encapsularla por "limpiar" el Servicio de Aplicación y dejarlo más legible en caso de ser complejo.
- [ ] Sí. Sólo así cumpliremos con una Arquitectura Hexagonal bien implementada asegurando la cambiabilidad.
