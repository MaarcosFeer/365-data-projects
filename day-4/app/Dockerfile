FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

# CAMBIO: Agregamos --default-timeout=1000 para conexiones lentas
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]