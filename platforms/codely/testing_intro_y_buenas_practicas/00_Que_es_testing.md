# ¿Qué es el testing y qué aporta? ¿Por qué deberíamos testear?

* Hay que testear
* Que es un test:
  * Automatizar un conjuntos de pruebas para que se puede ejecutar de forma automatica
* Test de aceptacion: Comprueba todo el flujo, llamando desde el cliente.
* Pipeline CI
  * Se definen una serie de pasos para desplegar el codigo. Uno de estos pasos sera ejecutar los tests.
  * Si el paso de test no pasa, no debe dejar que se integre en la rama de despliegues.
* Por que?
  * Comprobar que lo hemos hecho funciona
  * Reproducir facilmente casos complejos
  * Evitar bugs
  * Nos permite refactorizar (o añadir nuevas funcionalidades) y comprobar que sigue funcionando
  * Permite automatizar (CI)
  * Se permite explorar funcionalidades, es decir, los casos que nuestra aplicación permite realizar.
