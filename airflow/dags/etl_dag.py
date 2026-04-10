from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'komal',
    'start_date': datetime(2026, 4, 1),  # realistic recent date
    'retries': 1
}

with DAG(
    dag_id='etl_pipeline_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:

    run_etl = BashOperator(
        task_id='run_etl_pipeline',
        bash_command='python3 /root/project/etl/etl_pipeline.py'
    )