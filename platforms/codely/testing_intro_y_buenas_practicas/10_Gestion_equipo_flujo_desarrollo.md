# Gestión de equipo y flujo de desarrollo

## Convenciones a nivel de equipo: GitHooks

* **No refactorizarás con los tests fallando**: Si se refactoriza el código cuando los tests están fallando no podremos saber si esto ha roto o no el código, por lo que es recomendable esperar a que los tests estén en verde y así tener la garantía de que esta modificación no rompe nada
* **Mantendrás el código de producción y de tests separados**: El hecho de no separar elementos como los ObjectMothers o implementaciones de infraestructura para tests (Ej. InMemoryUserRepository) puede llevarnos a utilizarlos en producción, con todos los fallos que esto puede provocar
* **No commitearás con los tests fallando**: Hacer commits de nuestro código mientras tengamos tests fallando puede llevar a que éste código se acabe mergeando y promocionándose a pesar de estar mal, por lo que debemos poner especial cuidado en no commitear hasta que estén pasando nuestros tests
