import os
import socket
import time
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def print_env_vars():
    keys = str(os.environ.keys()).replace("', '", "'|'").split("|")
    for key in sorted(keys):
        print(key)


def print_airflow_cfg():
    with open(f"{os.environ['HOME']}/airflow/airflow.cfg", "r") as airflow_cfg:
        file_contents = airflow_cfg.read()
        print(f"\n{file_contents}")


def get_data():
    time.sleep(60)
    return os.getpid(), socket.gethostname()


dag = DAG(
    os.path.basename(__file__).replace(".py", ""),  # "massively-parallel-dag",
    description="Massive fanout",
    schedule_interval=None,
    # schedule_interval="*/10 * * * *",
    start_date=datetime(2017, 3, 20),
    catchup=False,
    is_paused_upon_creation=False,
    tags=["tutorial"],
)

dummy_operator = DummyOperator(task_id="dummy_task", retries=3, dag=dag)
list_python_packages_operator = BashOperator(
    task_id="list_python_packages", bash_command="python3 -m pip list"
)
get_env_vars_operator = PythonOperator(
    task_id="get_env_vars_task", python_callable=print_env_vars
)
get_airflow_cfg_operator = PythonOperator(
    task_id="get_airflow_cfg_task", python_callable=print_airflow_cfg
)

for i in range(10):
    data_operator = PythonOperator(
        task_id=f"hello_task_{i}", python_callable=get_data, dag=dag
    )
    [
        dummy_operator,
        list_python_packages_operator,
        get_env_vars_operator,
        get_airflow_cfg_operator,
    ] >> data_operator
