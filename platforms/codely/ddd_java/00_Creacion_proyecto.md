# Creación del proyecto: Bounded Context y Submodules

##  Bienvenida al curso: Objetivos, ¿qué aprenderás?

Explican los cursos que se tendrian que hacer antes de este curso: 

- SOLID
- Arquitectura Hexagonal
- Testing
- CQRS
- Comunicacion entre microservicios
- DDD

## Estructura de carpetas y acelerando la creación del proyecto

- Estructura en un unico proyecto.
- Las necesidades son para una plataforma de cursos online (BC):
  - Web suscripcion videos  (mooc)
  - Web para administrar plataforma (backoffice)
  - Blog
- Hay aplicaciones (fuera de los BC)
  - moocfrontend
  - moocbackend
  - backofficefront
  - backofficeback
- Este nivel materializa precisamente la idea de que las aplicaciones están fuera de los Bounded Contexts (una aplicación podrá atacar al código de n Bounded Contexts), lo cual supone una gran ventaja en términos de rendimiento ya que nos evitará tener que salir a la red para realizar llamadas Http a la API
- Se entiende que los "frontend" son los puntos de entrada por controladores/API y los backend serian entradas por CLI?
- Estructura de directorios

```
- apps
  - main
    - resources
    - tv.codely.apps
      - backoffice
        - backend
        - frontend
      - mooc
        - backend
        - frontend
  - test (se copia la estructura de directorios, los tests inyectan una request para hacer la prueba)
    - resources
    - tv.codelytv.apps
      - backoffice
        - backend
        - frontend
      - mooc
        - backend
        - frontend
- src
  - backoffice
    - main
      - tv.codely.mooc
        - videos
          - application
          - domain
          - infrastructure
        - courses
        - shared
        - ...
        - roadmap
    - test
      - tv.codely.mooc
        - videos
          - application
          - domain
          - infrastructure
        - courses
        - shared
        - ...
        - roadmap
  - mooc
    - main
    - test
  - shared
    - main
    - test
```

## Monorepo multiproyecto con Gradle

- Utilizan gradle porque simplifica mas que maven
- La idea es que al levantar una aplicacion teiene que empaquetar todos los subproyectos (BC)
- En "settings.gradle":

```groovy
rootProject.name = 'java-ddd-skeleton'

include ":shared"
project(':shared').projectdir = new File("src/shared')

include ":backoffice"
project(':backoffice').projectdir = new File("src/backoffice')

include ":mooc"
project(':mooc').projectdir = new File("src/mooc')
```

- Luego en el "build.gradle" es donde se definen las dependencias, version java
