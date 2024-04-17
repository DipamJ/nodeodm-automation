import requests
import time
import os

def initialize_task(nodeodm_url):
    try:
        response = requests.post(f"{nodeodm_url}/task/new/init").json()
        return response.get('uuid')
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def upload_images_to_task(nodeodm_url, task_uuid, image_paths):
    for path in image_paths:
        print(path)
        assert os.path.exists(path), f"Image not found: {path}"
    files = [('images', (os.path.basename(path), open(path, 'rb'))) for path in image_paths]
    upload_url = f"{nodeodm_url}/task/new/upload/{task_uuid}"
    response = requests.post(upload_url, files=files)
    print(response.text)  # Debugging response

def commit_task(nodeodm_url, task_uuid):
    commit_url = f"{nodeodm_url}/task/new/commit/{task_uuid}"
    response = requests.post(commit_url).json()
    print(response)
    
def check_task_status(nodeodm_url, task_uuid):
    while True:
        response = requests.get(f"{nodeodm_url}/task/{task_uuid}/info").json()
        print(response)
        if 'status' not in response:
            print("Task status not available. Response:", response)
            break
        status_code = response['status']['code']
        # Status codes: 10 = QUEUED, 20 = RUNNING, 30 = FAILED, 40 = COMPLETED, 50 = CANCELED
        if status_code == 40:  # COMPLETED
            print("Task completed.")
            return 'COMPLETED'
        elif status_code in [30, 50]:  # FAILED or CANCELED
            print(f"Task failed or was canceled. Status code: {status_code}")
            fetch_task_output(nodeodm_url, task_uuid)
            return 'FAILED_OR_CANCELED'        
        print(f"Task status: {status_code} - Checking again in 30 seconds.")
        time.sleep(30)

def download_task_results(nodeodm_url, task_uuid, download_path):
    response = requests.get(f"{nodeodm_url}/task/{task_uuid}/download/all.zip", stream=True)
    if response.status_code == 200:
        with open(download_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Results downloaded to {download_path}")
    else:
        print(f"Failed to download results. HTTP status code: {response.status_code}")

def fetch_task_output(nodeodm_url, task_uuid):
    output_url = f"{nodeodm_url}/task/{task_uuid}/output"
    response = requests.get(output_url)
    if response.ok:
        print("Console Output:\n", response.text)
    else:
        print("Failed to fetch console output.")
