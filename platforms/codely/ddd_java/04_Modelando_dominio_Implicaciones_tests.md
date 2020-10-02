# Modelando el dominio: Implicaciones en tests

## Patrón ObjectMother para nuestros tests

* Para evitar tener que estar modificando tests cada vez que cambie alguna particularidad en nuestro dominio usaremos el Patrón ObjectMother
* Un ObjectMother es una factoría que nos va a permitir crear instancias del objeto en cuestión que estemos ‘wrappeando’. Tal como venimos haciendo, mimificaremos en tests lo que tengamos en real, por lo que llevaremos estos ObjectMothers a la carpeta de dominio del módulo en el directorio de tests.
* Clase CourseNameMother

```java
public final class CourseNameMother {
    public static CourseName create(String value) {
        return new CourseName(value);
    }

    public static CourseName random() {
        return create(WordMother.random());
    }
}
```

* Generalmente todos nuestros ObjectMothers tendrán dos métodos: uno que devolverá una instancia del objeto en base a un valor que recibamos por parámetro y otro que la devuelva en base a un valor aleatorio. Además de generar las instancias de nuestros Value Objects nos van a permitir que nuestros tests no se vean afectados si dichos Value Objects se modifican. Es precisamente por esto por lo que este método random() nos resulta tan útil, ya que podremos abstraernos en los tests de detalles como el valor que estamos definiendo por ejemplo para CourseName cuando lo que realmente nos interesa es validar que el curso se está guardando en BD
* A un nivel de abstracción superior y saliéndonos de nuestros conceptos de Dominio encontramos otro tipo de factorías como son los WordMother
* Tendremos que añadir en el fichero build.gradle de los tests del contexto de Mooc que los tests dependerán del contexto de Shared, que es donde tendremos la clase WordMother
* Para añadir valor a esta factoría y que podamos probar indirectamente la entrada de valores aleatorios en los tests nos apoyaremos en una librería externa como faker, que añadiremos en nuestros build.gradle. Una vez instalada, esta librería nos provee de una enorme cantidad de conceptos que podremos generar de forma aleatoria (En caso de tener restricciones de tamaño, tipo de caracteres… crearíamos métodos que acotasen estos valores a nuestras necesidades en la clase WordMother)
* Delegando en estos ObjectMothers la tarea de instanciar nuestro Agregado conseguimos no sólo la aleatoriedad de los valores utilizados en los tests, sino que estos queden mucho más limpios al eliminar ruído y que hablen mucho más de lo que validan en lugar de perderse en otros detalles menos relevantes
* Tal como hemos hecho con los Value Objects, también podremos disponer de ObjectMothers para nuestros Agregados. Estos seguirán teniendo un par de métodos para instanciar el agregado bien a partir de unos atributos recibidos o bien generándo estos valores de forma aleatoria, pero además hemos definido un método fromRequest() que nos permita hacer la instancia a partir de una Request como la que le llegaría al caso de uso (no una Request de Spring)

