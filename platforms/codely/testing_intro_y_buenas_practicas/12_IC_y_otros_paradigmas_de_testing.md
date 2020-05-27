# Siguientes pasos: Integración Continua y otros paradigmas de testing

## Otros paradigmas de testing: Mutant y property based testing

### Mutant Testing

  * Para el ejemplo:
  
```java
final class Calculator {
  public int sum (Integer a, Integer b) {
      return a + b;
  }
}

// y el test

final class CalculatorShould {
    void sum_two_integer_numbers() {
        final Calculator calculator = new Calculator();
        // El test pasa, pero se nos olvido poner un assert para probar que el resultado sea el correcto.
        calculator.sum(3, 4);
    }
}
```

 * Para ello esta el mutation testing.
 * El mutation testing, aleatoriamente cambiaria el comportamiento para ver si sigue funcionando.
 * En nuestro ejemplo, cambiaria la operacion, y si el test sigue pasando es que algo raro pasa.
 * Si cambia el comportamiento del 30% del codigo y no fallan el 30% de los tests es que algo raro pasa.
 
### Property based-testing

* Comprobar las propiedades de nuestros datos/modelos
* Si la entrada de una funcion es un numero natural, la idea es pasarle varias combinaciones de numeros
  * Sobre todos los corner-cases
* La diferencia con el "data-provider" es que le dices como son las propiedades de las entradas y el te genera los inputs.

## Automatizando la ejecución de test: Integración Continua

* Flujo:
  * Revisar cambios
    * Mediante una Pull-Request o Merge-Request
    * Una vez aprobados los cambios, antes de hacer el merge, es importante que la rama este actualizada con master y los tests sigan pasando.
  * Tests en CI
    * Se define con un YML el proceso de contrudccion y ejecucion de test (o como sea en la plataforma CI que se use)
    * Estos tests son sobre las ramas (sincronizadas con master) que se han revisado anteriormente.
    * Es interesante ver la metrica de cobertura para ver si se ha incrementado (o decrementado)
  * Integración 
    * La rama (feature-branch) se mergea sobre master.
    * Luego se prepara el paquete
    * Aqui ya hay opcion de hacerlo automaticamete o manual el desplegar en produccion.
    * O hacerlo automaticamente en PRE y a PRO manualmente.
    
## Conclusiones y siguientes pasos

* Tipologías de tests y qué capas de nuestro código testear en cada una de ellas
* Pirámide de tests: Velocidad y cobertura de los diferentes tipos de tests
* CI/CD: Papel fundamental de los tests en estos procesos

