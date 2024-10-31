from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta
import time


def start_and_get_token():
    print("Token: asdf")


def parsed_pcbdoc():
    print("Start parsing pcbdoc.")


def upload_files_to_minio():
    print("Upload files to minio.")


def generate_data():
    print("Start generate data.")


def combined_data():
    print("Start combining plotly.js.")


def post_pcb_info():
    print("Post pcb-info.")


default_args = {
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    'demo',
    default_args=default_args,
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["demo"]
) as dag:

    start_task = PythonOperator(
        task_id='start_and_get_token',
        python_callable=start_and_get_token,
    )

    task2 = PythonOperator(
        task_id="parsed_pcbdoc",
        python_callable=parsed_pcbdoc
    )

    task3 = PythonOperator(
        task_id="upload_files_to_minio",
        python_callable=upload_files_to_minio
    )

    task4 = PythonOperator(
        task_id="generate_data",
        python_callable=generate_data
    )

    task5 = PythonOperator(
        task_id="combined_ploty_data",
        python_callable=combined_data
    )

    task6 = PythonOperator(
        task_id="post_pcb_info",
        python_callable=post_pcb_info
    )

    end_task = DummyOperator(
        task_id="end_task"
    )
    start_task >> task2 >> task3 >> task4 >> task5 >> task6 >> end_task
