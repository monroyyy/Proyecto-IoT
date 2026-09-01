# Modelo de detección de anomalías (red neuronal)

## ¿Qué es?

Modelo de aprendizaje automático (red neuronal) entrenado con datos de **operación normal** del brazo robótico, capaz de reconocer patrones habituales de movimiento y consumo, y señalar cuándo el comportamiento actual se desvía de ese patrón esperado.

## Función en TeleBrazo

Analiza continuamente la telemetría del brazo esclavo (ángulo comandado vs. ángulo real, consumo de corriente por servo, latencia de respuesta) para detectar señales tempranas de:

- **Desgaste mecánico** (por ejemplo, un servo que empieza a necesitar más corriente o tarda más en alcanzar el ángulo objetivo que antes).
- **Atascos** (una articulación que no logra llegar al ángulo comandado, o cuyo consumo se dispara de forma anómala).

Cuando detecta una desviación significativa respecto al comportamiento normal aprendido, genera una **alerta** que se envía al backend y se muestra en el dashboard, permitiendo intervención antes de una falla mayor.

## Por qué se eligió este enfoque

- Un enfoque basado en aprender el comportamiento normal (en vez de reglas fijas tipo "si el consumo supera X") permite detectar anomalías sutiles y específicas de cada articulación, que serían difíciles de capturar con umbrales manuales.
- Es coherente con el objetivo del proyecto de ir más allá de la simple teleoperación y aportar valor de mantenimiento predictivo, además de aprovechar la experiencia previa en redes neuronales.

## Consideraciones técnicas

- Requiere una fase inicial de recolección de datos de operación normal (sin fallas) para entrenar el modelo antes de poder usarlo en producción.
- El modelo debe correr en un servicio de inferencia que reciba telemetría reciente (desde la base de datos o directamente del backend) y devuelva resultados con la suficiente rapidez para que las alertas sean útiles en tiempo real.
- Es necesario definir cómo se valida el modelo (por ejemplo, provocando de forma controlada alguna anomalía leve) para reportar métricas reales de desempeño en la documentación final.
