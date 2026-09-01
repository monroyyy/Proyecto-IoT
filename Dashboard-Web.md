# Dashboard web (gemelo digital)

## ¿Qué es?

Aplicación web que funciona como el **gemelo digital** del brazo robótico: una representación visual e interactiva del estado real del sistema físico, actualizada en tiempo real.

## Función en TeleBrazo

Es la interfaz principal para el operador y para cualquier persona que quiera supervisar el sistema. Integra en una sola pantalla:

- **Visualización en tiempo real** de la pose del brazo (representación gráfica/3D o indicadores por articulación reflejando los ángulos actuales).
- **Video en vivo** proveniente de la cámara del sitio remoto.
- **Métricas de telemetría**: consumo por servo, latencia extremo a extremo, historial de movimientos.
- **Alertas de anomalías** generadas por el modelo de red neuronal, indicando qué articulación presenta un comportamiento fuera de lo normal.

## Por qué se eligió este enfoque

- Un dashboard web permite acceso remoto desde cualquier dispositivo con navegador, coherente con la naturaleza de teleoperación a distancia del proyecto.
- Concentrar estado, video y alertas en una sola vista es lo que convierte al sistema en un verdadero "gemelo digital" y no solo en un control remoto simple.

## Consideraciones técnicas

- Debe consumir datos en tiempo real del backend (WebSockets) para reflejar el estado del brazo sin retrasos perceptibles.
- El diseño debe priorizar que las alertas de anomalías sean visibles de inmediato (por ejemplo, con notificaciones o resaltado visual), ya que es una de las funciones diferenciadoras del proyecto.
- Es el lugar donde se reportan visualmente las métricas de desempeño (como la latencia) que forman parte de la documentación final del proyecto.
