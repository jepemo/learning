# Monolito - Cuándo son un problema

## Teoria

* Se quieren sistemas escalables: tanto mantenibles como en rendimiento
* Architectura monolitica:
  * Unica base de codigo donde esta implementado todo
  * Solamente se conecta a una BBDD
  * Varios tipos de clientes (mobile, web) se conectan a ella
  * Beneficio: 
    * Menos niveles de indirección
    * Añadir nuevas funcionalidades y encontrar bugs
  * Problemas:
    * Escalabilidad infraestructura (cuello de botella)
    * Escalabilidad aplicación (mismos recursos y ecosistema para distintas necesidades)
    * Escalabilidad equipos de desarrollo (gestión CVS)
* Temas
  * Identificar cuándo es un problema o limitación el seguir usando un monolito
  * Pros y contras de definir servicios compartiendo base de datos
  * Pros y contras de comunicar nuestros servicios vía APIs HTTP
  * Qué es un circuit breaker, cuándo usarlo, y qué beneficios aporta
  * * Afianzar conceptos de SOLID analizando el paralelismo entre su aplicación a nivel de clases y cómo llevarlo a nivel de arquitectura de servicios
  * Definir la estructura de nuestros eventos de dominio
  * Qué elementos componen un sistema de colas de mensajería
  * Qué tipos de exchange tenemos disponibles y cuándo usar cada uno de ellos
  * Gestionar errores derivados de las colas de mensajería como el orden no garantizado y la duplicidad de nuestros eventos al consumirlos
  * Definir nuestra estructura de colas en RabbitMQ
  * Aprovechar SNS y SQS para implementar nuestras colas en AWS optimizándolo para un consumo más eficiente
  * Publicar y consumir eventos desde sistemas como PHP y Scala (u otros lenguajes basados en JVM como Java)
  * Migrar de un monolito existente a microservicios de forma progresiva
  
## Test

¿Cuándo aplicaremos una arquitectura de microservicios?
- [ ] Al acabar el curso. Ya tendré los conocimientos y el primer proyecto que haga en el trabajo será aplicando microservicios independientemente de las necesidades.
- [ ] Cuando quiera rellenar mi currículum o LinkedIn con la skill de microservicios para MOLAR
- [x] Cuando me enfrente a un proyecto con las necesidades reales de escalabilidad y rendimiento que ofrecen
- [ ] Cuando tenga un proyecto sencillo en un monolito pero quiera sufrir teniendo que solucionar todos los problemas derivados de tener un sistema distribuido

¿Son malos los monolitos?
- [ ] Sí, siempre. Ya el propio nombre derivando de Manolito deja entrever poca seriedad.
- [x] No, todo depende del contexto. Para problemas sencillos, es una solución sencilla que evita tener que lidiar con muchos problemas de tener un sistema distribuido.

