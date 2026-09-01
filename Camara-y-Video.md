# Cámara y video en vivo (ESP32-CAM / Raspberry Pi + cámara)

## ¿Qué es?

Módulo de captura de video ubicado en el sitio remoto (junto al brazo esclavo). Puede implementarse con un **ESP32-CAM** (todo en un solo módulo, económico y de bajo consumo) o con una **Raspberry Pi + cámara** (más capacidad de cómputo y mejor calidad/latencia de streaming).

## Función en TeleBrazo

Transmite **video en vivo** del sitio donde opera el brazo esclavo, dando al operador contexto visual de lo que el brazo está manipulando mientras lo controla a distancia. Este video se integra en el dashboard web junto con la telemetría y la visualización del gemelo digital, para que el operador no dependa únicamente de los ángulos numéricos.

## Por qué se eligió esta opción

- Es indispensable para la teleoperación: sin retroalimentación visual, el operador mueve el brazo "a ciegas".
- Elegir entre ESP32-CAM o Raspberry Pi depende del balance deseado entre costo/simplicidad (ESP32-CAM) y calidad/latencia de video (Raspberry Pi).

## Consideraciones técnicas

- La latencia de video es una de las métricas clave del proyecto (latencia extremo a extremo); debe medirse y reportarse en la documentación final.
- El streaming debe compartir la red/infraestructura en la nube sin saturar el ancho de banda usado por MQTT y la telemetría.
- Es necesario definir un protocolo de streaming (MJPEG, WebRTC, RTSP, etc.) que balancee calidad de imagen contra consumo de ancho de banda y complejidad de implementación.
