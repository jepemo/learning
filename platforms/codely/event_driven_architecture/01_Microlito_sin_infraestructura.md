# Alternativa 1: Microlitos sin infraestructura

## Teoria

* Microlito = Microservicio + Monolito
* Tenemos el problema de tipos de clientes distintos con cargas distintas
* Este enfoque divide en servicios, pero utilizando la misma infraestructura: BBDD
* ¿Cuando pasar a (micro)servicios(s)? Aspectos:
  * Escalabilidad equipos de desarrollo
  * Escalabilidad implementación (ecosistema específico por necesidad)
  * Escalabilidad aplicación (recursos específicos por necesidades)
  * Escalabilidad infraestructura (cuello de botella entre necesidades)
  * No es un todo o nada
* En el ejemplo, de solucion, dividimos los dos casos de uso (de cargas distintas) en dos servicios diferentes

```
(Movil) GET /users/x ---> [UsersService]    [VideosService] <--- PUT /videos/x (Web)
                               |                |
                               |                |
                               v                v
                                  [MISMA BBDD]
```
* En este caso, el servicio (de subida de videos) reacciona bien, porque el se ha optimizado para eso.
* EL problema es que la BBDD es ahora el cuello de botella
* Se ha cambiado a un escenario:
  * 📊 👍 Escalabilidad aplicación (distinto ecosistema y recursos por necesidad)
  * Escalabilidad equipos de desarrollo (gestión CVS 👍, DB schema 👎)
  * 🎯 👎 Añadimos niveles de indirección
  * 🍼 👎 Escalabilidad infraestructura (cuello de botella)

## Test

* ¿Hemos ganado algo con la alternativa de Microlitos sin infraestructura?
- [ ] No, seguimos teniendo los mismos problemas de antes
- [ ] Sí, ahora todos se piensan que tenemos microservicios y lo podemos poner en las ofertas de trabajo para molar un poco más
- [x] Sí, ahora puedo usar el lenguaje de programación o framework más óptimo para cada necesidad a nivel de aplicación
