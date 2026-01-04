# **Día 1: El Infierno de las Dependencias (Dependency Hell)**

Este proyecto simula un problema real en el desarrollo de software: **Dos programas en la misma computadora necesitan versiones diferentes de la misma librería.**

## **📂 Los Archivos del Reto**

1. **ordenar.py (El Proyecto Legacy 👴):**  
   * Es un script antiguo que usa la función np.msort.  
   * **Requisito:** Funciona solo con **Numpy antiguo** (versiones \< 1.20).  
   * **Falla:** Si usas Numpy moderno, dará error porque msort fue eliminado.  
2. **agent.py (El Proyecto Moderno 🤖):**  
   * Es un script nuevo que usa la función np.matrix\_transpose.  
   * **Requisito:** Funciona solo con **Numpy muy moderno** (versiones \>= 1.25).  
   * **Falla:** Si usas Numpy estándar (ej. 1.24.2) o antiguo, dará error porque la función no existe.

## **💥 Parte 1: Reproducir el Error**

Si intentas correr ambos scripts con tu instalación global de Python, al menos uno (o los dos) fallará.

### **1\. Prueba el Agente (Falla con versiones \< 1.25)**

Si tienes Numpy 1.24.2 instalado, corre:

python agent.py

Resultado Esperado: AttributeError: module 'numpy' has no attribute 'matrix\_transpose'.  
(Esto prueba que necesitas un entorno más nuevo).

### **2\. Prueba el Ordenador (Falla con versiones modernas)**

Si intentas arreglar lo anterior instalando el Numpy más reciente y corres el script viejo:

python ordenar.py

**Resultado Esperado:** Error indicando que np.msort no existe o advertencia de depreciación.

## **🛠️ Parte 2: La Solución (Entornos Virtuales)**

Para que ambos convivan en paz, crearemos "cajas" separadas para cada uno.

### **✅ Solución para agent.py (Entorno Moderno)**

1. **Crear el entorno:**  
   python \-m venv venv\_moderno

2. **Activar:**  
   * Windows: .\\venv\_moderno\\Scripts\\activate  
   * Mac/Linux: source venv\_moderno/bin/activate  
3. **Instalar Numpy Reciente:**  
   pip install "numpy\>=1.25.0"

4. **Ejecutar:**  
   python agent.py

   🎉 *Éxito: Verás la matriz transpuesta correctamente.*

### **✅ Solución para ordenar.py (Entorno Legacy)**

1. **Abrir una NUEVA terminal** (o desactivar el anterior con deactivate).  
2. **Crear el entorno:**  
   python \-m venv venv\_legacy

3. **Activar:**  
   * Windows: .\\venv\_legacy\\Scripts\\activate  
   * Mac/Linux: source venv\_legacy/bin/activate  
4. **Instalar Numpy Antiguo:**  
   pip install "numpy==1.19.5"

   *(Nota: Si usas Python 3.12+, versiones muy viejas pueden fallar al instalar. 1.19.5 suele ser estable).*  
5. **Ejecutar:**  
   python ordenar.py

   🎉 *Éxito: Verás los datos ordenados usando la función antigua.*

## **📝 Resumen**

| Script | Entorno Necesario | Versión de Numpy | Comando Clave |
| :---- | :---- | :---- | :---- |
| ordenar.py | venv\_legacy | \~1.19.0 | pip install "numpy\<1.20" |
| agent.py | venv\_moderno | 1.25+ | pip install \--upgrade numpy |

¡Nunca instales librerías globalmente\! Usa siempre python \-m venv.