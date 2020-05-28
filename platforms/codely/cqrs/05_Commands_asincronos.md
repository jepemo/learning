# Commands asíncronos

## Read: Commands asíncronos

* Nos interesará aplicarla especialmente en todos aquellos casos en los que la lógica sea costosa.
* Diseño (para un ejemplo de hacer trim duración video):
  * Desde la Api: PATCH (porque queremos modificar un recurso que ya existe)
  * Llega al controlador: VideoDurationPathController y crea el command: TrimVideoCommand
  * Habra una implementacion del "CommandBus" de tipo Asincrona: AsyncCommandBus
  * Luego el proceso que lea de la cola asincrona, cuando vaya a utilizarlo, lo encolara en el "Bus sincrono"?
* Codigo:

````php
// La implementacion del Bus asincrono lo que hace el volcar el command, serializandolo, a un fichero.
```

## Test

¿Qué diferencia un Command síncrono de uno asíncrono?
- [ ] El síncrono se ejecuta en cuanto se recibe la petición y devuelve respuesta con la información del recurso, el asíncrono no
- [x] El síncrono se ejecuta en cuanto se recibe la petición, el asíncrono no
- [ ] El síncrono es como Javier Cansado, el asíncrono como Pepe Colubi

¿Por qué hacer un Command asíncrono?
- [ ] Porque quiero la complejidad de tener que gestionar esas casuísticas en la interface, y además coordinarlo en el backend. Sólo así seré un unicornio nivel 30
- [x] Porque tengo las necesidades a nivel de rendimiento que justifican asumir ese nivel de complejidad adicional
- [ ] Porque lo dice CodelyTV
