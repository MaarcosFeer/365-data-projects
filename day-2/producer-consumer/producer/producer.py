import time
import json
import random
import os
import uuid

# Ruta dentro del contenedor (debe ser un volumen compartido)
DATA_DIR = "/shared_data"

def generar_orden():
    print("🏭 [GENERADOR] Iniciando fábrica de órdenes...")
    while True:
        # Crear datos falsos
        orden_id = str(uuid.uuid4())[:8]
        orden = {
            "id": orden_id,
            "producto": random.choice(["Laptop", "Mouse", "Teclado", "Monitor"]),
            "precio": random.randint(20, 1500)
        }
        
        nombre_archivo = f"{DATA_DIR}/orden_{orden_id}.json"
        
        # Escribir archivo
        with open(nombre_archivo, 'w') as f:
            json.dump(orden, f)
        
        print(f"📦 [GENERADOR] Orden creada: {orden['producto']} (${orden['precio']})")
        
        time.sleep(3) # Pausa de 3 segundos

if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    generar_orden()