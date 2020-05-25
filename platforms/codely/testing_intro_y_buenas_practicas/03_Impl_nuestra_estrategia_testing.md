# Implementando nuestra estrategia de testing

## ¿ Que entendemos como unidad en nuestros tests unitarios? (Subject Under Test - SUT)

* No tiene porque ser una relacion 1-1 con las clases del codigo.
  * Esto hace que los tests sean fragiles. Cualquier codigo que cambie, hara que se rompa el test y habrá que arreglarlo.
* No modificar el test sino ha cambiado la logica de dominio
* Al refactorizar codigo, los tests no deberian cambiar.
* En la arquitectura hexagonal (Infraestructura, Aplicación,  Dominio)
  * Infraestrucura: Codigo que se acopla a librerias externas
  * Aplicación: Caso de uso (de principio a fin) desde el punto de vista de los usuarios
  * Dominio: Logica de negocio.
* Tests para probar la arquitectura hexagonal:
   * Test unitarios: Prueban los casos de uso+dominio
   * Test de integración: Son tambien unitarios pero prueban la integracion con los sistemas externos.
   * Test de aceptación: Prueban todo el flujo de principio a fin. En el caso web, desde el controlador a la BBDD y vuelta atras.
     * Pero es posible que la infraestructura en estos casos este mockeada. Por eso son utiles los tests de integracion.
* En todo caso, dependiendo de la criticidad del componente, sera interesente realizar el test sobre el, este donde este.   
* Ejemplo (prueba del caso de uso):

```scala
final class VideosSearcherShould extends UnitTestCase with VideoRepositoryMock {
  private val searcher = new VideosSearcher(repository)

  "search all existing videos" in {
    val existingVideo        = VideoMother.random
    val anotherExistingVideo = VideoMother.random
    val existingVideos       = Seq(existingVideo, anotherExistingVideo)

    // Le decimos al mock (del repositorio) lo que tiene que devolver
    repositoryShouldFind(existingVideos)

    // lo que se esta probando, es que el metodo all, devuelva los videos del repositorio (en este caso)
    searcher.all().futureValue shouldBe existingVideos
  }
}
```

* En este ejemplo de test unitario, la ‘unidad’ se correspondería con el caso de uso, es decir, vamos a testear la entrada/salida al caso de uso así como la colaboración de las dependencias dentro de éste. Puesto que en él no nos interesa validar la integración con la infraestructura, lo que haremos será mockear la implementación del repositorio
  
## Pirámide de test - Propuesta de estrategia para el día a día

* La piramide relaciona la velocidad de los tests y la cobertura de los tests:

 --> Aceptacion  : Los que tiene mas cobertura (ya que prueban todo el flujo), pero son los mas lentos de ejecutar
 --> Integracion : En medio
 --> Unitarios   : Son los mas rapidos de ejecutar, pero los que tiene mejor cobertura
 
 * Por lo que habria que tener pocos tests de aceptacion, mas de integracion y muchos mas unitarios.
 * Todos los tests particulares, se deberian hacer con los unitarios. Los de aceptación es mas para el happy-path.
 
 ## Test
 
 Asumir una relación 1-1 entre tests y clases suele derivar en...
- [ ] Tests más robustos
- [ ] Una menor cobertura del código
- [x] Ninguna de las anteriores es correcta

(Aunque puedan garantizarnos una mayor cobertura, este tipo de tests son mucho más dependientes de la implementación de cada clase y por ende más frágiles)

Es recomendable mockear la infraestructura en nuestros tests de aceptación si no queremos vernos limitados por posibles respuestas asíncronas de la infraestructura.
- [ ] Eso es correcto
- [x] Eso es falso

(Si bien es cierto que este tipo de tests son mucho más lentos, precisamente su objetivo probar el flujo completo de una petición lo más similar posible al entorno real)
