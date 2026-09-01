# Servomotores

## ¿Qué son?

Actuadores rotativos que giran a un ángulo específico según una señal de control (típicamente PWM) y mantienen esa posición mientras se les indique.

## Función en TeleBrazo

Los **5 servomotores del brazo esclavo** son los actuadores finales del sistema: reciben del ESP32 esclavo el ángulo objetivo de cada articulación (traducido desde los mensajes MQTT que llegan del brazo maestro) y mueven físicamente el brazo para replicar la pose capturada en el sitio del operador.

Cada servo corresponde a un grado de libertad del brazo (base, hombro, codo, muñeca y pinza/efector final, según el diseño físico ya existente del brazo).

## Por qué se usan

- El brazo robótico de 5 servos ya está construido y disponible de un semestre anterior, por lo que no requiere fabricación adicional.
- Los servomotores permiten control de posición directo (a diferencia de un motor DC simple), lo cual es indispensable para replicar poses exactas.

## Consideraciones técnicas

- La corriente consumida por los 5 servos en conjunto puede superar lo que el regulador del ESP32 puede entregar; se necesita una fuente de alimentación externa dedicada para los servos.
- El consumo de corriente de cada servo es también una de las señales de telemetría usadas por el modelo de detección de anomalías (un consumo anormal puede indicar atasco o desgaste).
- Es necesario suavizar transiciones bruscas de ángulo (interpolación) para evitar movimientos violentos que dañen el mecanismo.
