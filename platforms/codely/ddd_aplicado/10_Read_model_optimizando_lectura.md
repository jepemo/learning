# Read Model: Optimizando para la lectura

## Comunicar modules y Bounded Contexts: Query Bus vs Eventos

* En el ejemplo anterior, nos comunicabamos con otro modulo con el querybus
  * Pero no siempre nos puede interesar comunicarse de esa forma
* El ejemplo que utilizan sigue la siguiente estructura: Lesson -> Step -> Duration
  * Se quiere saber la duracion estimada de una lesson
* Tienen dos servicios

```
--> GET /lessons/x --> [ Lessons Module]           [Steps Module] <-- PUT /steps/x --
                              |                         |
                              |                         |
                              v                         v
                           [BBDD]                    [BBDD]
```

* Una forma de comunicar los BC es que Lessons Module llame a StepsModule con una Query
  * FindStepsQuery
  * Inconvenientes 👎
    * Estamos generando acoplamiento entre módulos
    * Tendremos problemas de rendimiento si debemos estar realizando múltiples queries cada vez que queramos recuperar los detalles de una Lección
    * Podemos acabar con un caso de uso enorme en el que encontremos un montón de queries
    * Necesidad de añadir un campo duration a Lesson como nullable o añadirlo en la response aunque no exista en el agregado
* Otra forma seria lanzar un evento de dominio de "step_created"
  * Lessons module estaria suscrito y actualizaria su proyeccion
  * Es decir, su campo de "estimated_duration".
  * Para evitar problemas de calcular la duracion con la informacion del evento.
    * Al recibir el evento podria hacer una query para recoger el "Step" y consultar su duracion
    
## Nueva feature: Horas totales de un curso

### Nueva feature: Horas totales de una lección

```php
final class VideoStep extends Step
{
    private $videoUrl;
    private $text;
    public function __construct(
        StepId $id,
        LessonId $lessonId,
        StepTitle $title,
        StepEstimatedDuration $estimatedDuration,
        StepOrder $order,
        DateTimeImmutable $creationDate,
        VideoUrl $videoUrl,
        VideoStepText $text
    ) {
        parent::__construct($id, $lessonId, $title, $estimatedDuration, $order, $creationDate);
        $this->videoUrl = $videoUrl;
        $this->text     = $text;
    }
    public static function create(
        StepId $id,
        LessonId $lessonId,
        StepTitle $title,
        StepEstimatedDuration $estimatedDuration,
        StepOrder $order,
        VideoUrl $videoUrl,
        VideoStepText $text
    ): self {
        $step = new self($id, $lessonId, $title, $estimatedDuration, $order, new DateTimeImmutable(), $videoUrl, $text);
        $step->record(
            new VideoStepCreatedDomainEvent(
                $id->value(),
                [
                    'lessonId'          => $lessonId->value(),
                    'title'             => $title->value(),
                    'estimatedDuration' => $estimatedDuration->value(),
                    'creationDate'      => date_to_string($step->creationDate()),
                    'url'               => $videoUrl->value(),
                    'text'              => $text->value(),
                ]
            )
        );
        return $step;
    }
    public function points(): StepPoints
    {
        return new StepPoints(100);
    }
    public function videoUrl(): VideoUrl
    {
        return $this->videoUrl;
    }
    public function text(): VideoStepText
    {
        return $this->text;
    }
}
```

* Clase Step:

```php
abstract class Step extends AggregateRoot
{
    private $id;
    private $lessonId;
    private $title;
    private $estimatedDuration;
    private $order;
    private $creationDate;
    public function __construct(
        StepId $id,
        LessonId $lessonId,
        StepTitle $title,
        StepEstimatedDuration $estimatedDuration,
        StepOrder $order,
        DateTimeImmutable $creationDate
    ) {
        $this->id                = $id;
        $this->lessonId          = $lessonId;
        $this->title             = $title;
        $this->estimatedDuration = $estimatedDuration;
        $this->order             = $order;
        $this->creationDate      = $creationDate;
    }
    public function id(): StepId
    {
        return $this->id;
    }
    public function lessonId(): LessonId
    {
        return $this->lessonId;
    }
    public function title(): StepTitle
    {
        return $this->title;
    }
    public function estimatedDuration(): StepEstimatedDuration
    {
        return $this->estimatedDuration;
    }
    abstract public function points(): StepPoints;
    public function order(): StepOrder
    {
        return $this->order;
    }
    public function creationDate(): DateTimeImmutable
    {
        return $this->creationDate;
    }
}
```

* Clase RecalculateLessonEstimatedDurationOnStepCreated:

```php
final class RecalculateLessonEstimatedDurationOnStepCreated implements DomainEventSubscriber
{
    private $recalculator;
    public function __construct(LessonEstimatedDurationRecalculator $recalculator)
    {
        $this->recalculator = $recalculator;
    }
    public static function subscribedTo(): array
    {
        return [
            ChallengeStepCreatedDomainEvent::class,
            QuizStepCreatedDomainEvent::class,
            VideoStepCreatedDomainEvent::class,
        ];
    }
    public function __invoke(StepCreatedDomainEvent $event)
    {
        $id = new LessonId($event->lessonId());
        apply($this->recalculator, [$id]);
    }
}
```

* Clase LessonEstimatedDurationRecalculator:

```php
final class LessonEstimatedDurationRecalculator
{
    private $bus;
    private $finder;
    private $repository;
    private $publisher;
    public function __construct(QueryBus $bus, LessonRepository $repository, DomainEventPublisher $publisher)
    {
        $this->bus        = $bus;
        $this->finder     = new LessonFinder($repository);
        $this->repository = $repository;
        $this->publisher  = $publisher;
    }
    public function __invoke(LessonId $id)
    {
        $lesson                        = $this->finder->find($id);
        $recalculatedEstimatedDuration = new LessonEstimatedDuration($this->sumStepsEstimatedDurationFor($id));
        $lesson->recalculateEstimatedDuration($recalculatedEstimatedDuration);
        $this->repository->save($lesson);
        $this->publisher->publish(...$lesson->pullDomainEvents());
    }
    private function sumStepsEstimatedDurationFor(LessonId $id): int
    {
        $steps = $this->askForSteps($id);
        return reduce($this->durationAdder(), $steps, 0);
    }
    private function askForSteps(LessonId $id): StepsResponse
    {
        $query = new SearchStepsByLessonQuery($id->value());
        return $this->bus->ask($query);
    }
    private function durationAdder(): callable
    {
        return static function (int $totalDuration, StepResponse $step): int {
            return $totalDuration + $step->estimatedDuration();
        };
    }
}
```

* Clase Lesson:

```php
final class Lesson extends AggregateRoot
{
    // ...

    public function recalculateEstimatedDuration(LessonEstimatedDuration $recalculatedEstimatedDuration): void
    {
        $this->estimatedDuration = $recalculatedEstimatedDuration;
        $this->record(
            new LessonEstimatedDurationRecalculatedDomainEvent(
                $this->id()->value(),
                [
                    'courseId'             => $this->courseId()->value(),
                    'newEstimatedDuration' => $recalculatedEstimatedDuration->value(),
                ]
            )
        );
    }
}
```
