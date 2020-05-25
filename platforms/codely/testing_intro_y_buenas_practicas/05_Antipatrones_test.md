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
