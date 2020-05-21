# Testing capa de infraestructura

# Teoria
* Nos permiten comprobar de forma aislada que las distintas implementaciones a nivel de infraestructura (adapters) funcionan como se espera.
* Estos tests, obviamente, tendran detalles de la tecnologia que se esta probando. Por ejemplo, volcado de caches, etc.
* Incluso los de notificaciones, deberiamos comprobar que el mensaje que se ha enviado, ha llegado y tiene el contenido que hemos enviado.
* Ejemplo:
```php
final class VideoRepositoryTest extends VideoModuleFunctionalTestCase
{
    /** @test */
    public function it_should_save_a_video()
    {
        $this->repository()->save(VideoStub::random());
    }

    /** @test */
    public function it_should_find_an_existing_video()
    {
        $video = VideoStub::random();

        $this->repository()->save($video);
        $this->clearUnitOfWork(); // ℹ️ Importante limpiar la Unit Of Work para evitar que al hacer el search quien nos devuelva el vídeo sea el ORM en base a lo que tiene ya en memória debido a haberlo guardado.

        $this->assertSimilar($video, $this->repository()->search($video->id()));
    }

    /** @test */
    public function it_should_not_find_a_non_existing_video()
    {
        $this->assertNull($this->repository()->search(VideoIdStub::random()));
    }

    // ℹ️ Nótese que a la hora de obtener la implementación a ejecutar del repositorio lo hacemos en base al contenedor de dependencias de producción.
    // Es decir, estamos atacando a la implementación del repositorio que usamos en producción.
    private function repository(): VideoRepository
    {
        return $this->service('codely.video.video.repository');
    }
}
```

## Test
¿Usaremos algún tipo de doble de test para evitar ir a la tabla de base de datos y que nuestros test de integración sean lentos?
- [ ] Sí, usaremos mocks para falsear la interface y así evitar ese gasto de tiempo de acceder a BD
- [x] No, en el caso de los test de integración es justamente lo que nos interesa testear
