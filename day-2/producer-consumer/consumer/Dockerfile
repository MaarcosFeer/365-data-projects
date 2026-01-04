FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /producer-consumer
COPY consumer.py .
CMD ["python", "consumer.py"]