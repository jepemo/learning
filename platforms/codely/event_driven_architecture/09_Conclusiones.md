# Conclusiones

* Principios Solid de diseño: pueden ser aplicados a nivel micro y a macro
  * En micro se usan interfaces para desacoplar
  * En macro se usan eventos para desacoplar
* Por lo que piensa sobre tus eventos de dominio como tus interfaces/contratos de tu dominio
* Intimidad inapropiada: Los servicios exponen informacion solo porque el otro servicio la necesita. 
  * Hay que simplificar los servicios limitando sus APIs.
* Domain events as ACL (Capa de anticorrupcion): Useful while refactoring legacy systems.


### Links

* [Testing CQRS talk (Spanish)](https://www.youtube.com/watch?v=cw6Va1ZW7iI)
* [We broke up with the monolith, and started dating #eventSourcing](https://www.slideshare.net/JavierCane/we-broke-up-with-the-monolith-and-started-dating-eventsourcing-symfonycat)
* [Versioning in an Event Sourced System](https://leanpub.com/esversioning)
* [RabbitMQ Simulator](http://tryrabbitmq.com/)
* [A Series of Fortunate Events](https://www.slideshare.net/matthiasnoback/a-series-of-fortunate-events-symfony-camp-sweden-2014)
* [The anatomy of Domain Event](https://blog.arkency.com/2016/05/the-anatomy-of-domain-event/)
* [Microservices: Improving the autonomy of our teams with Event-Driven Architecture (CodelyTV)](https://es.slideshare.net/CodelyTV/microservices-improving-the-autonomy-of-our-teams-with-eventdriven-architecture-cas2018)
