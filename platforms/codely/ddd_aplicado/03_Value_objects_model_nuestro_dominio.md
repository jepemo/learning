# Value Objects: Modelando nuestro dominio

## Refactorizando a Value Objects

* Respecto al codigo anterior:

```php
final class StudentSignUpper
{
    private static $students;

    public function __invoke(string $studentId, string $studentName, string $studentPassword){
        $existentStudent = get($studentId, self::$students);

        if(null !== $existentStudent)
        {
            throw new StudentAlreadyExist($studentId)
        }

        $student = new Student($studentId,$studentName,$studentPassword);

        self::$students[$studentId] = $studentId;
    }
}
```

* Si tenemos reglas de negocio para los parametros de entrada, hay que validarlos. 
  * Se puede hacer en el caso de uso (un if detras de otro)
  * O con value objects
* Caso de ponerlo en el caso de uso:

```php
final class StudentSignUpper
{
    private static $students;

	public function __invoke(string $studentId, string $studentName, string $studentPassword)
	{
		if(\strlen($studentPassword) > 5)
		{
			if(1 === preg_match('~[0-9]~'))
			{
				$existentStudent = get($studentId, self::$students);

				if(null !== $existentStudent)
				{
					throw new StudentAlreadyExist($studentId);
				}

				$student = new Student($studentId,$studentName,$studentPassword);

				self::$students[$studentId] = $studentId;
			} else {
				throw new \RuntimeException('The password should have at least a digit');
			}

    } else {
			throw new \RuntimeException('The password should have more than 5 characters');
		}

    }
}
```

* Primer se refactorizaria para invertir las clausulas de guarda. Es decir, que devuelvan en primer lugar:
   * Asi se disminuye la complejidad ciclomatica

```php
final class StudentSignUpper
{
    private static $students;

	public function __invoke(string $studentId, string $studentName, string $studentPassword)
	{
		if(\strlen($studentPassword) > 5)
		{
			throw new \RuntimeException('The password should have more than 5 characters');
		}
		{
		if(1 !== preg_match('~[0-9]~'))
		{
			throw new \RuntimeException('The password should have at least a digit');
    }
		
		$existentStudent = get($studentId, self::$students);

		if(null !== $existentStudent)
		{
			throw new StudentAlreadyExist($studentId);
		}

		$student = new Student($studentId,$studentName,$studentPassword);

		self::$students[$studentId] = $studentId;

    }
}
```

* Luego se extraerian esas clausulas:

```php
final class StudentSignUpper
{
  // ...
	
	private function ensurePasswordHasAtLeast5Characters(string $studentPassword)
	{
		if(\strlen($studentPassword) < 5)
		{
			throw new \RuntimeException()
		}
	}

	private function ensurePasswordHasAtLeast1Numer(string $studentPassword)
	{
		if(1 !== preg_match('~[0-9]~'))
		{
			throw new \RuntimeException('The password should have at least a digit');
		} 
	}

	private function ensureStudentDoesntExist(string $studentId)
	{
		$existentStudent = get($studentId, self::$students);
		if(null !== $existentStudent)
		{
			throw new StudentAlreadyExist($studentId);
		}
	}
}
```

* Finalmente se puede mover esa logica al value object:

```php
// por ejemplo para el caso del password
final class StudentPassword
{
	private $value;

	public function __construct(string $value)
	{
		ensurePasswordHasAtLeast5Characters($value)
		ensurePasswordHasAtLeast1Numer($value)

		$this->value = $value;
	}
	private function ensurePasswordHasAtLeast5Characters(string $studentPassword){
		// ...
	}
	private function ensurePasswordHasAtLeast1Numer(string $studentPassword){
		// ...
	}
}
```

* Con lo que en el caso de uso, simplemente se haria:
  * La instanaciacion de los value objects se haria en la infraestrcutura.

```php
final class StudentSignUpper
{
    private static $students;

	public function __invoke(string $studentId, StudentName $name, StudentPassword $password)
	{
		$student = new Student($studentId,$name,$password);

		self::$students[$studentId] = $studentId;				

	}
	// ...
```

* Por lo tanto, los Value Objects:
  * Nos van permitir no tener que duplicar las validaciones en nuestra aplicación
  * Añaden semántica en las firmas de métodos
  * Podremos encapsular fragmentos de lógica y empujarla hacia nuestro Dominio

## ¿Dónde poner validaciones?

* Se podrian poner en varios sitios:
  * En el Controlador
  * En el Caso de Uso
  * En el Value Object
  * En la Entidad
  * En un Servicio de Dominio que fuera utilizado tanto desde el Value Object como desde el Controlador
* Que pasa si quieres que en un paso te diga todas las validaciones (ejemplo formulario largo web)
  * Doble Validacion: La forma más sencilla sería duplicar en el front de la aplicación las validaciones que realices en el back, de tal modo que el usuario pueda ver los errores en el formulario. En este punto, cuando alguien atacase directamente a nuestra API, seguiríamos devolviendo los errores uno a uno
  * Control de errores mediante tipos de retorno: Como hemos visto, un inconveniente de manejar los errores a través del lanzamiento de excepciones es que estas romperán el flujo de nuestra aplicación, por lo que no se continúa realizando el resto de validaciones. Una alternativa a esto es llevar a cabo el manejo de errores mediante tipos de retorno
    * Es decir, devolver un optional: vacio si va bien o un/lista de errores si hay errores. (solucion mas funcional)
  * ¿Y un Servicio compartido entre el Controlador y el Value Object?
    * El problema que vemos de utilizar un Servicio compartido por estas dos piezas de la aplicación es que normlamente no vamos a querer darle el mismo tratamiento a los errores en ambos puntos. Por ejemplo, mientras que a nivel de Dominio lanzaríamos una excepción, en el Controlador no querremos lanzarla, sino acumular los errores en un array o algún otro componente de validación del formulario
    * Además, hacer uso de este Servicio desde los Value Objects nos obligaría a recibir una instancia del servicio o instanciarla ahí mismo, con los inconvenientes que tendía a nivel de gestión de memoria.
    
    
