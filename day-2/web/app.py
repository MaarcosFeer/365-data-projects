import sys
from flask import Flask
import redis
import os

# Mensaje de depuración visible en Docker
print("--> 🚀 Iniciando script de Python...", flush=True)

app = Flask(__name__)

# Configuración de Redis
redis_host = 'redis_service'
print(f"--> Configurado para conectar a Redis en: {redis_host}", flush=True)

cache = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    try:
        count = cache.incr('visitas')
        return f'<h1 style="color:green">¡Hola Docker!</h1><p>Esta página ha sido vista <b>{count}</b> veces.</p>'
    except redis.exceptions.ConnectionError as e:
        return f'<h1 style="color:red">Error: No puedo conectar con Redis.</h1><p>{e}</p>'

if __name__ == "__main__":
    print("--> 🌍 Servidor Flask arrancando en puerto 5000...", flush=True)
    # debug=False es más estable en algunos entornos Docker, pero True ayuda a ver errores
    app.run(host="0.0.0.0", port=5000, debug=False)