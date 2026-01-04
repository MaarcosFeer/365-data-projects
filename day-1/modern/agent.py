import numpy as np
import sys

def lectura_rapida():
    version_actual = np.__version__
    print(f"🤖 Iniciando Agente Moderno...")
    print(f"⚙️ Versión de Numpy detectada: {version_actual}")
    print("🔄 Procesando datos con algoritmos nuevos...")

    # Tupla cruda con datos (una matriz 2x2 simulada en una lista plana)
    datos_crudos = [[10, 20], [30, 40]]
    
    # 1. Creamos el array (Esto funciona en todas las versiones)
    matriz = np.array(datos_crudos)
    print(f"📡 Matriz original:\n{matriz}")

    # 2. INTENTO DE USO DE FUNCIONALIDAD NUEVA
    # La función 'matrix_transpose' fue agregada en Numpy 1.25.0.
    # Si tienes Numpy 1.24.2, esta línea hará COLAPSAR el programa
    # con un 'AttributeError'.
    
    try:
        transpuesta = np.matrix_transpose(matriz)
        print(f"✅ Transpuesta calculada (Función Nueva):\n{transpuesta}")
    except AttributeError as e:
        print("\n💥 ERROR CRÍTICO REAL:")
        print(f"   Python dice: {e}")

        sys.exit(1)


if __name__ == "__main__":
    lectura_rapida()