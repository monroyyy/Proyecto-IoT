# Wiki de Componentes de TeleBrazo

Bienvenido a la Wiki técnica del proyecto. Aquí se describe cada componente de hardware y software que conforma la arquitectura de **TeleBrazo**, explicando qué es y qué función cumple dentro del sistema.

## 🧠 Hardware de Control
*El cerebro electrónico que lee comandos y mueve el brazo.*

- **[ESP32](./ESP32.md):** Microcontroladores con Wi-Fi/Bluetooth. Tenemos dos: el "Maestro" lee el controlador manual del operador, y el "Esclavo" mueve los servomotores y recolecta telemetría. Actúan como los nodos edge del proyecto.

## 🦾 Sensores y Actuadores
*La interfaz con el mundo físico.*

- **[Potenciómetros](./Potenciometros.md):** Resistencias variables ubicadas en las articulaciones del controlador Maestro. Sirven como sensores para saber exactamente qué ángulo desea el operador.
- **[Servomotores](./Servomotores.md):** Motores con control de posición ubicados en el brazo Esclavo. Su función es ejecutar el movimiento comandado y aplicar la fuerza física necesaria.

## 👁️ Visión y Video
*Ojos remotos para el operador.*

- **[Cámara y Video](./Camara-y-Video.md):** Módulo de cámara IP que transmite un flujo de video de baja latencia al dashboard, permitiendo operar el brazo sin línea de visión directa.

## 📡 Comunicación y Datos
*El sistema nervioso central.*

- **[Broker MQTT](./Broker-MQTT.md):** Servidor de mensajería asíncrona de altísimo rendimiento. Su función es recibir los comandos de movimiento y la telemetría, distribuyéndolos entre el Maestro, el Esclavo y el Backend en milisegundos.
- **[Base de Datos de Series de Tiempo](./Base-de-Datos-Series-de-Tiempo.md):** Base de datos (ej. InfluxDB) optimizada para marcas de tiempo. Guarda el historial de telemetría (ángulos y corrientes eléctricas de los servos) para generar analíticas de consumo y estrés mecánico.
- **[Backend API](./Backend-API.md):** Servicios y endpoints (REST/WebSockets) que leen del Broker MQTT, insertan a la base de datos, y proporcionan datos al Dashboard Web.

## 💻 Interfaz e Inteligencia
*La ventana hacia el sistema.*

- **[Dashboard Web](./Dashboard-Web.md):** Interfaz gráfica para el operador. Sirve para ver el **Gemelo Digital 3D** moviéndose en vivo, monitorear gráficas de salud de los motores y ver la cámara.
- **[Modelo de Detección de Anomalías](./Modelo-Deteccion-Anomalias.md) (Fase 2):** Red neuronal que analiza el historial de telemetría en la Base de Datos para detectar de manera predictiva atascos y fallas antes de que rompan el sistema.
