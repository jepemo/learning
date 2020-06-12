# Read Model: Casos comunes en entornos complejos #KeepItReal

## Evitando JOINs denormalizando Read Model

* Como agregar información
* En el ejemplo que presentan, una listado de productos.
  * Se ve que el listado agrega información distinta: Nombre, tipo, descripcion, rating, etc.
  * El objetivo es realizar una busqueda sobre estos campos
  * La aproximacion inicial asumimos que las tablas con las que estamos trabajando están normalizadas al máximo, por lo que para recuperar todos los datos del producto tendremos que lanzar una query con un montón de JOINs a otras tablas como Categoría, Tipo de uva, Procedencia… Por supuesto esto se traduce en un aumento de tiempo para recuperar todos los datos del producto.
* Nuestra propuesta es que ya que la búsqueda a través de cualquier motor de indexación nos devolverá un conjunto de ids, cuando vayamos a realizar la búsqueda en nuestra BD MySQL, la realicemos también a través de dichos ids, de tal modo que en vez de consultar varias tablas, la propia tabla de Productos contenga en una única row los datos serializados en formato json como una única columna
* Con este procedimiento estaremos penalizando el rendimiento en tiempo de escritura, pero el hecho de denormalizar de esta forma el Read Model nos va a garantizar que el tiempo de lectura será mucho menor y en términos de SEO conseguiremos mejores resultados
* Resumen:
  * Si utilizamos un motor de busqueda (elasticsearch, etc) este va a devolver un listado de ids
  * Por lo tanto hacer queries por ids con toda la informacion que vas a mostrar (en una vista materializada).
  * Que se penalizara en tiempo de escritura (ya que tendra que actualizar las vistas) pero como hay mas lecturas estara bien.
  
## Alternativas para agregar información

### Obtener datos del curso y todas las lecciones

* Estas son algunas alternativas que hemos pensado en el caso de necesitar agregar información de las Lecciones dentro del propio caso de uso de recuperar la información de un _Curso. Si tenéis en mente otras alternativas nos encantaría que las compartierais con nosotros en una nueva discusión al final del post

#### Cliente => N backends

* La primera opción sería que desde el cliente pidiera la información del curso al backend y posteriormente hiciera una o más peticiones para recuperar las lecciones (Un ejemplo de esta alternativa lo tenemos en la carga de videos en YouTube)
* Ventajas
  * Si no quieres cargarlo todo, no tienes que hacerlo
* Inconvenientes
  * Aumenta el número de peticiones
* Este enfoque será fácil de implementar en un frontend con componentes autónomos como en el caso de React o Vue, sin embargo si que puede ser algo enrevesado cuando lo que gestionamos es un frontend generado desde el propio backend

#### Cliente => API Gateway => N Backends

* El patrón API Gateway se define como el ‘Backend for Frontends’ y consiste en situar un sistema ‘delante’ de nuestras APIs, ocupándose de realizar las N peticiones necesarias y mergeándo las responses en una única que es devuelta al frontend. Esta opción nos permite encapsular en el Gateway lógica como la relativa a los headers HTTP o la autenticación de usuarios, con lo que el backend sigue siendo una pieza ‘tonta’ ya que solo tendrá la información mínima necesaria.
* Ventajas:
  * Orquestar las peticiones y unificar la respuesta en el Gateway
  * Encapsular lógica fuera del backend
* Inconvenientes
  * Supone la creación de un stack nuevo
  
#### Cliente => 1 Backend => Application Service => Info agregada por eventos

* Tal como hemos visto anteriormente, una tercera alternativa es que el cliente realice una petición a un solo Backend, donde el Application Service ya tendría toda la información agregada a través de eventos
* Ventajas
  * Se recoge toda la información realizando una única petición al backend
* Inconvenientes
  * Supone la creación de toda la infraestructura necesaria para la publicación y susbscripción a los eventos (Mayor coste de infraestructura)
  * Controlar la posible generación de eventos duplicados o desordenados
  
#### Cliente => 1 Backend => 1 Controller => N queries

* La cuarta opción que proponemos es que desde el Cliente se realice una petición al backend y desde el Controlador se realicen N queries, mergearlas en el propio controlador y devolver una sola response
* Lanzar las N queries desde el Controlador y no desde el Application Service tiene total intención, ya que evitamos que los Application Services conozcan acerca del resto de módulos, esto se lo dejaremos a la capa mas externa
* Ventajas Se recoge toda la información realizando una única petición al backend
* Inconvenientes: Dependiendo del tipo de rendimiento que necesitemos puede no ser la mejor opción

