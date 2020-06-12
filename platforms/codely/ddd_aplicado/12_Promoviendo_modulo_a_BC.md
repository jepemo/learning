# Promoviendo un Módulo a Bounded Context

## Promoviendo el módulo Notifications a Bounded Context

* Si un modulo crece mucho, quizas hay que moverlo a un BC
* El ejemplo que plantean es que el modulo "Notifiaciones" de dentro de "mooc" esta creciendo mucho.
  * Nuestra aplicación tenía originalmente dos contextos (Backoffice y Mooc) además de un contexto compartido Shared, sin embargo la situación ha cambiado desde que definimos estos contextos, de modo que ha surgido la necesidad de montar un equipo de desarrollo en torno a las Notificaciones, que hasta ahora se definía como un módulo dentro de Mooc
* La carpeta de "Notificaciones" se sube al mismo nivel que Mooc/Backoffice en "src".

### Consideraciones para promover un Módulo a Bounded Context

#### Clientes

La promoción a Bounded Context debería ser transparente para los clientes. Gracias al Query/Command Bus vamos a estar totalmente desacoplados y no tendremos el problema de tener que realizar modificaciones en los clientes.

#### Infraestructura

Será necesario crear una nueva infraestructura y migrar los datos del nuevo Bounded Context. Esto supone un trabajazo por parte del equipo de desarrollo, pero puesto que esta promoción surge de una necesidad, entendemos que el equipo querrá hacer modificaciones en la estructura de datos en base a los nuevos casos de uso que surjan

#### Namespaces

Desplazar el módulo Notifications al nivel de los demás Bounded Contexts implicará también actualizar los namespaces del directorio y allí donde lo estemos llamando

* Tip ☝️: En la familia de IDEs de JetBrains podemos llevar a cabo el cambio de namespaces y la migración de directorios creando un fichero en la raiz del módulo y cambiando el namespace desde el menú de refactoring
