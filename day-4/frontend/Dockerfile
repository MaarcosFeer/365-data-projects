FROM python:3.9-slim

WORKDIR /app

# Instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# Exponemos el puerto de Streamlit
EXPOSE 8501

# Comando para iniciar Streamlit
# --server.address=0.0.0.0 es obligatorio en Docker
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]