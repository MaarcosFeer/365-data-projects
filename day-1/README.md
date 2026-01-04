Proyecto Día 1: Entornos Virtuales en Python¿El Problema?Imagina que tienes dos proyectos en tu computadora:Proyecto A (Antiguo): Usa la librería pandas versión 1.0.Proyecto B (Nuevo): Usa la librería pandas versión 2.0.Si instalas pandas directamente en tu computadora (instalación global), solo puedes tener una versión. Al actualizarla para el Proyecto B, rompes el Proyecto A.La Solución: Entornos Virtuales (venv)Un entorno virtual es una carpeta que contiene una instalación de Python independiente y "limpia". Lo que instalas ahí, se queda ahí.🚀 El Proyecto PrácticoSigue estos pasos en tu terminal para completar el reto del Día 1.Paso 1: Crear la carpeta del proyectomkdir proyecto_day1
cd proyecto_day1
Paso 2: Crear el Entorno VirtualEste comando crea una carpeta llamada venv (o .venv) que contiene el Python aislado.# En Windows/Mac/Linux
python -m venv venv
(Si usas Mac/Linux y python no funciona, prueba con python3 -m venv venv)Paso 3: Activar el EntornoEste es el paso crucial. Fíjate que al hacerlo, aparecerá un (venv) en tu terminal.En Windows (PowerShell):.\venv\Scripts\Activate
(Si te da error de permisos, ejecuta Set-ExecutionPolicy Unrestricted -Scope Process y prueba de nuevo).En Windows (CMD):.\venv\Scripts\activate.bat
En Mac / Linux:source venv/bin/activate
Paso 4: Instalar una librería externaVamos a instalar una librería ligera llamada colorama para probar que estamos en el entorno.pip install colorama
Paso 5: Crear el script de prueba (main.py)Crea un archivo llamado main.py y pega el siguiente código para verificar que la librería funciona.from colorama import init, Fore, Style

# Inicializar colorama
init()

print(Fore.RED + "¡Hola Mundo desde mi Entorno Virtual!" + Style.RESET_ALL)
print(Fore.GREEN + "Si ves esto en colores, tu entorno funciona." + Style.RESET_ALL)
print(Fore.BLUE + "La librería 'colorama' está aislada aquí dentro." + Style.RESET_ALL)
Paso 6: Ejecutar el scriptpython main.py
Paso 7: Guardar tus dependencias (El estándar de la industria)Para que otro desarrollador sepa qué librerías usa tu proyecto, generamos un archivo de requisitos.pip freeze > requirements.txt
Abre el archivo requirements.txt y verás colorama listado allí con su versión exacta.Paso 8: Salir del entornoCuando termines de trabajar:deactivate
Verás que el prefijo (venv) desaparece. Si intentas correr python main.py ahora, probablemente fallará porque colorama no existe en tu sistema global (¡y eso es bueno!).Resumen de Comandos ClaveAcciónComandoCrearpython -m venv venvActivar (Win).\venv\Scripts\ActivateActivar (Mac/Linux)source venv/bin/activateInstalar libreríapip install nombre_libreriaGuardar listapip freeze > requirements.txtInstalar desde listapip install -r requirements.txtSalirdeactivate