# Flujo de desarrollo: TDD y TCR

## Introducción a TDD

* Primero se desarrolla el test y luego la implementacion
* Flujo:
  * Test falla
  * Minima implentacion para que funcione test
  * Pasa test
  * Refactor
  * Vuelta a empezar
* Se tiende a empezar por infraestructura o detalles, en vez del caso de uso.
  * En general, el desarrollo se debe hacer desde fuera hacia adentro: Primero caso de uso, etc.
* Link interesante: https://github.com/neomatrix369/refactoring-developer-habits
  * [Esquema](https://github.com/neomatrix369/refactoring-developer-habits/blob/master/02-outcome-of-collation/tdd-manifesto/TDDManifesto.png)

## Introducción y ejemplo de TCR

* Test-Commit-Revert
* El flujo seria:
  * Test && commit || revert
  * Lanzo los test, si funcionan se hace el commit
  * Si falla, hago un revert (y pierdo los cambios?)
  * Es un TDD llevado al extermo
  * Para no arriesgarnos a perder el codigo, habria que ir con pequeños pasos (baby steps)
* Por ejemplo, como implementarlo:
  * test && commit || revert
  * Alias:
  
```bash
alias test='./vendor/bin/phpunit tests'
alias commit='git commit -a'
alias revert='git reset --hard'
```

## Test

Los tests pueden servirnos como 'documentacion' de nuestra aplicación
- [ ] Eso es cierto
- [ ] Pero sólo los tests de aceptación
- [ ] Eso es falso

(Al definir los contratos y funcionalidades de nuestra aplicación, los tests pueden constituir en cierto modo una útil documentación de la misma)

Aplicando TCR condicionamos el guardado de nuestro código a que primero pasen los tests
- [x] Correcto
- [ ] Incorrecto

(Siguiendo este enfoque, el resultado de lanzar los tests es lo que determinará que el código se commitee o lo revirtamos hasta el último commit)
