# TeleBrazo 🤖

**TeleBrazo** es un sistema robótico teleoperado de 5 ejes, diseñado para ofrecer un control fluido y preciso a distancia con muy baja latencia. El proyecto integra un control de hardware físico con una arquitectura IoT moderna, proporcionando además capacidades de telemetría en tiempo real y visualización remota mediante un gemelo digital.

## 👥 Equipo de Trabajo
- **Jorge Monroy Peña** -
- **Diana Laura Pérez** -
- **Edgar Rodríguez** -

## 🎯 Propósito del Proyecto y Problema que Resuelve
En entornos industriales, peligrosos o de difícil acceso (como manejo de materiales tóxicos, zonas de desastre o procesos de manufactura remota), la intervención humana directa representa un riesgo crítico. **TeleBrazo** resuelve este problema al permitir que un operador controle un brazo robótico a distancia de manera intuitiva (replicación de movimiento 1:1), sin sacrificar la retroalimentación. 

A diferencia de los brazos teleoperados tradicionales, TeleBrazo no actúa a ciegas:
1. Extrae **telemetría** constante de los motores (consumo eléctrico y precisión de ángulo) para anticipar fallos o atascos mecánicos antes de que sucedan.
2. Proporciona una interfaz web con un **gemelo digital en 3D** y video en tiempo real, mejorando radicalmente la conciencia situacional del operador remoto.

## ⚙️ ¿Cómo funciona?
El sistema está dividido en tres capas principales:

1. **Capa Física (Maestro y Esclavo):**
   - El operador mueve un brazo controlador (Maestro). Un ESP32 lee los ángulos de las articulaciones mediante potenciómetros.
   - Las señales se envían de forma asíncrona a través de WiFi mediante el protocolo **MQTT**.
   - El brazo real (Esclavo), gobernado por otro ESP32, recibe estas señales e imita los movimientos usando servomotores. Al mismo tiempo, extrae datos de su esfuerzo físico y los devuelve.
2. **Capa de Procesamiento (Backend y BD):**
   - Un broker MQTT gestiona el tráfico de mensajes en tiempo real.
   - Una API procesa la telemetría del esclavo y la almacena en una **Base de Datos de Series de Tiempo** (TSDB), lo que nos permite mantener un registro histórico milimétrico de la salud del brazo.
3. **Capa de Interfaz (Frontend):**
   - Un **Dashboard Web** consume los datos del backend para renderizar un modelo 3D que se mueve sincronizadamente con el brazo físico.
   - El dashboard muestra gráficas de telemetría y un flujo de video para apoyar visualmente la operación.

## 📂 Estructura del Repositorio
- `/wiki`: Contiene toda la documentación detallada de cada componente (Hardware, Backend, MQTT, etc.).
- `/spec`: Especificaciones de funcionalidades, planes y asignación de tareas del equipo.

Para conocer en detalle cada pieza del proyecto, dirígete a la [Wiki de Componentes](./wiki/Home.md).
