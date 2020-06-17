# Ubiquitous Language: Jerga del día a día en el código

## Lenguaje ubicuo y flujo de trabajo outside-in en DDD

* Impregnar todo el código con el lenguaje de dominio
* Contribuye a que no se cometan Leaks de Infraestructura hacia nuestra aplicación y nuestro dominio

### Definiendo una nueva Feature

* La feature es crear mostrar el curso: nombre, rating, summary, etc.
* Las dinámicas como **event-storming** resultan super interesantes tanto a la hora de descubrir nuevos contextos, cuando no tenemos una feature concreta También cuando entra una persona nueva al equipo es muy util para que pueda impregnarse de todo ese lenguaje ubicuo del código
* se puede diseñar mediante una herramienta de prototipado o boli, etc.
  * https://marvelapp.com/pop/?popref=1
* Lo primero es definir el contrato (para que los clientes que lo consuman lo sepan) y saber que se tenga que devolver:
  * A nivel del controlador (API)  
* El flujo es desde fuera hacia adentro (->) (outside-in)
* Cualquier equipo que esté desarrollando uno de los clientes podrá mockear la respuesta del servidor y avanzar en su línea de trabajo
* En el lado del servidor ya conoceremos el tipo de información que vamos a tener que devolver, también podremos paralelizar los posibles trabajos que se deriven de esta funcionalidad e impregnar el resto del flujo de la petición con ese lenguaje
  
### Flujo de Petición DDD + CQRS

```
            -> Command/Query (A)                         -> SERVICES (D)
-> Ctrl (I) -> BUS (I) -> Handler (A) -> APP.SERVICE (A) -> MODELS (D)
                                                         -> REPOS        <- REPO IMPL
```

* Para el caso de uso de buscar un curso de la plataforma este sería el flujo que seguiríamos
  * CourseGetController: Al tratarse de Infraestructura, no resulta negativo que el acoplamiento con el protocolo HTTP sea visible en el propio nombre del Controlador
  * FindCourseQuery: Esta Query la enviaríamos al QueryBus, que si será genérico
  * FindCourseQueryHandler: Como vimos en lecciones anteriores el handler estará vinculado a la Query en el QueryBus
  * CourseFinder: Este sería nuestro Application Service, que encapsula de forma atómica nuestro caso de uso. A su vez el caso de uso interacciona con una serie de colaboradores:
    * Services
    * Models
    * Repos
* Gracias al hecho de haber empezado desde fuera hacia dentro (outside-in), será imposible que la infraestructura (la implementación que definamos para la interfaz del repo) condicione el caso de uso. Además, si hemos desarrollado hasta este punto, aunque no hayamos alcanzado los detalles de implementación, podremos ya testear unitariamente nuestro caso de uso
* "El arte del patadón pa’lante" - Eduardo Ferro: Artículo super interesante que resalta la importancia de dejar para el final los detalles de implementación de nuestra aplicación
  * http://www.eferro.net/2016/12/el-arte-del-patadon-palante-posponer.html
