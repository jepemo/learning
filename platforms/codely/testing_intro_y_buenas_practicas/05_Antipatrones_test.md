# Anti-patrones de test

## Cómo solucionar tests que fallan aleatoriamente

* Tests que a veces fallan y otras veces no
* En una pipeline (serie de pasos) de CI
* Normalmente son tests que dependen del orden en el que se ejecutan
  * Por ejemplo, en un test se inserta un registro de BBDD y en otro se recupera dicho registro
  * Una solucion seria limpiar todo antes de cada test y que en cada test se inserte(o lo que sea) que se tenga que utilizar
  
### Aleatoriedad en los tests

* Normalmente las suites (conjuntos de test) se ejecutan en paralelo, pero los de dentro de cada una no. Pero se puede forzar segun el framework
* En PHP-Unit: hay un parametro "random-order/order-by"
* En Java + jUnit: Este ya lo hace de forma aleatorio, pero luego ya sigue siempre el mismo orden. Pero existe una anotación "@TestMethodOrder" que permite decir que sea aleatorio.
* En Scala + ScalaTest: Anyadir el trait "RandomTestOrder"
* En Javascipt/Jest: Ya lo hace por defecto

## Como forzar tests deterministas

* Para hacer que pasen correctamente aquellos que tienen condiciones más peculiares y evitar que los errores puedan enmascararse por cómo hayamos definido los valores.
* Ejemplos:
  * Un ejemplo típico que suele ser fuente de problemas es tener nuestras urls de producción definidas en constantes, ya que puede derivar en que cuando cambiemos el valor de estas constantes, a pesar de estar pasando el test, nos encontremos con que falla en producción (tendríamos que cambiar los tests y los propios consumidores de la api). Lo apropiado en estos casos es forzarnos a hacer explícito cualquier cambio que tenga implicaciones sobre los clientes
  * Otro caso recurrente es cuando trabajamos con fechas, es decir, aquella lógica de negocio en la cual se siga un determinado flujo o incluso se genere un error en base al día/hora en que se ejecute (Ej. premios que se envían en un juego sólo por la mañana o descuentos que se aplican cada Viernes)
  * Codigo (comprueba si es de dia, el mirara la hora del servidor):
  
 ```php
 //...
public function check(): bool
{
    $currentHour = (new DateTimeInmutable())->format('H');

    return $currentHour >= self::MORNING_START_AT 
			&& $currentHour <= self::MORNING_END_AT;
}

/** @Test*/
public function it_should_return_true_when_its_morning()
{
      $checker = new MorningChecker();

      $this->assertTrue($checker->check());
}
 ```
 
 * Habria que sacar el estado fuera del codigo (**el tiempo es estado, no un primitivo**):
 
 ```php
 interface Clock 
{
    public function now(): DateTimeInmutable
}

final class MorningChecker
{
  //...
  public function __construct(Clock $clock)
  {
    $this->clock = $clock;
  }
  public function check(): bool
  {
      $currentHour = ($this->clock->now())->format('H');

      return $currentHour >= self::MORNING_START_AT 
				&& $currentHour <= self::MORNING_END_AT;
  }
  
  
  // y el Test
  
  /** @Test*/
public function it_should_return_true_when_its_morning()
{
      $clock = Mockery::mock(Clock::class);

      $clock->shouldReceive('now')
      ->once()
      ->andReturn(new DateTimeInmutable('2019-05-20 09:00:00'));

      $checker = new MorningChecker($clock);

      $this->assertTrue($checker->check());
      
      Mockery::close();
}
 ```
 
 * Esta interface nos va a permitir que en tiempo de test podamos mockear el valor que retornará la llamada al método now(), de tal modo que será posible emular que la llamada al checker se hace por la mañana o por la tarde en función de lo que queramos validar.
 * Cabe decir que lo ideal en este tipo de pruebas es generar una hora aleatoria dentro del rango que nos interese y así obtener poder cubrir todo el abanico de opciones en el mismo test case
 
