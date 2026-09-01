# Plan - Teleoperación y Control

1. **Fase de Pruebas Unitarias Hardware:** Probar sensores individuales y un servo aislado.
2. **Fase de Mapeo y Calibración:** Ajustar rangos analógicos contra rangos de grados físicos (0-180) asegurando que no haya colisiones físicas.
3. **Fase de Integración Inalámbrica:** Establecer comunicación MQTT Maestro-Esclavo y validar latencias sin el backend definitivo (usar broker local de prueba).
4. **Fase de Afinación:** Suavizado de movimientos (filtros de ruido) y gestión de la energía/consumos.
