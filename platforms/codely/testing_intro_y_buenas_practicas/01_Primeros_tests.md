# ¡Al turrón!: Nuestros primeros tests

## Teoría

* Tipos de test:
  * **Unit testing**
  * **Test integración** (pruebas de la infraestructura a nuestro sistema)
  * Mutant testing
  * **Acceptance testing**
  * Black box testing
  * Property-based testing
  * Stress testing
  * Compatibility testing
  * Security testing
  * Load testing
* Ejemplo de test unitario a partir de una Kata (Fizzbuzz):
  * Escribe un programa que pinte una linea de con entrada de numeros de 1 al 100
  * Para multiplos de 3 pinta Fizz
  * Para multiplos de 5 pinta Buzz
  * Para multiplos de 3 y 5 pinta FizzBuzz
  * Ejemplo código (con javascript):  
```javascript
describe('Fizzbuzz should', () => {
  test('return itselfnumber', () => {
    expect(fizzBuzz(1).toBe(1))
  })
})

// Si aplicamos la filosofia de TDD de aplicar el minimo codigo para que funcione:
function fizzBuzz(number) {
  return 1;
}
```
En este caso debe devolver ya "Fizz":
```javascript
test('return Fizz if fivisible by 3', () => {
    expect(fizzBuzz(3).toBe('Fizz'))
  })
```

Modificamos el codigo:
````javascript
function fizzBuzz(number) {
  if(number % 3 === 0) {
    return 'Fizz';
  }
  return 1;
}
```

Siguiendo con la misma filosifia llegamos a:
```javascript
function fizzBuzz(number) {
  if(number % 15 === 0) {
    return 'FizzBuzz';
  }

  if(number % 3 === 0) {
    return 'Fizz';
  }

  if(number % 5 === 0) {
    return 'Buzz';
  }

  return number;
}
```

* SUT (Subject Under Test): Es el conjunto del "Describe" mas los tests que incluyen a ese caso.
