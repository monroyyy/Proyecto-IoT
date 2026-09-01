# ESP32

## ¿Qué es?

Microcontrolador de bajo costo con Wi-Fi y Bluetooth integrados, doble núcleo y suficientes pines GPIO/analógicos para leer sensores y controlar actuadores al mismo tiempo que mantiene comunicación en red.

## Función en TeleBrazo

Se usan **dos ESP32**, uno en cada extremo del sistema:

- **ESP32 maestro**: lee continuamente los 5 potenciómetros del brazo maestro (entradas analógicas), convierte esas lecturas en ángulos y las publica como mensajes MQTT hacia el broker en la nube.
- **ESP32 esclavo**: se suscribe a los tópicos MQTT donde llegan los ángulos, y mueve los 5 servomotores del brazo físico para replicar la pose indicada. También publica telemetría (ángulo comandado, ángulo real, consumo, marca de tiempo) que alimenta al backend.

## Por qué se eligió

- Ya se cuenta con unidades disponibles, sin costo adicional.
- El Wi-Fi integrado permite conexión directa a internet para publicar/consumir MQTT sin hardware de red adicional.
- Suficientes canales PWM para controlar los 5 servos y suficientes entradas ADC para los 5 potenciómetros.

## Consideraciones técnicas

- La lectura analógica de los potenciómetros debe filtrarse (por ejemplo, promedio móvil) para evitar ruido que se traduzca en temblores del brazo esclavo.
- El envío de ángulos por MQTT debe hacerse a una frecuencia que balancee fluidez de movimiento contra consumo de ancho de banda y carga del broker.
- Se debe sincronizar el rango de movimiento físico de cada articulación del maestro con el rango físico real del esclavo (mapeo de ángulos).
