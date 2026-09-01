# Backend / API

## ¿Qué es?

El servicio de servidor que conecta entre sí a todos los demás componentes: recibe datos del broker MQTT y del stream de video, los procesa y almacena, y expone la información al dashboard web mediante una API (REST y/o WebSockets para datos en tiempo real).

## Función en TeleBrazo

- Actúa como **puente** entre el broker MQTT y la base de datos de series de tiempo: se suscribe a los tópicos de telemetría y escribe cada lectura en la base de datos.
- Recibe el stream de video proveniente de la cámara y lo reenvía (o lo hace disponible) al dashboard.
- Expone endpoints/canales en tiempo real para que el dashboard reciba el estado actual del brazo (ángulos, consumo) sin tener que consultar directamente el broker o la base de datos.
- Orquesta la comunicación con el **modelo de detección de anomalías**: le envía los datos recientes de telemetría y recibe de vuelta las alertas generadas, para reenviarlas al dashboard.

## Por qué se eligió esta capa

- Sin un backend intermedio, el dashboard web tendría que hablar MQTT directamente desde el navegador y consultar la base de datos sin control de acceso ni lógica de negocio, lo cual complica la seguridad y la escalabilidad.
- Centralizar la lógica de orquestación (MQTT ↔ base de datos ↔ modelo de IA ↔ dashboard) en un solo servicio facilita medir y registrar la latencia extremo a extremo del sistema completo.

## Consideraciones técnicas

- Debe soportar comunicación en tiempo real hacia el frontend (WebSockets o Server-Sent Events) para que el dashboard se actualice sin necesidad de refrescar o hacer polling constante.
- Es el punto natural donde instrumentar las métricas de latencia (marca de tiempo de origen en el ESP32 vs. marca de tiempo de llegada al dashboard).
