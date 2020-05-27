# Gestión de equipo y flujo de desarrollo

## Convenciones a nivel de equipo: GitHooks

* **No refactorizarás con los tests fallando**: Si se refactoriza el código cuando los tests están fallando no podremos saber si esto ha roto o no el código, por lo que es recomendable esperar a que los tests estén en verde y así tener la garantía de que esta modificación no rompe nada
* **Mantendrás el código de producción y de tests separados**: El hecho de no separar elementos como los ObjectMothers o implementaciones de infraestructura para tests (Ej. InMemoryUserRepository) puede llevarnos a utilizarlos en producción, con todos los fallos que esto puede provocar
* **No commitearás con los tests fallando**: Hacer commits de nuestro código mientras tengamos tests fallando puede llevar a que éste código se acabe mergeando y promocionándose a pesar de estar mal, por lo que debemos poner especial cuidado en no commitear hasta que estén pasando nuestros tests

* Se puden forzar estas condiciones con los "GitHooks".
  * Acciones que se ejecutan antes de hacer un commit o push.
  
## Cómo promovemos el testing en nuestras empresas

* Mostrar la ventajas economicas: 
  * Al garantizar mayor calidad del codigo
  * Riesgo menor de que pueda fallar
* Hay que introducir en el equipo el trabajo de testing y hacerque el equipo 
* Recomendaciones:
  * Practicar y tomar soltura suficiente para que el impacto de aplicar testing sea el menor posible
  * No pedir permiso, asumiendo nosotros mismos que el testing es una responsabilidad nuestra a fin de desarrollar con seguridad y agilidad
  * Evaluar el contexto en el que os encontráis, pues no siempre compensará el esfuerzo de hacer testing
  
## Test

* Es recomendable hacer refactor cuando los tests fallen y así agilizar las correcciones
- [ ] Eso es cierto
- [x] Eso es falso

(Si hacemos esto y los tests siguen fallando será muy complicado saber si ese refactor habrá roto algo)

Mantener mezclado el código de producción y de test puede llevarnos a...
- [x] Utilizar implementaciones para tests en el código de producción
- [ ] Que los mocks de la capa de infraestructura no funcionen en los tests
- [ ] Ninguna de las anteriores es correcta

(Tener elementos como las implementaciones de infraestructura para tests mezcladas con las de producción puede llevarnos a la confusión de usarlas en el entorno real, con los errores que esto acarrearía)

