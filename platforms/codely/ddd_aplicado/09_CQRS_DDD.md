# CQRS en DDD

## Flujo petición CQRS vs Hexagonal

* Repaso capas arquitectura hexagonal
  * Infraestructura: recibe peticiones HTTP/BBDD
    * Ahora mismo instancia los VO para pasarselos a los casos de USO
    * Accede a capa aplicacion y dominio (repositorio, VO)
  * Aplicacion: Casos de uso
    * Accede a capa de dominio
  * Dominio: mi dominio 
    * Se comunica consigo mismo
* Flujo:

```
-> Controller -> Application Service -> Services
                                     -> Models
                                     -> Repos    <--- Implementation
```

* Arquitectura CQRS
  * Nuvos compoenentes:
    * Command/query: para modificar estado y realizar consutlas (Capa de aplicacion)
    * BUS: Donde se envian los comandos/queries (Capa infraestructura)
    * Handler: (ESTA EN CAPA DE SERVICIO)
      * Recibe el command/query instancia valueobjects
      * Tiene inyectados los casos de uso y
      * Llama al caso de uso
  * Al lanzar una query (querybus) nos devuelve un objeto response
    * El caso de uso para la vuelta podria tener el serializador de vuelta
  * El controller ya no llama directamente al App.Service
    * Sino con el BUS
    * Se simplifica el controller
```
    /----> COMMAND/QUERY
    |
-> CTRL -> BUS -> HANDLER -> APP. SERVICE -> SERVICES
                                          -> MODELS
                                          -> REPOS   <----- IMPL.
```
