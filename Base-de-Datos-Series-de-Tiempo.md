# Base de datos de series de tiempo

## ¿Qué es?

Una base de datos optimizada para almacenar y consultar datos que llegan continuamente con una marca de tiempo (por ejemplo, InfluxDB, TimescaleDB), pensada para escrituras frecuentes y consultas por rangos de tiempo, mucho más eficiente para este caso que una base de datos relacional tradicional.

## Función en TeleBrazo

Almacena toda la **telemetría histórica** del sistema: ángulo comandado vs. ángulo real de cada servo, consumo de corriente, y marcas de tiempo usadas para calcular la latencia extremo a extremo. Esta base de datos es la fuente de la que:

- El **modelo de detección de anomalías** obtiene los datos de operación normal para entrenarse, y los datos recientes para comparar contra el comportamiento esperado.
- El **dashboard web** consulta el historial para graficar tendencias (por ejemplo, consumo de un servo a lo largo del tiempo) y no solo el estado instantáneo.

## Por qué se eligió

- La naturaleza de los datos del proyecto (lecturas periódicas con timestamp de sensores y actuadores) encaja exactamente con el caso de uso de una base de series de tiempo.
- Permite calcular métricas agregadas (promedios, picos, tendencias) necesarias tanto para el modelo de IA como para las gráficas del dashboard, de forma mucho más eficiente que con una base relacional genérica.

## Consideraciones técnicas

- Definir la política de retención de datos (cuánto tiempo se conserva la telemetría cruda antes de agregarla o descartarla).
- Diseñar el esquema de "measurements"/tags de forma que separar por articulación (servo 1 a 5) sea sencillo tanto para el entrenamiento del modelo como para las consultas del dashboard.
