# Preguntas frecuentes

## Cómo convencer al equipo para aplicar DDD

* Hay que indentificar la necesidad real en la que tenga sentido aplicar las tecnologias.
* Hay que ligarlo a los objetivos de negocio
* Puede que no interese utilizar todas las tecnicas relacionadas con DDD:
  * CRQS
  * Arquitectura Hexagonal
  * Value Objects
  * Agregados
  * Solid
* Sino la que pueda aportar valor en el momento

## ¿Buses síncronos vs. Asíncronos? ¿Integración en framework?

### Buses síncronos vs. Asíncronos

* Una petición asíncrona implica que una vez ha sido enviada al servidor, lo que éste nos va a responder no es el resultado de haberla procesado hasta el final, sino que nos contestará indicándonos que ha registrado dicha petición y que la procesará en algún momento
* Este tipo de peticiones constituyen un reto a nivel de UI si pensamos en la comunicación Cliente-Servidor tradicional ya que, al no tener un canal de comunicación full-duplex por el cual el servidor pueda avisar al cliente de que ha procesado la petición, nos obliga a tener que estar preguntando periódicamente al servidor si tiene lista la respuesta mientras mantenemos alguna renderización falseada en el cliente que simule el tener ya dicha respuesta. El problema de esto es que podemos acabar friendo al servidor con tantas peticiones
* Al margen de los truquillos que podamos utilizar en comunicaciones ‘tradicionales’, en este tipo de casos en los que el cliente queda a la espera en un flujo asíncrono lo óptimo es utilizar canales de comunicación bidireccionales como los websockets. Igualmente, dado el grado de complejidad que añade el manejo de la asincronía, es importante considerar en qué casos nos aporta más beneficios que complicaciones

### Integración en framework

* Una cuestión importante a la hora de diseñar nuestra aplicación es hasta que punto atarnos a un framework, ya que esto nos va a aportar tanto beneficios como algunos inconvenientes Por ejemplo, en lo que refiere a envío peticiones y respuestas (vease Controllers) podemos sacar mucho provecho del framework, y esto irá a nivel de Infraestructura desde el momento en que tenemos en estas clases un use/import de alguna librería externa (a pesar de estar en el punto más externo de la aplicación
* Por otro lado, la capa de Aplicación si que nos interesa que sea puro en el sentido de mantenerlo sin acoplamientos a cosas externas. Ante el debate sobre si algo debe mantenerse en el Controller (acoplado a la infraestructura) o si lo metemos en Application Service, la regla de oro es: Si lo metemos en el Controller y tenemos un nuevo punto de entrada, ¿Tendremos que duplicar el código en ese nuevo punto de entrada? Si es así, estaremos ante una evidencia clara de que debemos empujarlo a la lógica de negocio
* Un Tip que nos puede ayudar a decidir qué lógica va en la Aplicación o en el Controlador es considerar que las definiciones de negocio irán precisamente dentro de la lógica de negocio de la aplicación
* Otros puntos de nuestra aplicación donde también podemos encontrar beneficioso hacer uso del framework y librerías externas son aquellos en los que realicemos un mapeo a base de datos (Doctrine en el caso de PHP o Hibernate para Java). En este caso añadiremos la Interfaz de Dominio a modo de barrera para separar estos elementos de Infraestructura.
* Las validaciones de dominio también son un punto de nuestra aplicación en el que podríamos requerir de librerías externas y para ello, lo más adecuado será englobarlas dentro de un Value Object de modo que fuera de éste no encontraremos ningún use/import externo

## ¿Transaccionabilidad? ¿Sagas? ¿Lógica de Agregados?

### Qué lógica poner en los Agregados

* Recapitulando, un agregado no es más que un elemento conceptual que agrupa aquellos modelos de dominio alrededor de un mismo concepto. Debemos partir siempre de la norma de empujar la lógica de Dominio lo más hacia dentro posible para tener mayor cohesión. Esta cohesión se traduce en que la lógica esté lo más cerca posible de los atributos/valores a los que haga referencia. Así, si se da el caso en que la lógica que encapsulamos en una clase se relaciona más con los atributos de otra clase, lo que debemos hacer es mover la lógica a esa otra clase Dentro de los Value Objects también encontraremos lógica relacionada con las validaciones, pero ojo 👀, en el momento en que esta lógica involucre a varios Value Objects (por ejemplo, comprobar que un usuario de Tipo administrador no puede tener un Email de un dominio externo a la empresa) la recogeremos dentro del propio Agregado
* Sin embargo, pese a ser también validaciones, cuando la lógica implique entrada/salida de datos (por ejemplo, comprobar que no exista el Email en BD), no podremos mantenerla dentro del Agregado, sino que se quedará en el caso de uso. En general, siempre que necesitemos un servicio/colaborador o toquemos entrada/salida esa lógica no podrá ir dentro del Modelo

### Agregados con 8 campos… Lazy Loading?

* Los ORM suelen hacer uso de Lazy Loading para cargar las relaciones entre tablas para evitar hacer el SELECT de esa otra tabla hasta que no se interaccione con ello.
* Sin embargo, creemos que puede no ser muy buena idea hacer uso de Lazy Loading. Por una parte, esto lleva a que nuestro agregado acabe sabiendo de sobre la Infraestructura, conociendo qué queries se tienen que ejecutar (El ORM podría ocuparse de todo esto de forma automágica). Por otra parte, estamos perdiendo el control explícito sobre cuando tiene lugar la carga computacional y la entrada/salida de datos
* Una solución posible es serializar toda la información relacionada y guardarla en una sóla columna en BD de modo que podamos recuperarlo de golpe y en mucho menos tiempo

### 1 Agregado / Request

* Seguimos la norma de un sólo agregado mutado a la vez por request porque de lo contrario incurriremos en términos de transaccionalidad (no podemos deshacer una transacción que afecta a dos BD distintas)
* La opción de Sagas-Transacciones entre Microservicios añade una complejidad muy alta dentro de nuestro código y por lo general podremos evitarla gracias a Event-Driven Architecture
