# Testing capa de aplicación y dominio

## Teoria

* Existen diferentes tipos de test: aceptación, unitarios, integración
* Testeamos la capa de aplicación e indirectamente se probara la de dominio
* Test aceptacion:
  * Simulan ser un cliente de nuestra aplicación. Entrarán en juego todas las implementaciones reales para comprobar que todo el flujo y la integración con la infraestructura se producen satisfactoriamente. Con lo cuál, las características principales serían:
  * El objetivo de estos tests es el de asegurar que la aplicación funciona correctamente y el flujo completo de las peticiones se puede realizar satisfactoriamente.
  * Son los test más lentos de ejecutar ya que tienen un alcance mayor y sí ejecutan operaciones de entrada/salida como inserts en base de datos ya que usan las implementaciones reales de estos componentes.
  * Aportan mayor valor debido al alcance que tienen (nos asegura que absolutamente todo está ejecutandose como esperamos)
  * En nuestro caso, al implementar una API HTTP, simularemos peticiones HTTP y comprobaremos que las respuestas tienen el código HTTP y el contenido del cuerpo esperados.
  * Al ser los test más lentos de ejecutar, sólo implementaremos una pequeña muestra de las distintas ramificaciones que pueden tomar nuestros casos de uso. Dejando para los test unitarios la responsabilidad de probar cada una de las casuísticas. Así evitaremos incurrir en el anti-patrón de test del cono de helado.
* Test unitario
  * Los test unitarios son los que usaremos para comprobar que la lógica de negocio de nuestros casos de uso (capa de aplicación) y modelos o servicios de dominio se comportan como esperamos. Características principales:
  * El objetivo de estos tests es el de validar que la implementación de nuestra lógica de negocio es correcta.
  * Son los test más rápidos de ejecutar. En estos tests falsearemos la implementación a usar de todo componente de infraestructura. Es decir, allá donde definamos un puerto en nuestros casos de uso, inyectaremos un doble de test para que no hagan operaciones de entrada/salida pero poder validar la interacción del dominio con estos componentes. Importante falsear la interface de dominio y no el cliente final para evitar incurrir en el anti-patrón de Infrastructure Mocking.
  * El test unitario será independiente del punto de entrada. Desde el momento en el que encapsulamos nuestros casos de uso en servicios de aplicación para poderlos reaprovechar desde múltiples puntos de entrada (controlador API HTTP o CLI), el test unitario invocará directamente al caso de uso para desacoplarse también del controlador.
  * Al ser los más rápidos de ejecutar y estar centrados en la lógica de negocio, es en estos test donde ubicamos las comprobaciones más exhaustivas en cuanto a las distintas ramificaciones de nuestros casos de uso.
  * Ejemplo:
  
```scala
  final class VideoCreatorShould extends UnitTestCase with MockFactory {

  // ℹ️ Falseamos las dependencias de infraestructura (adapters) creando un doble de test de la interface de dominio (ports)
  private val repository: VideoRepository = mock[VideoRepository]
  private val messagePublisher: MessagePublisher = mock[MessagePublisher]

  // ℹ️ Instanciamos el caso de uso inyectando las dependencias falseadas
  private val creator = new VideoCreator(repository, messagePublisher)

  "create a video" in {
    val video        = VideoStub.random
    val videoCreated = VideoCreatedStub(video)

    // ℹ️ Definimos la comprobación de que el caso de uso interacciona con el repositorio guardando nuestro vídeo
    repositoryShouldSave(video)

    // ℹ️ Definimos la comprobación de que el caso de uso interacciona con el publicador de eventos publicando el evento de vídeo creado
    publisherShouldPublish(videoCreated)

    // ℹ️ Invocamos al caso de uso directamente sin pasar por la capa del controlador y esperamos que se ejecute satisfactoriamente y con las interacciones previamente definidas
    creator.create(video.id, video.title, video.duration, video.category).shouldBe(())
  }

  private def repositoryShouldSave(video: Video): Unit =
    (repository.save _)
      .expects(video)
      .returning(Future.unit)

  private def publisherShouldPublish(message: Message): Unit =
    (messagePublisher.publish _)
      .expects(message)
      .returning(())
}
```

* Test de integración
  * Tipo de test unitario donde el objeto de test es alguna implementación de uno de nuestros puertos.
  * Por ejemplo, en el caso del test unitario, habríamos falseado mediante un doble de test la interface de dominio UserRepository, mientras que en el test de integración lo que haremos será justamente testear la implementación de MySqlUserRepository para validar que se comporta como esperamos.
  
 ## Test
 
 Si la conexión a la base de datos la tenemos mal configurada y la contraseña no es correcta, ¿qué tests petarían?
- [ ] Test de aceptación
- [ ] Test unitario
- [ ] Test de integración
- [ ] Test de aceptación y Test unitario
- [x] Test de aceptación y Test de integración
- [ ] Test de aceptación, Test unitario y Test de integración

Hemos explicado que creamos un doble de test a partir del contrato de dominio UserRepository. No obstante, podríamos crearlo a partir de la conexión a MySQL que se le inyecta a MySqlUserRepository (MySqlClient). ¿Por qué no lo hacemos?
- [ ] Porque no lo pone en el libro de Software Craftsmanship ni de Implementing Domain Driven Design
- [x] A nivel de arquitectura hemos definido que queremos tener cambiabilidad a partir de la interface de dominio. Es decir, poder cambiar a PostgreSQL sin que el dominio se vea afectado. Desde el momento en el que los test unitarios testean el dominio, si falsearamos a ese nivel tendríamos que cambiar también nuestros tests al cambiar a PostgreSQL, cosa que no pasaría falseando a nivel de interface de dominio.
- [ ] Realmente sería lo ideal, pero no podemos porque MySqlClient no es una interface si no una clase final y no podemos crear dobles de test de ella

Si nos olvidamos de guardar en base de datos cuando nos hacen un POST a /videos/id-nuevo-video, ¿qué test debería petar?
- [ ] Test de aceptación
- [x] Test unitario
- [ ] Test de integración
- [ ] Test de aceptación y Test unitario
- [ ] Test de aceptación y Test de integración
- [ ] Test de aceptación, Test unitario y Test de integración

* Explicación ultima pregunta:

```
El test de integración seguro que no fallaría ya que la integración con base de datos sería correcta, el único problema sería que no se estaría haciendo uso de ella. Con lo cuál, lo podemos descartar sobre seguro.

El test unitario, en caso de estar bien hecho y aquí sí haber especificado que se debe invocar al método save del colaborador VideoRepository, sí fallaría estrepitosamente evidenciando el problema.

El test de aceptación es el único que podríamos dudar dependiendo de las comprobaciones que hagamos a nivel de aceptación. Por ejemplo, en el caso que veíamos en la lección no petaría, ya que la respuesta seguiría siendo un 201 created. No obstante, sí que es cierto que si nuestros test de aceptación comprueban que el registro existe en la base de datos tras haberse ejecutado, también fallaría.

Esto es un tema donde puede haber controversia y preferimos dejarlo a gusto del consumidor, así que estamos completamente abiertos a que nos expliques tus argumentos a favor o en contra en los comentarios de abajo!
```
