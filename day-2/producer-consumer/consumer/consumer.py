import time
import json
import os
import glob

DATA_DIR = "/shared_data"

def procesar():
    print("🕵️ [CONSUMIDOR] Buscando archivos nuevos...")
    while True:
        # Buscar todos los .json en la carpeta compartida
        archivos = glob.glob(f"{DATA_DIR}/orden_*.json")
        
        if not archivos:
            print("💤 [CONSUMIDOR] Nada que hacer...")
        
        for archivo in archivos:
            try:
                with open(archivo, 'r') as f:
                    data = json.load(f)
                
                print(f"💰 [CONSUMIDOR] PROCESADO: {data['producto']} por ${data['precio']}")
                
                # Simular trabajo y borrar para no procesar de nuevo
                time.sleep(0.5)
                os.remove(archivo)
                print(f"🗑️ [CONSUMIDOR] Archivo eliminado: {archivo}")
                
            except Exception as e:
                print(f"❌ Error: {e}")
        
        time.sleep(5)

if __name__ == "__main__":
    procesar()