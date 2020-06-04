# Cómo migrar de monolito a microservicios

### Solucion 1: Fallback por HTTP/BD para importacion progresiva

* Sin migrar los datos del viejo sistema al nuevo.
* Pasos:
  * Ponemos como frontal el nuevo microservicio
  * El microservicio consulta su BBDD para recuperar el dato
  * Si el dato no esta, llama al viejo sistema para recuperar los datos.
  * El microservicio actualiza su BBDD
  * Devuelve al cliente el resultado
* Es como si hiciera de cache?/proxy del viejo sistema
* Problemas:
  * Los datos se actualizan muy poco a poco
  * La latencia es muy grande
  * Puede afectar al rendimiento si todos atacan al nuevo servicio.
  
### Solucion 2: Importación inicial

* En este caso si que migrar los datos al nuevo servicio
* Pasos:
  * Borramos los eventos de la cola hasta el momento X
  * Desplegamos el microservicio con consumers desactivados, desde el momento X.
    * Los eventos se van encolando en la cola
  * Ejecutamos importacion para migrar datos hasta el momento X.
    * Esto puede tardar, ya que a lo mejor hay que hacer transformaciones de los datos
  * Activamos consumers del nuevo microservicio
    * Importante la idempotencia
    
### Otros tips

* Si el monolito no lanza eventos, podemos añadir triggers en BD
  * Para que lanze los eventos y los consuma el servicio
  * Esto es para no modificar el monolito y añadirle eventos.
* Si lanza eventos, para evitar bucles, podemos poner un flag en la metadata "from_legacy"
  * Ejemplo:
    * Movil -> peticion -> API (legacy) -> SNS (Evento) "from_legacy=true" -> SQS -> (nuevo sistema) -> consumer OK
    * El nuevo sistema, tiene que reenviar el evento a las colas de los nuevos servicios
      * Tambien con el flag "from_legacy=true"
      * Lo que pasa es que es posible que estos no le hagan caso, porque saben que ya se ha procesado.
    * Igual que si la peticion viene a la API de los nuevos servicios, es posible que se tenga que llamar a la API vieja para que tenga el evento y actualice su BBDD.
    
### Recursos

* [Entrevistas Desarrolladores](https://codely.tv/blog/entrevistas/build-stuff-2017/)
