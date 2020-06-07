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


|                                    | Framework coupled code | Modules | Bounded Contexts       | Microservices          |
|------------------------------------|------------------------|---------|------------------------|------------------------|
| Learning Curve                     | Low                    | Medium  | High                   | High++                 |
| Teams autonomy                     | Low                    | Medium+ | High                   | High++                 |
| Infrastructure                     | Shared & Coupled       | shared  | Isolated & distributed | Isolated & distributed |
| Code maintainability/extensibility | Low--                  | High    | High+                  | High++                 |
| Infrastructure complexity          | Low                    | Medium  | High                   | High++++               |





