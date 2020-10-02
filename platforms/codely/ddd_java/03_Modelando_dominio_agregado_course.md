# Modelando el dominio: Agregado Course

## Utilizando Request/Response para comunicarnos con los AS

* Ya hemos iniciado un planteamiento de desarrollo Outside-in, establecido mínimamente nuestra estrategia de testing e incluso hemos extraído el Application Service fuera del Controller, por lo que ya va siendo hora de llevar a cabo cierto refactor para comenzar a modelar nuestro dominio a través de las clases Request/Response
* Estas clases no tienen que ver con las Requests y Responses del protocolo HTTP, sino que se tratan de DTOs (También conocidos como POJOs en el ecosistema Java) que nos permitirán dar el paso para desacoplar los Controladores de los Servicios de Aplicación
* Hasta ahora, el procedimiento que llevábamos a cabo era invocar al caso de uso desde el controller pasándole directamente los atributos, sin embargo a la larga esto nos supondrá un problema tanto al comenzar a utilizar Value Objects que encapsulen cierta lógica de Dominio (¡Chirría instanciar estos elementos desde la capa de infraestructura!) como cuando queramos migrar a CQRS
* Aunque ya tenemos un objeto Request dentro del propio controller, no creemos que tenga sentido mantener su uso ya que el hecho de tener que pasarle los atributos a través de los setters supone siempre un riesgo de que olvidemos pasarle alguno de ellos y nos genere un error (es mucho más recomendable usar un objeto que nos fuerce a pasarle todos los campos en el constructor), además queremos poder reutilizar el caso de uso tanto en diferentes protocolos de comunicación como en Eventos de Dominio, por lo que nos interesa añadir esta ‘complejidad’ y evitar cualquier dependencia con la capa de infraestructura (como también suponía utilizar el objeto Request de Spring)
* Así pues crearemos nuestro propio CreateCourseRequest al mismo nivel de directorio que el caso de uso y con los mismos parámetros que el agregado Course. Será ahora esta request lo que reciba el método create() del caso de uso por parámetro, de donde extraerá los valores y seguirá el flujo tal y como habíamos visto hasta ahora
  * En courses.application.create
  
```java
// En controlador
// ...
this.creator.create(new CreateCourseRequest(id, request.name(), request.duration()));
// ...
```

* Estamos omitiendo el prefijo ‘get’ en los getters del DTO puesto que asumimos que los atributos de clase serán siempre privados (obligando a que las mutaciones de estado se den sólo dentro de la propia clase) y no habrá por tanto confusión respecto a si se llama al método o al propio atributo
Este refactor implicará también modificar nuestro test unitario del caso de uso para que el caso de uso reciba también una instancia de nuestro objeto request, los tests de aceptación, por su parte, no sufrirán ningún cambio ya que el protocolo de comunicación (con el cual interaccionamos en este test) no se ve afectado

## UUIDs como Identificadores

* Antes de entrar a ver cómo llevamos a cabo el modelado de los identificadores os recomendamos encarecidamente que hayáis visto el curso de CQRS, donde dedicamos una lección exclusívamente dedicada a explicar por qué pasar los identificadores desde el cliente. Con este punto de partida asumimos que lo que esperamos será entonces recibir estos identificadores en formato UUIDs
* El objetivo entonces es crear nuestro primer Value Object CourseId, el cual nos permitirá poner una capa por encima a la propia clase UUID de Java y en la cual podremos modelar y asegurarnos de que cumple con el formato que queremos
* El lenguaje Java nos provee de una clase UUID propia con un conjunto importante de métodos que nos facilitarán bastante la vida, ejemplo de ello es el método fromString(), que podremos usar a modo de named constructor para crear instancias de UUID en base a un String
* Para ser consistentes con nuestra API, nuestro Value Object tendrá un atributo ‘value’ que definiremos como privado y de tipo String. Este atributo sólo se asigna desde el constructor y únicamente después de haber pasado una cláusula de guarda que nos garantice que cumple con nuestro formato. Es aquí, en esta cláusula, donde aprovecharemos el fromString() del UUID de Java, que lanza una excepción cuando el String que le pasamos no es válido
* Clase Identifier (Resultado final):

