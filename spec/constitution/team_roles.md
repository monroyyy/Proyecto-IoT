# Roles y División de Tareas

El trabajo se divide en 3 personas, priorizando la estabilidad física inicial.

## 🧑‍💻 Persona 1 (Jorge Monroy Peña)
- ESP32 Maestro (lectura analógica, filtros de ruido).
- ESP32 Esclavo (control PWM de servomotores, mapeo de ángulos).
- Publicación a MQTT y recolección de consumo de corriente.

## 🧑‍💻 Persona 2 (Diana Laura Pérez)
- Infraestructura MQTT.
- Base de Datos de Series de Tiempo.
- Backend API para ingesta y exposición de datos.

## 🧑‍💻 Persona 3 (Edgar Rodríguez)
- Dashboard Web.
- Gemelo Digital (render 3D).
- Integración de Video y Gráficas de Telemetría.
