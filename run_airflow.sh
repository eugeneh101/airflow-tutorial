# Stolen... I mean copied from https://airflow.apache.org/docs/apache-airflow/stable/start.html

AIRFLOW_VERSION=2.8.4

# Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
# See above for supported versions.
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.8.4 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.8.4/constraints-3.8.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# starts up the Airflow server
airflow standalone