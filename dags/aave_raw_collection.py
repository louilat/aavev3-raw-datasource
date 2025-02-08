from pendulum import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)

with DAG(
    dag_id="aavev3-raw-collection",
    schedule="@once",
    start_date=datetime(2025, 3, 30),
) as dag:
    events_collector = KubernetesPodOperator(
        namespace="projet-datalab-group-jprat",
        image="louilat/aavev3-raw-events-collector",
        cmds=["python3", "main_etl.py"],
        name="raw_events_collection",
        task_id="task-one",
        is_delete_operator_pod=True,
        get_logs=True,
    )

    events_decoder = KubernetesPodOperator(
        namespace="projet-datalab-group-jprat",
        image="louilat/aavev3-raw-events-decoder",
        cmds=["python3", "main_etl.py"],
        name="raw_events_decoding",
        task_id="task-two",
        is_delete_operator_pod=True,
        get_logs=True,
    )

    balances_collector = KubernetesPodOperator(
        namespace="projet-datalab-group-jprat",
        image="louilat/aavev3-raw-balances-collector",
        cmds=["python3", "main_etl.py"],
        name="raw_balances_collection",
        task_id="task-three",
        is_delete_operator_pod=True,
        get_logs=True,
    )

    events_collector >> events_decoder >> balances_collector