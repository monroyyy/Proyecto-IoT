# Broker MQTT

## ¿Qué es?

MQTT es un protocolo de mensajería ligero, basado en el patrón publicador/suscriptor, diseñado para dispositivos con recursos limitados y redes poco confiables. El **broker** es el servidor central que recibe los mensajes publicados por unos dispositivos y los reenvía a todos los dispositivos suscritos al mismo tópico.

## Función en TeleBrazo

Es el **canal de comunicación** entre los dos ESP32, alojado **en la nube** (no en la red local) para que el maestro y el esclavo puedan estar en ubicaciones físicas distintas, comunicándose a través de internet:

- El ESP32 maestro publica los ángulos leídos de los potenciómetros en tópicos como `telebrazo/maestro/angulos`.
- El ESP32 esclavo está suscrito a ese tópico y actúa en cuanto llega un nuevo mensaje.
- El ESP32 esclavo publica telemetría (ángulo real, consumo, timestamp) en tópicos como `telebrazo/esclavo/telemetria`, a los que el backend está suscrito para almacenar los datos.

## Por qué se eligió

- MQTT es el estándar de facto en IoT para comunicación de baja latencia y bajo consumo entre dispositivos y la nube.
- Al ser en la nube (y no un broker local), el sistema deja de depender de que maestro y esclavo compartan la misma red Wi-Fi, habilitando teleoperación real a distancia.

## Consideraciones técnicas

- La calidad de servicio (QoS) del mensaje debe elegirse según la prioridad: los ángulos de control probablemente usan QoS 0/1 (prioriza velocidad), mientras que la telemetría puede tolerar QoS 1 para no perder datos.
- El tiempo que tarda un mensaje en ir del maestro al esclavo vía el broker es un componente central de la **latencia extremo a extremo** que el proyecto busca medir y reportar.
- Se debe asegurar la conexión (usuario/contraseña o TLS) ya que el broker está expuesto en internet.
