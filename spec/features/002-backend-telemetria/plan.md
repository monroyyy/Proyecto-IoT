# Plan - Backend y Telemetría

1. **Broker:** Desplegar el broker y asegurar que los ESP32 puedan conectarse y publicar/suscribirse.
2. **Persistencia:** Configurar esquemas, retención y tags en la base de datos de series de tiempo.
3. **API:** Desarrollar los servicios backend que fungen de puente entre MQTT, TSDB y los clientes web.
