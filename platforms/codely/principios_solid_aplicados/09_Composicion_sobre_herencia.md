# Composición sobre herencia

Por ejemplo, para el ejemplo de siempre:

```php
final class VideoCreator
{
    private $repository;
    private $publisher;
    public function __construct(VideoRepository $repository, DomainEventPublisher $publisher)
    {
        $this->repository = $repository;
        $this->publisher  = $publisher;
    }
    public function create(VideoId $id, VideoType $type, VideoTitle $title, VideoUrl $url, CourseId $courseId): void
    {
        $video = Video::create($id, $type, $title, $url, $courseId);
        $this->repository->save($video);
        $this->publisher->publish(...$video->pullDomainEvents());
    }
}
```

* La clase "VideoCreator" se compone de Videorepository y DomainEventPublisher.
* Es decir, utilizamos los comportamientos de "VideoRepository" y "DomainEventPublisher" en vez de heredarlos.
* La herencia da problemas porque es dificil generalizar para todos los hijos: acabas metiendo flags, etc. (Y se complica)
* Así solo componemos donde realmente lo necesitamos. Por herencia siempre lo tienes todo (uses o no lo uses).
* La herencia es mas complicado de testear.
* Utilizar la herencia solamente para los modelos que lo necesiten.
* Si el lenguaje lo permite, marcar las clases como "final" para que no puedan heredar.
