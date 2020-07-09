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
