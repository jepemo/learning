# Health check de la aplicación: Nuestro primer endpoint

## Crear Endpoint de health check

* Health Check: Consiste simplemente en un punto de entrada en nuestra aplicación que nos confirme que esta se está ejecutando en el servidor. Este tipo de controladores son utilizados habitualmente por los Load Balancer para comprobar periódicamente si el servidor está bien o por el contrario debe echarlo abajo y levantar uno nuevo.
  * No va a probar la conexión de BBDD. Normalmente esto lo haria el endpoing del "StatusPage", ademas de otros subsistemas.
  * En este caso solo queremos ver que la aplicacion se ha levantado bien.
* En el ejemplo de Java explican las anotaciones de "SpringBootApplication" que dice que es una aplifacion "SpringBoot" :D y "@ComponenteScan" para hacer el autowired de los componentes.
* Siguiendo un cierto razonamiento en cuanto a lo que queremos hacer, podemos llegar a la conclusión de que pretendemos crear un punto de entrada a través del cual se pueda verificar mediante una llamada HTTP que la aplicación está correctamente levantada. Esto se traducirá en que dentro de la carpeta ‘controller’ de nuestra aplicación (tendremos una carpeta por cada protocolo de comunicación que introduzcamos) crearemos otra para ‘health_check’ y, dentro de esta, la clase HealthCheckGetController que tal y como vimos en el curso de DDD aplicado queremos que se acople en el naming al protocolo de comunicación utilizado
* En "apps/main/tv.codely.apps/mooc/controller/health_check/HealCheckGetController.java"
* Codigo:

```java
@RestController
public final class HealthCheckGetController {

    @GetMapping("/health-check")
    public HashMap<String, String> handle() {
        HashMap<String, String> status = new HashMap<>();
        status.put("status", "ok");

        return status;
    }

}
```

* Lo primero que encontramos en esta clase es la anotación ‘RestController’ que nos permitirá que sea identificada como un controlador por SpringBoot. Además añadimos la ruta de entrada con la anotación ‘GetMapping’ y lanzamos un HashMap como respuesta indicando que todo está OK 👌(El propio SpringBoot lo serializará a Json mágicamente)

* El hecho de hacer explícito el verbo Http en el nombre de la clase y limitar el número de métodos de entrada subyace a la intención de acotar el acoplamiento lo máximo posible en la clase

## Añadir tests de aceptación con Spring Boot Runner

* Tipos de test de arquitectura hexagonal

```    
                                            -> Services (D)
-> Controller (I) -> Application Service(A) -> Models (D)
                                            -> Repos (D)
                                                     ^------------------ Implementation (I)
                   <- Unit Test -----------------------> <- Integration test ------------>                                               
< ------------ Aceptance test ------------------------------------------------------------->
```
* **Unit Test**: Comienzan en nuestro Caso de uso (Entendiendo cada Caso de uso como una ‘unidad’) y validarán precisamente la lógica que hay dentro de este con independencia del número de puntos de entrada existentes y sin alcanzar la implementación de la infraestructura
* **Integration Test**: Se encargan de validar nuestra Infraestructura (Acceso a BD, Conexiones a colaboradores externos…)
* **Acceptance Test**: Implica todo el flujo de la petición, incluyendo el propio punto de entrada (controladores, comandos…)
* Codigo:

```java
final class HealthCheckGetControllerShould extends RequestTestCase {
    @Test
    void check_health_check_is_working_ok() throws Exception {
        assertResponse("/health-check", 200, "{'application':'mooc_backend','status':'ok'}");
    }
}
```

* Lo primero que observamos en el test es que estamos heredando de RequestTestCase (en el repo podéis encontrarla como MoocApplicationTestCase), que se trata de una clase custom propia en la que tenemos toda la magia de Spring necesaria para simular una Request Http (Así dejamos encapsulado todo el acoplamiento en Infraestructura dejando limpio nuestro dominio)
  * Ojo 👀, en este caso no nos compensa realmente hacer uso de la composición sobre la herencia, ya que no vamos a tener un punto donde introducirnos y falsear una implementación (como vimos con SOLID)
  * Tiene implementados unos helpers para reutilizar en todos los tests
* Finalmente, dentro del TestCase lo que haremos será simplemente hacer uso de nuestro método helper assertResponse() con el que simularemos una petición a la ruta especificada, pasándole además el StatusCode y la Response esperada
  * 🐢Este tipo de tests requieren levantar por detrás toda la infraestructura necesaria, por lo que, aunque los tests en si mismos corran raudos y veloces 🐇, siempre tendrán una demora de tiempo para esa preparación inicial
  
  ## Test
  
 Tener un HealthCheck nos permite comprobar que todo el sistema funciona correctamente (Acceso a BD, comunicación con el sistema de colas...)
- [ ] ¡Cierto!
- [x] ¡Falso!

(Este tipo de Controller simplemente comprueban que la aplicación se esté ejecutando en el servidor, evaluando si es necesario tirar y volver a levantarlo)

Hacer explícito el protocolo de comunicación y método en el naming de los Controllers nos permite...
- [ ] Que el framework pueda inyectar estas clases automáticamente
- [ + Que la clase no tenga acoplamiento con el framework
- [x] Forzarnos a delimitar el acoplamiento en estas clases

(Esta práctica persigue que el acomplamiento esté lo más acotado posible en nuestros Controllers y forzarnos a limitar las responsabilidades que tendrán cada uno de ellos)

Los tests unitarios de nuestra aplicación abarcan..
- [ ] El caso de uso
- [ ] El controlador
- [x] Ambas son correctas

(Se entiende el caso de uso como la 'unidad', por lo que sólo evaluaremos la lógica de éste con independencia del número de puntos de entrada)
