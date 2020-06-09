# Eventos de dominio

## Cómo y por qué desacoplar entre módulos y Bounded Contexts

* Flujo de peticion:

``` 
                                        -> VideoFinder
  -> VideoPutController -> VideoCreator -> Video
                                        -> VideoRepository <--- InMemoryVideoRepository
```

* VideoCreator (ApplicationService)
  * Guarda en BBDD
  * En un futuro podria ser:
    * Incrementar contador
    * Notificar subs
    * Email confirmacion
    * etc.
* En definitiva cada vez más acciones derivadas del hecho de crear un video, asumiendo más responsabilidades y rompiendo con el principio SRP de SOLID
* La solucion seria utilizar los **eventos de dominio**
  * lo que hará será publicar un evento de dominio en el exchange al que podrán subscribirse otros módulos independientes y realizar las las acciones pertinentes cada vez que lo reciban
* Gracias a este flujo, si queremos añadir nuevas acciones derivadas de crear un nuevo vídeo, lo único que tendremos que hacer será añadir una nueva cola conectada al exchange sin necesidad de modificar el código existente
* Como ya hemos comentado, aunque ahora nos encontremos con mayor número de clases en nuestra aplicación, estamos ganando en independencia de los distintos equipos de trabajo que puedan estar implicados. Por otro lado, una vez que nuestro caso de uso realiza un único cometido, la respuesta será mucho más rápida y mejoraremos en términos de rendimiento

## Refactoring del caso de uso añadiendo publicación de eventos

* Caso de uso de cuando se publica un video: Clase VideoPublisher:

```java
public final class VideoPublisher{

    private final Eventbus eventBus;

    public VideoPublisher(EventBus eventBus) {
        
        this.eventBus = eventBus;
    
    }

    public void publish(String rawTitle, String rawDescription) {
        
        final var title = new VideoTitle(rawTitle);
        final var description = new VideoDescription(rawDescription);

        final var video = Video.publish(title, description);

        eventBus.publish(video.pullDomainEvents());
    }
}
```

* Fijaos que el método se llama pullDomainEvents, y esto es así con toda la intencionalidad semántica, ya que en el cuerpo del método estaremos vaciando la lista de eventos que tiene la clase. De este modo, nos aseguramos de que si dentro del caso de uso seguimos realizando acciones con esa clase y volvemos a publicar eventos, no se repitan aquellos que ya se habían procesado antes

* Clase Video:

```java
public final class Video {
    
    private VideoTitle title;
    private VideoDescription description;

    private Video(VideoTitle title, VideoDescription description) {
    
        this.title = title;
        this.description = description;
    
    }

    public static Video publish(VideoTitle title, VideoDescription description) extends AggregateRoot {
        var video = new Video(title, description);

        var videoCreated = new VideoPublished(title.value(), description.value());

        video.record(videoCreated);

        return video;
    }
}

* El Agregate root es:

```java
public abstract class AggregateRoot {
    private List<DomainEvent> recordedDomainEvents = new LinkedList<>();

    final public List<DomainEvent> pullDomainEvents() {
        final var recordedDomainEvents = this.recordedDomainEvents;
        this.recordedDomainEvents = new LinkedList<>();

        return recordedDomainEvents;
    }

    final protected void record(DomainEvent event) {
        recordedDomainEvents.add(event);
    }
}
```

* Tal como hemos visto, es el caso de uso tendrá las implicaciones de la atomicidad en términos de transaccionabilidad de BD y publicaciones de eventos, pero serán los eventos que recoja del Aggregate Root, por lo que será el agregado el responsable de generar los eventos
  * El agregado no es quien publica el evento, sino que lo va a generar y registrar guardándoselo dentro
* Lo que nos va a permitir AggregateRoot es dotar a nuestras clases de la capacidad de registrar eventos. Así podremos desde el Application Service publicarlos a través de un publicador

Y el evento (Se trata de una acción que se ha realizado, lo cual se traduce en una mutación de estado en nuestro sistema):

```java
public final class VideoPublished implements DomainEvent {
    private static final String FULL_QUALIFIED_EVENT_NAME = "codelytv.video.video.event.1.video.published";

    private final String title;
    private final String description;

    public VideoPublished(String title, String description) {
        this.title = title;
        this.description = description;
    }

    public String fullQualifiedEventName() {
      return FULL_QUALIFIED_EVENT_NAME;
    }

    public String title() {
        return title;
    }

    public String description() {
        return description;
    }
}
```

* VideoPublished no deja ser un modelo, implementando la interface DomainEvent que nos obligará a implementar el método fullQualifiedEventName para devolver el nombre del evento
* El hecho de que los atributos del evento de dominio se definan como escalares nos va a permitir por una parte que esté desacoplado de contextos o módulos, y por otra que sean fácilmente serializables


