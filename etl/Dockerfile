FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y git && apt-get clean

RUN git clone -b main https://github.com/temakarkz/open_weather_full_pipeline.git

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