```java
public abstract class Identifier implements Serializable {
    final protected String value;

    public Identifier(String value) {
        ensureValidUuid(value);

        this.value = value;
    }

    protected Identifier() {
        this.value = null;
    }

    public String value() {
        return value;
    }

    private void ensureValidUuid(String value) throws IllegalArgumentException {
        UUID.fromString(value);
    }

    // ... 
}
```

* Puesto que se trata de un patrón que va a repetirse en los identificadores de nuestros agregados, lo que haremos será sacar esta lógica a una clase abstracta Identifier en la carpeta Shared que ahora implementará nuestro CourseId (En el resultado final de esta clase, se ha añadido la interface Serializable para poder serializarla a formato Json)
* El hecho de que el atributo de clase sea un String y no directamente un UUID puede ser objeto de discusión y al final es algo que debe consensuar el equipo, pero si que es importante el hecho de evitar filtraciones de los detalles de la implementación, es decir, debemos evitar exponer (en el getter o el constructor de la clase) el tipo de datos que estamos wrappeando y en su lugar trabajar con datos primitivos tanto a la entrada como a la salida. Además, encapsular estos detalles nos facilitará muchísimo el trabajo si en algún momento tuviéramos la necesidad de modificarlos

## Value Objects: Immutabilidad y tips para agilizar desarrollo

* Ya que hemos visto cómo pasar nuestros identificadores a Value Objects, terminaremos esta lección siguiendo los mismos pasos con los demás atributos de nuestro Curso, añadiéndoles mayor semántica y permitiendo llevar a estos la lógica de validación.
* A diferencia del UUID, que nos interesa mantener compartido dentro del Shared Kernel al tratarse de una pieza que usaremos en la comunicación entre distintos módulos y contextos, querremos que los atributos CourseId y CourseDuration se mantengan dentro del módulo y evitar compartir su lógica. Ya que tendremos múltiples Value Objects en cada Bounded Context, nos va a interesar que su creación sea un proceso ágil 
* Clase CourseName:

```java
public final class CourseName extends StringValueObject {
    public CourseName(String value) {
        super(value);
    }

}
```

* El modificar directamente los argumentos que recibía el agregado Course de Strings a Value Objects y permitir que sea el propio IDE quien nos ayude a generar estas clases va a facilitarnos mucho la tarea, pero por supuesto es algo abierto al gusto de cada uno
* Ambos Value Objects encapsulan un atributo de tipo String, así que tal como vimos en el caso del UUID, también nos interesará hacer uso de la herencia y que extiendan de una clase padre StringValueObject En este caso no le vemos tanto sentido a extraerlo a un servicio y hacer uso de la composición (puesto que no tocamos Entrada/Salida de datos ni tratamos de abstraernos de algo que pueda cambiar en el futuro). Será interesante igualmente este tipo de jerarquía con otros Value Objects de distinto tipo (ej: IntValueObject)
* La clase StringValueObject nos encapsulará tanto la validación de que estamos recibiendo realmente un valor de tipo String como la implementación del método equals() que podremos utilizar para comparar por valores como veíamos previamente en los tests
* Al modificar el tipo de parámetros que recibe Course tendremos que modificar también aquellos puntos en nuestros tests donde estuviéramos instanciando esta clase, veremos en el siguiente video cómo hacer que nuestros tests sean menos frágiles a este tipo de cambios

## Test

* El hecho de recibir DTOs en el caso de uso nos permite...
- [x] Desacoplar el Controller de la capa de Aplicación
- [ ] Enviar mayor cantidad de parámetros
- [ ] Empujar las validaciones hasta el Controller

(Los DTOs son objetos planos para la comunicación entre clases/capas que nos ayudarán a desacoplar los controladores de los servicios de aplicación)

* Los Value Objects no exponen un metodo público setter del atributo que envuelven
- [ ] Incorrecto
- [ ] Sólo en el caso de los UUIDs
- [x] Correcto

(Los Value Objects deben ser inmutables, por lo que sólo se asigna valor al atributo envuelto desde el constructor y sólo si pasan la cláusula de guarda)

* Una de las ventajas que nos aporta el uso de Value Objects es...
- [ ] Encapsulacion de validaciones a nivel de Aplicación
- [x] Encapsulación de validaciones a nivel de Dominio
- [ ] Encapsulación de validaciones en el agregado

(Los Value Objects nos permiten empujar al Dominio ciertas validaciones como el tipo de dato recibido, que un string cumpla con cierta expresión regular o que el número recibido sea un valor positivo)
