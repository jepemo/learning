# Monorepo vs. Multirepo

## Monorepo 🐒 vs. Multirepo 🐑

* La estructura del codigo/carpetas a la hora de estructurar los bounded contexts.
* Monorepo
  * Todos los BC/Aplicaciones estan en el mismo repositorio
  * Resulta más cómodo a la hora de compartir código y tendremos el código más ‘recogido’
* Multirepo
  * Cada BC(+sus aplicaciones) estan en un repositorio
  * Resulta más sencillo utilizar diferentes lenguajes en cada contexto y que cada uno evolucione mas libremente
* A la hora de tomar la decisión sobre qué diseño seguir, un criterio crítico es ver cual nos ofrece de forma más sencilla los beneficios que estemos buscando, por lo que hay que tener claro los beneficios que estamos buscando:
  * Nuestro código está lo suficientemente desacoplado, en nuestro codigo, como para poder tener ecosistemas diferentes si hace falta
  * Está lo suficientemente cohesionado para que los cambios no impliquen que un cambio o rollback de una parte de nuestro código implique un proceso paralelo en otros puntos de éste
* Con frecuencia se asocia el uso de monorepos a connotaciones negativas derivadas de razones históricas o a malas experiencias en anteriores proyectos que pudieran tener restricciones para su adecuada implementación. 
  * Sin embargo, respetando las ‘reglas del juego’ (convenciones) de un buen uso de este tipo de diseño, no tendremos esa serie de restricciones sobre los monorepos
  
  ## Monorepo en PHP
  
  * 
