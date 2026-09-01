# Feature 002: Backend y Telemetría

## Descripción
Infraestructura de datos del proyecto, encargada de recibir, persistir y servir la telemetría generada por el control físico.

## Especificaciones
- Broker MQTT central (local o nube).
- Base de Datos de Series de Tiempo (TSDB) optimizada para alta frecuencia de inserciones.
- API (REST/WebSockets) que consume los tópicos MQTT para guardar datos y los expone al Frontend.
