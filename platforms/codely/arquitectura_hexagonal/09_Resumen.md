# Resumen

* Ayuda a disminuir la complejidad accidental
* Capas de la Arquitectura Hexagonal: infraestructura, dominio, aplicacion
* Cómo definir un puerto para nuestros repositorios de base de datos.
* Servicios de Aplicación vs. Servicios de Dominio.
* Cómo modelar nuestro dominio (patrón de diseño Value Object, named constructors…).
* Cómo publicar eventos de dominio en RabbitMQ. Qué alternativas tenemos a la hora de publicar eventos.
* Flujo de una petición.
* Estrategia de testing para test unitarios y de integración.
* Preguntas:
  * ¿Si se utiliza un servicio de dominio en varios casos de uso, porque no inyectarlo en vez de instanciarlo?
    * Se puede hacer (si esta controlado)
    * Es mejor no hacerlo ya que:
      * Se ha dicho que solamente habria que inyectar las interfaces de dominio de la infraestructura
      * Complicaria el testing, ya que entonces habria que instalarlo en cada uno de los test.
