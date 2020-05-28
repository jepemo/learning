# Command y Query Bus - ¿Qué son?

## Command y Query Bus - ¿Qué son?

* Enfoque **"clasico"**:
  * Implementar la logica en la primea clase que recibe la peticion.
  * Ejemplo: ponerlo todo en el Controlador
  * El problema de esto es que no es posible reutilizar esa logica.
  * Si hubiera otro punto de entrada para ese caso de uso, no se podria aprovechar y se tendria que duplicar.
* Enfoque **Hexagonal**:
  * El controlador no tiene la logica, la tiene el "caso de uso".
  * El caso de uso, implementa la logica de el caso de uso (capa de servicio/application service)
  * El problema es si interesa acoplar el caso de uso en los clientes (controladores/clientes etc.)
* Enfoque **CQRS**:
  * Va igualmente al controlador
  * Este instancia el DTO (command) y lo tira al BUS
  * El BUS no cambiara (se extendera)
  * El BUS es el que sabe, segun el tipo de comando a que "CommandHandler" ira.
  * Esto aporta desacoplamiento
    * Podríamos incluso tener los controladores en un determinado lenguaje de programación, y los servicios que ejecuten la lógica de negocio en otro.
    * El "controlador" no sabe nada de los casos de uso.
  * Otro cliente, simplemente lanzaria el mismo "command" y ya esta.
  * Se puede usar la asincronia (Mejora rendimiento)
  * Tambien de podria envolver nuestros handlers o casos de uso con middlewares para que ejecuten ciertas lógicas transversales como logging, transaccionabilidad, etc.
  
## Test

Si nuestra aplicación no tiene unos altos requisitos de rendimiento, pero sí queremos mantener una alta modularidad o reutilización de la lógica de negocio, ¿qué usaremos?
- [ ] Lógica implementada directamente en los controladores (puntos de entrada)
- [x] Lógica en servicios (casos de uso / Application Services / Actions)
- [ ] Lógica en servicios y command/query bus intermedio para distribuir las peticiones

¿Qué beneficios aporta el command/query bus?
- [ ] Unifica los buses y las queries, eso está bien
- [ ] Desacopla. Siempre hay que buscar el desacoplamiento
- [ ] Unifica el punto de decisión de qué caso de uso ejecutar
- [ ] Permite ejecuciones de lógica de negocio asíncronas en lenguajes de programación donde no es tan viable
- [ ] Añade un punto de indirección único donde poder añadir middlewares con lógicas transversales a todos los casos de uso
- [ ] 1, 2 y 3 son correctas
- [x] 3, 4 y 5 son correctas
- [ ] 2, 4 y 5 son correctas
- [ ] 2, 3, 4 y 5 son correctas

