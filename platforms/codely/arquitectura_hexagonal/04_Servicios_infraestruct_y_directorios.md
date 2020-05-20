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
