# Potenciómetros

## ¿Qué son?

Resistencias variables cuyo valor cambia según la posición de un eje giratorio. Al conectarse como divisor de voltaje, entregan una señal analógica proporcional al ángulo en el que se encuentran.

## Función en TeleBrazo

Se coloca **un potenciómetro por cada articulación del brazo maestro** (5 en total), acoplado mecánicamente al eje de cada junta. Cuando el operador mueve el brazo maestro con la mano, cada potenciómetro reporta el ángulo actual de su articulación al ESP32 maestro, que traduce esa lectura analógica a un valor de ángulo (grados) para enviarlo por MQTT.

Son, en esencia, **la interfaz de entrada** de todo el sistema: sin ellos no hay forma de capturar la intención de movimiento del operador.

## Por qué se eligieron

- Son el sensor más simple y económico para capturar posición angular en un mecanismo réplica tipo "brazo maestro".
- Lectura directa por ADC del ESP32, sin necesidad de protocolos adicionales.

## Consideraciones técnicas

- Requieren calibración por articulación: mapear el rango físico de giro del potenciómetro (ej. 0–300°) al rango de movimiento real de esa junta.
- Sensibles al ruido eléctrico; conviene aplicar suavizado (filtro/promedio) antes de traducir la lectura a ángulo.
- El acoplamiento mecánico al eje debe ser firme para evitar lecturas erráticas por juego mecánico (backlash).
