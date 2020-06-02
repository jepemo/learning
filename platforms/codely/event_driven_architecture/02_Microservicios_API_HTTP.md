# Alternativa 2: Microservicios comunicándose usando APIs HTTP

## Teoria

* En el caso anterior, aunque los servicios escabalan bien a nivel de codigo, estaba el cuello de botella de la BBDD (infraestructura)
* En este caso, los cambios son (cada servicio tiene su infraestructura):

```
(movil) GET /user/x -----> [USERS SERVICE] -- GET /videos?user=x -> [VIDEOS SERVICE] <------ PUT /videos/x ----- (web)
                                 |                                      |
                                 |                                      |
                                 v                                      v
                                BBDD                                   BBDD
```

 * En este caso, el problema es que mientras el servicio de usuarios va bien (en principio), el de videos sigue teniendo problemas (porque tiene mas carga). Con lo que el servicio de usuarios al final dara problemas tambien, si tiene que consultar el de videos.
 * Changelog (cambios respecto a la anterior arquitectura)
   * Ganancias:
     * 👍 Escalabilidad infraestructura (cuello de botella)
     * 👍 Escalabilidad equipos de desarrollo (gestión CVS 👍, DB schema 👍) 
   * Perdidas:
     * 👎 Escalabilidad implementación (consumidores condicionan definición)
       * Se acopla informacion de clientes en el servicio de videos
     * 👎 Añadimos niveles de indirección
       * En este caso llamando a traves de HTTP (o otra forma de comunicacion)
     * 👎 Escalabilidad dependiente de otros servicios (acoplamiento, efecto dominó)
     * 👎 Añadimos latencia de comunicación entre servicios
     * 👎 Requiere más desarrollo (query SQL vs. exponer y consumir endpoint)
     
## Circuit breaker: Hystrix

* Un circuit breaker permite:
  * Evitar saturar otros servicios si ya están caídos
    * Se guarda en un estado interno si el servicio esta fallando.
    * Despues de cierto umbral, abre el circuito (y avisa al cliente que esta caido)
    * Luego, despues de cierto tiempo, vuelve a intentar cerrar el circuito.
  * Caching de resultados
  * Monitorización y cambios de configuración en tiempo real
  * Concurrencia: Operaciones (llamadas a servicios terceros) en batch
  * Basicamente, evita el efecto DOMINÓ.
* Changelog:
  * (+) Se reduce la latencia (caching) y evitamos efecto domino (circuit breaker)
  * (-) Escalabilidad implementacion (consumidores condicionan definicion)
  
## Test

¿En qué ayudan los circuit breakers?
- [x] Esencialmente, en evitar realizar más peticiones a un servicio ya saturado "abriendo el circuito" sin dejar pasar más llamadas
- [ ] Evitar consumo de ram al cargar demasiados objetos en memoria
- [ ] Pintar el cielo de púrpura, el mar de rosa, y las nubes de color arcoíris 🌈
 
