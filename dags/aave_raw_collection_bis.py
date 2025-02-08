from airflow.providers.docker.operators.docker import DockerOperator
from airflow import DAG
from datetime import datetime

with DAG(
    dag_id="aavev3-raw-collection",
    start_date=datetime(2025, 3, 30),
) as dag:
    events_collector = DockerOperator(
        image="louilat/aavev3-raw-events-collector",
        task_id="task-one",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
    )

    events_decoder = DockerOperator(
        image="louilat/aavev3-raw-events-decoder",
        task_id="task-two",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
    )

    balances_collector = DockerOperator(
        image="louilat/aavev3-raw-balances-collector",
        task_id="task-three",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
    )

    events_collector >> events_decoder >> balances_collector
