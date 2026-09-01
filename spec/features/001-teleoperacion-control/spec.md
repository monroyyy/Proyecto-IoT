# Feature 001: Teleoperación y Control Físico

## Descripción
El núcleo del proyecto. Permite que el brazo esclavo replique los movimientos del control maestro en tiempo real, leyendo 5 potenciómetros y moviendo 5 servomotores, publicando la telemetría a través de MQTT.

## Especificaciones
- **Hardware:** 2 ESP32 (Maestro y Esclavo).
- **Entradas:** 5 Potenciómetros (lectura analógica filtrada).
- **Salidas:** 5 Servomotores (control PWM).
- **Comunicación:** Protocolo MQTT (WiFi).
- **Telemetría:** Extraer ángulos reales, consumos de corriente y latencia.
