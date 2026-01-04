# **Día 2: Dominando Docker (Redes y Volúmenes)**

En este día vamos más allá de simplemente "correr un contenedor". Aprendemos cómo conectar contenedores entre sí y cómo compartir información de manera persistente.

Para esto, hemos construido dos proyectos distintos:

1. **Proyecto Web (Networking):** Un sitio web que se conecta a una base de datos.  
2. **Proyecto Producer-Consumer (Volumes):** Una tubería de procesamiento de datos compartidos.

## **🟢 Proyecto 1: Contador de Visitas (Concepto: Redes)**

Este proyecto demuestra cómo dos contenedores aislados (web y redis) pueden hablarse entre sí usando una red interna de Docker.

### **📂 Estructura**

Ubicación: ./web

* **web/:** Aplicación en Flask (Python).  
* **redis:** Base de datos en memoria (Imagen oficial).

### **🧠 Concepto Clave**

En el código de Python, no conectamos a localhost. Conectamos a host='redis\_service'. Docker resuelve mágicamente ese nombre a la dirección IP interna del contenedor de base de datos.

### **🚀 Cómo ejecutarlo**

1. Entra a la carpeta:  
   cd web

2. Inicia el sistema:  
   docker compose up \--build

3. Abre tu navegador en: http://localhost:8000

## **🔵 Proyecto 2: Producer-Consumer (Concepto: Volúmenes)**

Este proyecto demuestra cómo compartir archivos entre contenedores que **no** se hablan por red, usando un disco compartido (Volumen).

### **📂 Estructura**

Ubicación: ./producer-consumer

* **producer:** Genera órdenes de compra (archivos JSON).  
* **consumer:** Procesa y elimina esas órdenes.  
* **Volumen shared\_data:** Carpeta compartida donde ocurre la magia.

### **🧠 Concepto Clave**

Aunque los contenedores son efímeros y aislados, definimos un volumen en docker-compose.yml. Ambos contenedores "montan" ese volumen en la ruta /shared\_data, permitiéndoles ver y modificar los mismos archivos en tiempo real.

### **🚀 Cómo ejecutarlo**

1. Entra a la carpeta:  
   cd producer-consumer

2. Inicia la tubería:  
   docker compose up \--build

3. Observa los logs en la terminal para ver cómo interactúan el Productor y el Consumidor.

## **🧹 Comandos Globales Útiles**

* **Detener contenedores:** Ctrl \+ C  
* **Limpiar todo (Detener y borrar contenedores/redes):**  
  docker compose down

* **Limpiar contenedores huérfanos (si cambias nombres):**  
  docker compose down \--remove-orphans

**Resumen del Día:**

* Si necesitas que los servicios se hablen (ej. App \-\> Base de Datos) ➡️ Usa **Redes** (nombres de servicio).  
* Si necesitas compartir archivos (ej. Generador \-\> Procesador) ➡️ Usa **Volúmenes**.