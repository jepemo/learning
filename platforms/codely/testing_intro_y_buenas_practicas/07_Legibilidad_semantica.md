# Aportando legibilidad y semántica a nuestros tests

## Aportando legibilidad y semántica a nuestros tests

* Como simplificar mas aun nuestros tests.
* Ejemplo:

```php
public function it_should_find_an_existing_video(): void
{
    // Given
    $video = $this->givenARandomVideo(); // VideoMother::random();

    // When
    $actualResponse = $this->whenFinderIsInvoked($video);
    
    // Then: Este es el que crea el mock
    $this->thenTheResponseShouldBeTheExpected($video, $actualResponse);
}
```

* Se ha extraido a funciones, lo que estabamos haciendo en el test: creacion del video, mock, etc.
* En vez de instanciar el $video para el test (que el metodo refactorizado devuelva el video). Se podria inicializar uno para la clase. Esto podria ser beneficioso si hay muchos colaboradores. Sino se tendria que pasar por parametro para cada uno.
* Esta segunda forma, podria ser lo que vaya en el setup (explicito), o en si mismo es como un setup, lo veo en el test.
* En muchos casos (casi todos?) no es necesario refactorizar en metodos, porque si son muy simples empeora la legibilidad.

## Test

Encapsular la lógica de cada 'bloque' siguiendo el patrón Given-When-Then nos permite...
- [x] Reducir ruído en los tests
- [ ] Reducir el número de tests a ejecutar

(Al simplificar aún más la estructura de nuestros tests, conseguimos reducir al máximo el ruido y ganar aún más en legibilidad)
