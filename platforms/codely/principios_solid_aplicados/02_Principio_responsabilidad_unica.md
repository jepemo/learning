# Principio de Responsabilidad Única
* Una clase debe representar un unico concepto y responsabilidad.
* Solo debe tener una razon para cambiar
* Clases de servicios pequeñas con objetivos acotados
* Servicios:
  * Utiliza los modelos de dominio
  * Orquestra (serie de pasos)
  * Toca infraestructura
  * Llama otros servicios
  * Si un servicio tiene mas de un metodo publico, entonces probablemente haga mas de una cosa  != SRP
* Modelo de dominio:
  * Datos + Comportamiento
  * Modelos anemicos (Sin comportamiento)
* Finalidad:
  * Alta cohesión y robustez
  * Permitir composición de clases (inyectar colaboradores)
  * Evitar duplicidad de código
* Ejemplo:
  * Order | User: Modelos de dominio -> BIEN
  * OrderAnalyzer | OrderProcessor: Servicios, pero nombres demasiado genericos y que haran mas de una cosa != SRP -> MAL
  * OrderTrustabilityChecker | OrderMarginCalculator: Servicios que realizan una funcion especifica -> BIEN
  
#### Ejemeplo:

Este ejemplo es incorrecto, porque se esta acoplando la salida (pintar en pantalla) con el modelo de datos.

```java
final class Book
{
    public String getTitle()
    {
        return "A great book";
    }
    public String getAuthor()
    {
        return "John Doe";
    }
    public void printCurrentPage()
    { 
        System.out.println("current page content");
    }
}

final class Client
{
    public Client() {
        Book book = new Book(…);
        book.printCurrentPage();
    }
}
```

El correcto seria el siguiente, en el que desacopla la salida del modelo:

```java
final class Book
{
    public String getTitle()
    {
        return "A great book";
    }
    public String getAuthor()
    {
        return "John Doe";
    }
    public String getCurrentPage()
    {
        return "current page content";
    }
}

final class StandardOutputPrinter
{
    public void printPage(String page)
    {
        System.out.println(page);
    }
}

final class Client
{
    public Client() {
        Book book = new Book(…);
        String currentPage = book.getCurrentPage();
        StandardOutputPrinter printer = new StandardOutputPrinter();
        printer.printPage(currentPage);
    }
}
```

Se podria extraer el comportamiento con una interfaz (por si se quisiera implementar otra forma de salida):

```java
interface Printer
{
    public void printPage(String page);
}

final class StandardOutputPrinter implements Printer
{
    public void printPage(String page)
    {
        System.out.println(page);
    }
}

inal class StandardOutputHtmlPrinter implements Printer
{
    public void printPage(String page)
    {
        System.out.println("<div>" + page + "</div>");
    }
}
```

## Keep It Real

* Para el caso de aplicacion web: MVC
  * Habria que crear una clases para cada recurso/operacion (VideoPostController)
  * A esta clase, se le inyectaria el servicio que va a usar (VideoCreator)
  * En el caso del VideoCreator, inyectaria el repositori, para insertar el video en BBDD, pero antes crearia la instancia del objeto.
* Para el caso de CQRS
  * El punto de entrada (tambien una clases para recurso/operacion)
  * Crearia el "command" con los parametros de entrada y haria el dispatch
  
## Test
¿Qué beneficios obtenemos al aplicar el Principio de Responsabilidad Única?
- [ ] Permitir composición de clases (inyectar colaboradores)
- [ ] Evitar duplicidad de código
- [ ] Alta cohesión y robustez
- [x] Todas las anteriores

¿Cuándo empujaremos la lógica de negocio hacia nuestros modelos de dominio?
- [ ] Siempre. La Programación Orientada a Objetos se particulariza por representar en clases los datos + su comportamiento asociado
- [x] Siempre que no requiera de dependencias externas. En ese caso extraeremos esa lógica a un servicio aparte para poderlo componer
- [ ] Depende de cómo me levante ese día, tampoco hay un criterio claro.

