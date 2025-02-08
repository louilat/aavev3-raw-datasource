from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
import time

def task_one():
    print("Julius")
    time.sleep(10)

def task_two():
    print("Julius Du Parc")
    time.sleep(10)

def task_three():
    print("Julius Du Parc Au Loup")
    time.sleep(10)

with DAG(
    dag_id="experiment",
    start_date=datetime(2025, 3, 30),
) as dag:
    t1 = PythonOperator(
        task_id="t1",
        python_callable= task_one,
    )
    
    t2 = PythonOperator(
        task_id="t2",
        python_callable=task_two,
    )

    t3 = PythonOperator(
        task_id="t3",
        python_callable=task_three,
    )

    t1 >> t2 >> t3
    

