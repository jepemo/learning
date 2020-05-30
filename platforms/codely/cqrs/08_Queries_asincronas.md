# Queries asíncronas

## Queries asincronas con Scala

* Para evitar bloquear nuestro hilo principal de ejecución mientras se realizan operaciones de entrada y salida a la base de datos. 
* La asincronía responde por tanto una necesidad a nivel de rendimiento.
* Flujo:
  * Peticion WEB /users/x/greet
  * Controlador prepara query
  * Query al querybus
  * Query bus al queryhandler
  * Llama al UserGreeFinder -> consulta User -> UserGreet
    * UserId -> Para devolver el user
    * User -> Para construir el userGreet
    * UserRepository -> InDelayedMemoryUserRepository (Para probar que la query tarda, por lo que es ideal para usar una llamada asincrona)
* Utilizan scala, para que el repositorio devuelve un futuro (en realidad todo el flujo va con futuros)
  * Asi el controlador puede continuar el flujo y no se para.
* Codigo

```scala
package tv.codely.cqrs_ddd_scala_example.acceptance

import java.util.UUID

import scala.reflect.classTag
import scala.concurrent.duration._
import scala.concurrent.ExecutionContext.Implicits.global

import cats.implicits._
import org.joda.time.DateTime
import org.scalatest.concurrent.ScalaFutures
import org.scalatest.Matchers._
import org.scalatest._
import org.scalatest.concurrent.PatienceConfiguration.Timeout
import org.scalatest.time.{Seconds, Span}
import tv.codely.cqrs_ddd_scala_example.bus.domain.QueryBus
import tv.codely.cqrs_ddd_scala_example.user_greet.application.generate.{
  FindUserGreetQuery,
  FindUserGreetQueryHandler,
  UserGreetFinder
}
import tv.codely.cqrs_ddd_scala_example.user_greet.infrastructure.InAsyncDelayedMemoryUserRepository

final class AsyncUserGreetFinderTest extends WordSpec with ScalaFutures with GivenWhenThen {

  "UserGreetGenerator with an AsyncQueryBus" should {
    "not block the execution flow until getting a response from a slow repository" in {

      Given("a UserGreetGenerator with a user repository with a notable delay")

      val notableDelay                  = 10.seconds
      val userRepository                = new InAsyncDelayedMemoryUserRepository(notableDelay)
      val userGreetGeneratorWithDelay   = new UserGreetFinder(userRepository)
      val generateUserGreetQueryHandler = new FindUserGreetQueryHandler(userGreetGeneratorWithDelay)

      And("an AsyncQueryBus which doesn't block the execution flow until getting a response")

      val queryBus = new QueryBus(
        Map(
          classTag[FindUserGreetQuery] -> generateUserGreetQueryHandler
        ))

      When("we ask the GenerateUserGreetQuery to the AsyncQueryBus")

      val query = FindUserGreetQuery(
        UUID.randomUUID(),
        DateTime.now(),
        UUID.fromString("1646fd5c-de2b-435f-b20f-ad1f50924dfe"))

      val futureGreeting = queryBus.ask(query)

      println("Query asked to the async query bus")

      Then("it should say hello to someone")

      futureGreeting.futureValue(Timeout(Span(15, Seconds))).greet
    }
  }
}
```

## Test

El QueryBus asíncrono nos permite…
- [ ] Hacer más de una query en paralelo
- [ ] Hacer múltiples queries secuencialmente
- [ ] No bloquear el hilo principal mientras se ejecutan las queries
- [ ] Hacer una query sin tener una response
- [ ] Todas las anteriores son correctas
- [ ] 1, 2 y 3 son correctas
- [ ] 1, 2 y 4 son correctas
- [x] 1, 3 y 4 son correctas
- [ ] 2, 3 y 4 son correctas
- [ ] 6, 7 y 8 son correctas

Scala nos beneficia respecto a PHP en…
- [ ] Somos más cools
- [x] Gestionar múltiples procesos concurrentes de forma agnóstica al hardware
- [ ] Devolver Promises
