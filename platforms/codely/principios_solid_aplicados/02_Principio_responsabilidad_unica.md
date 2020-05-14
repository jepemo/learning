# Principio de Responsabilidad Única
* Una clase debe representar un unico concepto y responsabilidad.
* Solo debe tener una razon para cambiar
* Clases de servicios pequeñas con objetivos acotados
* Servicios:
  * Utiliza los modelos de dominio
  * Orquestra (serie de pasos)
  * Toca infraestructura
  * Llama otros servicios
  * Si un servicio tiene mas de un metodo publico, entonces probablemente haga mas de una cosa  != SRP
* Modelo de dominio:
  * Datos + Comportamiento
  * Modelos anemicos?
* Finalidad:
  * Alta cohesión y robustez
  * Permitir composición de clases (inyectar colaboradores)
  * Evitar duplicidad de código
