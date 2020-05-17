# Qué es la Arquitectura de Software

* No es la arquitectura de Hardware (O arquitectura de sistemas)
* Reglas autoimpuestas para definir como se diseña el software.
* Por ejemplo: Un componentes de dominio no puede atacar a la arquitectura, esto lo tiene que hacer un componente de arquitectura.
* Ejemplos de arquitecturas: MVC, DDD, Hexagonal
* Hay patrones tacticos: Repository, ValueObject, etc.
* Macro vs micro design
  * Micro: clases, etc. (como se relacionan las clases entre si)
  * Macro: se lanza un evento, alguien lo captura, etc.
* Beneficios arquitectura software:
  * Mantenibilidad
    * Se evita el crecimiento de la complejidad accidental
    * Complejidad: = Esencial + Accidental
    * A medida que pasa el tiempo, la complejidad de nuestro sistema aumenta. Pero además, esta la accidental, que involuntariamente se añade sobre la que ya hay (esencial). 
  * Cambiabilidad
    * Por ejemplo: Sustituir un componente por otro (MySQLVideoRepository a RedisVideoRepository). Utilizando interfaces.
  * Testing
    * Relacionado con lo anterior, si queremos hacer tests y atacamos sobre una BBDD, podriamos tener un componente que ataque a memoria para que los tests vayan rapidos (o utilizar mocks)
  * Simplicidad
    * Utilizando patrones de arquitectura aparece como una [simetria](https://twitter.com/gonedark/status/936275444420268032) en el codigo (es decir son parecidos) y por lo tanto mas faciles de entender y extender.
* Links:
  * [Macro vs micro design](https://codurance.com/2015/05/12/does-tdd-lead-to-good-design/)
  * [Debate acerca de la terminologia de "Arquitectura"](https://twitter.com/mathiasverraes/status/939096131744817153)
  * [Complejidad accidental vs complejidad esencial](https://en.wikipedia.org/wiki/No_Silver_Bullet)
  
## Test
¿A qué nivel afecta la Arquitectura de Software?
- [ ] Macro design
- [ ] Micro design
- [x] Macro y micro design
