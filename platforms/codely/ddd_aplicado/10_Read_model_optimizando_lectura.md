# Read Model: Optimizando para la lectura

## Comunicar modules y Bounded Contexts: Query Bus vs Eventos

* En el ejemplo anterior, nos comunicabamos con otro modulo con el querybus
  * Pero no siempre nos puede interesar comunicarse de esa forma
* El ejemplo que utilizan sigue la siguiente estructura: Lesson -> Step -> Duration
  * Se quiere saber la duracion estimada de una lesson
* Tienen dos servicios

```
--> GET /lessons/x --> [ Lessons Module]           [Steps Module] <-- PUT /steps/x --
                              |                         |
                              |                         |
                              v                         v
                           [BBDD]                    [BBDD]
```

* Una forma de comunicar los BC es que Lessons Module llame a StepsModule con una Query
  * FindStepsQuery
  * Inconvenientes 👎
    * Estamos generando acoplamiento entre módulos
    * Tendremos problemas de rendimiento si debemos estar realizando múltiples queries cada vez que queramos recuperar los detalles de una Lección
    * Podemos acabar con un caso de uso enorme en el que encontremos un montón de queries
    * Necesidad de añadir un campo duration a Lesson como nullable o añadirlo en la response aunque no exista en el agregado
* Otra forma seria lanzar un evento de dominio de "step_created"
  * Lessons module estaria suscrito y actualizaria su proyeccion
  * Es decir, su campo de "estimated_duration".
  * Para evitar problemas de calcular la duracion con la informacion del evento.
    * Al recibir el evento podria hacer una query para recoger el "Step" y consultar su duracion
