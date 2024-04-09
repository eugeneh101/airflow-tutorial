# Airflow Tutorial
Getting started with Airflow on your (MacBook/Linux) laptop. There would be small modifications for Windows laptop.

1. Create a virtual environment: `python -m venv .venv`
    * If `virtualenv` is not installed, then install first: `pip install virtualenv`
2. Activate the virtual environment: `source .venv/bin/activate`
    * If you are Windows, it should be `.\venv\Scripts\activate`
3. Run Airflow locally: `bash run_airflow.sh`
    * Look at the printouts to see what the username and password is
    * Airflow will create a folder at `~/airflow`
4. Go to any browser (Chrome, Firefox, etc) and put this in the url: `localhost:8080` and paste in the username and password from the previous step
5. Open a new termianl, go back to the repo folder, and copy the DAGs from `dags/` for to `~/airflow/dags/` folder: `cp -r dags/ ~/airflow/dags/`
    * It took ~7 minutes for those DAGs to show up in Airflow on my computer.
6. When you are done, just do Ctrl + C in your terminal. When you want to start Airflow again, just run `airflow standalone` in the terminal.
    * If you want to get rid of all the stuff, you can delete `~/airflow` folder: `rm -rf ~/airflow`
