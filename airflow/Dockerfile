FROM apache/airflow:2.9.3

USER root
RUN apt-get update && apt-get install -y vim

USER airflow
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags/ /opt/airflow/dags/
COPY plugins/ /opt/airflow/plugins/
