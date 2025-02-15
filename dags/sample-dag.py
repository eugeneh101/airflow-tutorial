import os
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def print_hello():
    return "Hello World"


dag = DAG(
    os.path.basename(__file__).replace(".py", ""),  # "sample-dag",
    description="Hello world example",
    schedule_interval="*/5 * * * *",
    start_date=datetime(2017, 3, 20),
    catchup=False,
    is_paused_upon_creation=False,
    tags=["tutorial"],
)

dummy_operator = DummyOperator(task_id="dummy_task", retries=3, dag=dag)

hello_operator = PythonOperator(
    task_id="hello_task", python_callable=print_hello, dag=dag
)

dummy_operator >> hello_operator
