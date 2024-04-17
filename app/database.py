import mysql.connector
from datetime import datetime
import zipfile
import os

# Database configuration
config = {
    'user': 'root',
    'password': 'Winter.123',
    'host': '127.0.0.1',
    'database': 'nodeodm_results',
}

def get_database_connection():
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        exit(1)

# Function to insert a new job record
def insert_job(cursor):
    add_job = ("INSERT INTO odm_jobs (status, date_created) VALUES (%s, %s)")
    job_data = ('processing', datetime.now())
    cursor.execute(add_job, job_data)
    job_id = cursor.lastrowid
    # cnx.commit()
    return job_id

# Function to update the job status and completion date
def update_job(cursor, job_id, status):
    update_job_status = ("UPDATE odm_jobs SET status = %s, date_completed = %s WHERE job_id = %s")
    job_data = (status, datetime.now(), job_id)
    cursor.execute(update_job_status, job_data)
    # cnx.commit()

# Function to extract ZIP and insert output metadata
def extract_and_store_output(job_id, zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("output")
        # Iterate over each file in the extracted folder
        for root, dirs, files in os.walk("output"):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                insert_output(job_id, file, file_path, file_size)
        # Clean up extracted files if you no longer need them here

# Function to insert a record into odm_outputs for each extracted file
def insert_output(cursor, job_id, file_name, file_location, file_size):
    add_output = ("INSERT INTO odm_outputs (job_id, file_type, file_name, file_location, file_size, date_created) VALUES (%s, %s, %s, %s, %s, %s)")
    file_type = 'unknown'  # Determine the file type based on your logic
    output_data = (job_id, file_type, file_name, file_location, file_size, datetime.now())
    cursor.execute(add_output, output_data)
    # cnx.commit()

def close_resources(cursor, cnx):
    if cursor:
        cursor.close()
    if cnx:
        cnx.close()
