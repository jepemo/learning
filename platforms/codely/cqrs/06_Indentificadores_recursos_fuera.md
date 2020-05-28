# Identificadores de recursos desde fuera

## Read

* Clasicamente el ID del recurso se crearia en la BBDD (id de la tabla).
* Problemas:
  * MySql devuelve el ID y se rellena en la entidad y esta se pasa al cliente para poder identificar-lo en el futuro
  * El problema es que se crea en la Infraestructura
    * El problema es que si se cambia el componente de la infraestructura ya no genera los ids de la misma forma.
  * Además el bus no devuelve nada en un command. 
    * Como se haria para devolver al cliente el ID?
    * El cliente tiene un estado de inconsistencia con la entidad en la que temporamente no tiene ID
  * Complejidad adicional en testing. (no tengo los ids) tendria que mockear la BBDD?
  * Si se genera el ID en el "caso de uso", ya no tendriamos el problema de la generacion en la BBDD y no tendira problema en cambiar la infraestructura.
    * Pero aun tengo el problema de devolverlo por el bus?
    * El cliente tampoco tiene el id
    * Tambien problemas con testing
* La idea seria generar el ID desde el Cliente:
  * Se trata el id como un atributo mas
  * El command no tiene que devolver nada, etc.
  * etc.
  
  
