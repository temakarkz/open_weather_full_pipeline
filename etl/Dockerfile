FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY ../.env.local .env.local

ENV PYTHONPATH=/app

CMD ["python", "-m", "etl.app.extract_openweather"]
