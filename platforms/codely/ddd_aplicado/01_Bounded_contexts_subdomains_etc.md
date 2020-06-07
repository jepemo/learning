# Bounded Contexts, subdomains y modules: Creando nuestra aplicación

## Cómo definir Bounded Contexts

* Los Bounded Context son agrupaciones flexibles que pueden cambiar a lo largo del tiempo
* Lenguaje ubicuo: palabras de negocio que se utilizan para definir conceptos en el codigo
  * Por ejemplo en Codely: La Home, el Backoffice, el Mooc, el Blog…
* Ejemplo de separacion logica, primer pensamiento: Frontend y Backend
* Ejemplo: La separación lógica que estableceríamos sería a nivel de bounded contexts:
    * Mooc
    * Backoffice del Mooc
    * Blog
 * Además dentro de los BoundedContext hay modulos (mini-bounded-context):
   * Son elementos que tienen sentido dentro de un bounded context.
   * Ejemplo: 
     * En Mooc serian: Videos, Courses, Estudiantes, etc.
     * En Backoffice serian: Courses, tickets, estudiantes, etc.
  * Aplicaciones (cómo y donde queremos desplegar):
    * Web, dispositivos móviles, etc
    * Si tenemos nuestras aplicaciones en el mismo repo que los bounded contexts, nuestras aplicaciones web podrán comunicarse con estos bounded contexts sin necesidad de salir al exterior del servidor (No hará falta establecer comunicaciones HTTP, TCP, …) mejorando enormemente la latencia en nuestra aplicación
    * Ejemplos de aplicaciones:
      * MoocFrontend (Cliente WEB), MoocBackend (API), BackofficeFront., BackOfficeBack., etc.
      
### Alternativas

* Existirian otras formas de organizar el codigo.
* Ejemplo 1: Apps dentro de los Bounded Contexts
  * Ventajas: Codigo Autocontenido y mas recogido
  * Inconvenientes: Puede ser engorroso si nuestra aplicación tiene que llamar no solo a la api de su bounded context sino a otras externas
* Ejemplo 2: Modulos dentro de las Apps (frontend y backend que contendrían a los módulos.):  
  * Ventajas: El código está agrupado a nivel de conceptos
  * Inconvenientes: Estaríamos confundiendo los módulos propiamente dichos con una agrupación de código por conceptos
  
* Esto al final es un proceso iterativo, en el que se quiere
  * Aislarse para no chocar entre varios equipos/desarrolladores que trabajan cada uno en su BC
  * Tener la comunicacion en una direccion, sin tener que salir fuera para tener que llamar a otro sitio.
  
* Ejemplo codigo: https://github.com/CodelyTV/php-ddd-example

## Diferencias entre Bounded Contexts, Subdomains, Modules, y Shared Kernel

* **Context Map**: "Mappea" los conceptos del dominio a los "Boounded Context"
* **Subdomain**: Hace referencia exáctamente a lo mismo que los Bounded Contexts. Mientras que Subdomain estaría en el terreno de la problemática que queremos resolver, Bounded Context estaría en el terreno de la solución que damos a dicho problema.
* **MicroServicio**: Es una práctica habitual desplegar aplicaciones como Microservicios. Aunque normalmente suele ir en relación 1 a 1 con los Bounded Contexts, también es posible que se relacionen 2 microservicios(Por ejemplo la parte backend y frontend) con un mismo "contexto".
* **Shared Kernel**: Se trata de código compartido entre Bounded Contexts y entre Módulos dentro de un mismo Bounded Context (También podemos encontrarlo bajo el nombre de Common o Shared). Aquí dejaremos las cosas con la menor lógica posible para no generar acoplamiento en los contextos.
  * Tip: Si nos llevásemos un Bounded Context en otro proyecto distinto, tendríamos que llevarnos tanto ese Bounded Context como la carpeta de Shared Kernel


|                                        | Framework coupled code | Modules | Bounded Contexts       | Microservices          |
|----------------------------------------|------------------------|---------|------------------------|------------------------|
| **Learning Curve**                     | Low                    | Medium  | High                   | High++                 |
| **Teams autonomy**                     | Low                    | Medium+ | High                   | High++                 |
| **Infrastructure**                     | Shared & Coupled       | shared  | Isolated & distributed | Isolated & distributed |
| **Code maintainability/extensibility** | Low--                  | High    | High+                  | High++                 |
| **Infrastructure complexity**          | Low                    | Medium  | High                   | High++++               |
| **Comunication Between**               | Coupled                | Buses   | Buses                  | Distributed Buses      |
| **Deploy**                             | Shared                 | Shared  | Shared                 | Isolated               |


* **Learning Curve**: La curva de aprendizaje se incrementa considerablemente cuando nos enfrentamos a un sistema distribuído entre distintos microservicios frente a aquel código acoplado al framework en el que todo está junto. Por eso, lo ideal es avanzar progresivamente, iterando en los distintos estadios hasta llegar a una estructura de microservicios.
* **Autonomía de los equipos**: Trabajar con Bounded Contexts y Microservicios nos va a permitir separar los equipos de modo que puedan desarrollar y desplegar de manera independiente. Al otro lado, trabajar con un código acoplado nos obliga a que los equipos coincidan en el mismo código tanto al desarrollarlo como en los despliegues.
* **Infraestructura**: En un código acoplado al framework, puesto que todo está unido, podemos toparnos con un efecto dominó 🀄 de modo que si una de las piezas implicadas falla, todo lo demás falle. En el otro extremo, al estar aislada la infraestructura, si una de ellas falla (Por ejemplo la referente a Usuarios) el resto seguiría funcionando con normalidad.
* **Mantenibilidad/Extensibilidad del código**: Por supuesto, cuanto más desacoplado y aislado esté nuestro código, más fácil será mantenerlo y extenderlo. Como hemos comentado en otras ocasiones, tener nuestro código fuertemente acoplado nos obligará a que cada modificación que hagamos lleve a tocar en múltiples sitios.
* **Complejidad de la Infraestuctura**: Tener menos elementos implicados, como en el caso del código acoplado, supone una menor complejidad en términos de infraestructura. Por eso al trabajar con Bounded Contexts y especialmente con Microservicios, estaremos aumentando bastante su complejidad (No será lo mismo tener un sólo deploy y una sóla BD que tener múltiples deploys y trabajar con varias BBDD).
* **Comunicación entre ellos**: En el caso del código acoplado, la comunicación será inevitablemente acoplada (Por ejemplo a través de Inyección de Dependencias). Por otro lado, la comunicación puede ser a través de Buses en el caso de Módulos y Bounded Contexts, o por medio de Buses distribuidos entre Microservicios
* **Despliegue**: Respecto a nivel de Despliegue, el cambio se observa en el paso a Microservicios, donde será aislado para cada uno de ellos, lo cual nos permitirá una mayor escalabilidad (Se despliega una parte concreta de nuestra aplicación)


