# Alternativa 1: Microlitos sin infraestructura

## Teoria

* Microlito = Microservicio + Monolito
* Tenemos el problema de tipos de clientes distintos con cargas distintas
* ¿Cuando pasar a (micro)servicios(s)? Aspectos:
  * Escalabilidad equipos de desarrollo
  * Escalabilidad implementación (ecosistema específico por necesidad)
  * Escalabilidad aplicación (recursos específicos por necesidades)
  * Escalabilidad infraestructura (cuello de botella entre necesidades)
  * No es un todo o nada
* En el ejemplo, de solucion, dividimos los dos casos de uso (de cargas distintas) en dos servicios diferentes

```
(Movil) GET /users/x ---> [UsersService]    [VideosService] <--- PUT /videos/x (Web)
                               |                |
                               |                |
                               v                v
                                  [MISMA BBDD]
```
