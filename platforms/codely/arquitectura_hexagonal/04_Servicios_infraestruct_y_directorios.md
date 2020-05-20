# Servicios de infraestructura y estructura de directorios

## Teoria

* Relacionado con el patron repositorio (que en parte es un servicio de infraestructura)
* Acoplamiento estructural: se diseña parte del dominio pensando indirectamente como sera la parte de infraestructura. 
  * Clase Mensaje del dominio tiene campos como: Sujeto, cuerpo (mail). Cuidado con las "header interfaces".
* Definir la interfaz en el dominio, que lo implementa la interfaz.
* En las clases de infraestrcutura sse pueden hacer llamadas a librerias externas.
* El constructor del objeto de infraestructura es especifico de este, con detalles de inicializacion, etc.
* A este nivel, la estructura de los proyectos de podria dividis de la siguiente forma:
```
├── entry_point
│   ├── EntryPointDependencyContainer.scala
│   ├── Routes.scala
│   ├── ScalaHttpApi.scala
│   └── controller
│       ├── status
│       ├── user
│       └── video
└── module
    ├── shared
    │   └── infrastructure
    ├── user
    │   ├── application
    │   ├── domain
    │   └── infrastructure
    └── video
        ├── application
        ├── domain
        └── infrastructure
```
* Esta estructura permite:
  * Cohesión y facilidad de encontrar lo que buscas:
    * La aplicación refleja conceptos de dominio antes que conceptos relacionados con la arquitectura de Software. Esto visibiliza más nuestro dominio haciendo que sea más fácil de encontrar lo que buscas
    * Los conceptos relacionados con un mismo módulo están más cerca unos de otros. Esto hace que se más fácil moverse entre los distintos componentes necesarios a modificar.
  * Escalabilidad del código/mantenibilidad
    * Uno de los principales motivos por los que separar nuestra aplicación en módulos o sub-dominios es el de promover la mantenibilidad de la aplicación a lo largo del tiempo. Con lo cuál, podría tener sentido buscar el aislamiento entre los distintos módulos de nuestra aplicación. Desde el momento en el que son unidades atómicas (cada carpeta de modules + la de shared autocontiene todo lo necesario para su funcionamiento), esto se torna más fácil.
    * Podemos elevar el aislamiento entre módulos a través de un Command y Query Bus como se ve en el curso de CQRS. Esto haría que los módulos no se conocieran entre sí (no podríamos hacer uso del repositorio del módulo de vídeos desde el módulo de usuarios por ejemplo). La comunicación se haría a través del bus.
    * Esto facilitaría una eventual promoción de los módulos a Bounded Context, servicios aislados, o división de los módulos en caso de que alguno empiece a crecer mucho.

## Test
¿Cómo le especifico el canal de Slack al que enviar notificaciones en mi adaptador para notificar nuevos vídeos publicados?
- [ ] Parámetro de tipo SlackChannel en método notify
- [ ] Parámetro sin tipado estricto en método notify para poder pasar otro tipo de valor como el email de destino en el caso del notificador vía email
- [x] Inyección de parámetro vía constructor de clase ya que no está en la interface

¿Qué puedo hacer para evitar enviar emails de verdad al ejecutar mis tests?
- [x] Mockear el componente de infraestructura, o inyectar una implementación fake
- [ ] Especificar emails falsos como datos de test
- [ ] Mockear el servidor de envío de emails para que cuando mi implementación lo llame, éste no haga nada

¿Cuándo se da el acoplamiento estructural?
- [x] Cuando nos hemos desacoplado a nivel de código de una implementación gracias a una interface, pero esta interface sigue exponiendo semántica de la implementación, nos obliga a usar los métodos en un determinado orden, o en resumen la interface y su uso se ve influenciado por alguna implementación
- [ ] Cuando la estructura de carpetas de nuestra aplicación tiene mucho acoplamiento a los conceptos de dominio
- [ ] Cuando estructuramos las interfaces pensando en los clientes que las van a usar y no en las implementaciones que tenemos
