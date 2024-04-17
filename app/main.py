from nodeodm import *
from database import *

# Example usage
nodeodm_url = 'http://localhost:3000'
image_paths = ['C:/Users/dipam/NodeODMProject/odm_data_aukerman-master/images/image1.jpg', 'C:/Users/dipam/NodeODMProject/odm_data_aukerman-master/images/image2.jpg', 'C:/Users/dipam/NodeODMProject/odm_data_aukerman-master/images/image3.jpg', 'C:/Users/dipam/NodeODMProject/odm_data_aukerman-master/images/image4.jpg','C:/Users/dipam/NodeODMProject/odm_data_aukerman-master/images/image5.jpg', 'C:/Users/dipam/NodeODMProject/odm_data_aukerman-master/images/image6.jpg']
download_path = 'C:/Users/dipam/NodeODMProject/downloaded_results.zip'

try:
    cnx = get_database_connection()
    cursor = cnx.cursor()
    task_uuid = initialize_task(nodeodm_url)
    
    if task_uuid:
        print(f"Task initialized, UUID: {task_uuid}")
        upload_images_to_task(nodeodm_url, task_uuid, image_paths)
        print("Images uploaded to task.")
        commit_task(nodeodm_url, task_uuid)
        print("Task committed for processing.")
        task_status = check_task_status(nodeodm_url, task_uuid)
        
        if task_status == 'COMPLETED':
            download_task_results(nodeodm_url, task_uuid, download_path)
            job_id = insert_job(cursor)
            extract_and_store_output(cursor, job_id, download_path)
            update_job(cursor, job_id, 'completed')
            print("Database Updated")
    else:
        print("Failed to initialize task.")
        
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    close_resources(cursor, cnx)
