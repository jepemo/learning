# Health check de la aplicación: Nuestro primer endpoint

## Crear Endpoint de health check

* Health Check: Consiste simplemente en un punto de entrada en nuestra aplicación que nos confirme que esta se está ejecutando en el servidor. Este tipo de controladores son utilizados habitualmente por los Load Balancer para comprobar periódicamente si el servidor está bien o por el contrario debe echarlo abajo y levantar uno nuevo.
  * No va a probar la conexión de BBDD. Normalmente esto lo haria el endpoing del "StatusPage", ademas de otros subsistemas.
  * En este caso solo queremos ver que la aplicacion se ha levantado bien.
* En el ejemplo de Java explican las anotaciones de "SpringBootApplication" que dice que es una aplifacion "SpringBoot" :D y "@ComponenteScan" para hacer el autowired de los componentes.

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
