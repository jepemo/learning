# Shared Kernel

## Qué compartimos entre Bounded Contexts

* Hay elementos que tienen que compartir entre los Modulos/BC
* Utilizan una carpeta llamada shared (puede haber mas de una en distintos niveles).
* Esta al mismo nivel de los elementos que la usan.
*  ¿Qué compartirmos en Shared?
  * Es importante que no saquemos a estas carpetas compartidas aquél código que pensamos que acabaremos compartiendo en múltiples sitios, sino una vez que estamos utilizando ese código en varios sitios y tiene sentido que se esté utilizando en mas de un lugar (Por ejemplo VideoId)
* En el caso de los Value Objects, como por ejemplo TotalDuration que lo encontramos en varios sitios, debemos tener en cuenta a la hora de decidir si extraerlo a Shared si tendran distintas particularidades como el valor máximo, puesto que nos estará indicando que realmente son distintos Value Objects
* Otro caso en el que si podríamos extraer código a Shared es el de Infraestructura a nivel de implementación de clases commo nuestro ReactorEventBus, que podrá ser utilizado desde múltiples contextos. Ojo! 👀que no estamos hablando de las instancias, recordemos que la infraestructura de cada Bounded Context es independiente y tanto nuestro contexto de Backoffice como el contexto de Mooc tendrán distintas BBDD
* A nivel de Módulos dentro de un mismo Bounded Context, al igual que sucede a nivel inter-contextos, extraeremos a Shared aquel código que sea utilizado por distintos módulos de un mismo contexto y que tenga sentido que este utilizándose en múltiples sitios
