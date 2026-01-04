import numpy as np
import sys
def ejecutar_ordenamiento_legacy():
    version_actual = np.__version__
    print(f"⚙️ Versión de Numpy detectada: {version_actual}")
    
    datos = np.array([5, 2, 9, 1, 5, 6])
    print(f"📊 Datos originales: {datos}")
    
    # Uso de mergesort
    ordenados = np.msort(datos)
    print(f"✅ Datos ordenados (Legacy Mergesort): {ordenados}")

if __name__ == "__main__":
    ejecutar_ordenamiento_legacy()