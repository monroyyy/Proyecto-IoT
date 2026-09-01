import time
import math
import json
import paho.mqtt.client as mqtt

# Usamos un broker público para hacer pruebas sin necesidad de instalar nada aún
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC_CONTROL = "telebrazo/control/angulos"

PUBLISH_INTERVAL_SEC = 0.1  # 10Hz (10 mensajes por segundo)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[OK] Conectado exitosamente a {BROKER}")
    else:
        print(f"[ERROR] Fallo al conectar. Codigo: {rc}")

def simulate_angles(step):
    """
    Genera ángulos simulados (0-180) para los 5 servos usando funciones senoidales.
    Esto permite simular un brazo moviéndose de forma natural y fluida, 
    no con saltos erráticos que romperían el modelo 3D.
    """
    return {
        "servo1_base": int(90 + 90 * math.sin(step * 0.05)),
        "servo2_hombro": int(90 + 45 * math.sin(step * 0.03)),
        "servo3_codo": int(90 + 60 * math.sin(step * 0.04 + math.pi/4)),
        "servo4_muneca_pitch": int(90 + 30 * math.sin(step * 0.06)),
        "servo5_garra": int(45 + 45 * math.sin(step * 0.1))
    }

def main():
    print("[INFO] Iniciando Simulador de ESP32 Maestro (Software)...")
    
    client = mqtt.Client()
    client.on_connect = on_connect
    
    print(f"Conectando a {BROKER}:{PORT}...")
    try:
        client.connect(BROKER, PORT, 60)
    except Exception as e:
        print(f"Error conectando al broker: {e}")
        return

    client.loop_start()
    step = 0
    
    try:
        while True:
            # 1. Generar JSON de ángulos
            angulos = simulate_angles(step)
            payload = json.dumps(angulos)
            
            # 2. Publicar a MQTT
            client.publish(TOPIC_CONTROL, payload)
            print(f"[MQTT] Publicando a '{TOPIC_CONTROL}': {payload}")
            
            step += 1
            time.sleep(PUBLISH_INTERVAL_SEC)
            
    except KeyboardInterrupt:
        print("\n[INFO] Simulacion detenida por el usuario.")
    finally:
        client.loop_stop()
        client.disconnect()
        print("[INFO] Desconectado.")

if __name__ == "__main__":
    main()
