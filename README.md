# NodeODM Processing Automation

This project automates the process of uploading images to NodeODM, monitoring the job status, and handling the outputs by storing them in a MySQL database. The results are then made available through a PHP-based web interface.

## Purpose

The purpose of this project is to streamline the workflow of processing drone imagery with NodeODM and to provide a user-friendly web interface to access and download the processed outputs.

## Getting Started

### Prerequisites

- NodeODM running on `localhost:3000`
- Python 3.x installed
- MySQL Server running on `localhost`
- PHP 7.x and Apache/Nginx web server

### Installation

1. Clone the repository to your local machine or server.

   git clone https://github.com/DipamJ/nodeodm-automation



*SSH to Server Using Atom*

-	If you don't have a public key, use the following instructions to generate it (OpenSSH Client):  https://phoenixnap.com/kb/generate-ssh-key-windows-10
-	Open file ‘SSH PUBLIC key’ and save there with your name the content of your public key file (.pub can be open with notepad to see content inside). After this information has been added, please email me to add this key to the server. This will allow you to connect.
-	Install ATOM code editor
-	Install remote-ftp (by icetee) package, if not able find then install it manually 
	1. Download the atom-beautify package from GitHub(https://github.com/icetee/remote-ftp). Either via git clone or manually download it is find.
	2. Extract the package files to a temporary directory.
	3. Open a terminal window and navigate to the temporary directory.
	4. Run the instillation command if needed
	5. apm install <package_name>
	6. This will install the package and any of its dependencies.
	7. Then after installing the packages or themes you may now restart the atom text editor window.
-	Add Project (Create and select new folder. This can be created in Documents)
-	From Atom top bar > Packages > Remote FTP > Create SFTP config file
o	Example:
{
    "protocol": "sftp",
    "host": "158.101.127.212",
    "port": 22,
    "user": "ubuntu",
    "pass": "",
    "promptForPass": false,
    "remote": "/var/www/html/uas_tools",
    "local": "",
    "agent": "",
    "privatekey": "/Users/Jose Landivar/.ssh/id_rsa",
    "passphrase": "",
    "hosthash": "",
    "ignorehost": true,
    "connTimeout": 10000,
    "keepalive": 10000,
    "keyboardInteractive": false,
    "keyboardInteractiveForPass": false,
    "remoteCommand": "",
    "remoteShell": "",
    "watch": [],
    "watchTimeout": 500
}

-	From Atom top bar > Packages > Remote FTP > Toggle
-	Next to Project click on Remote > Connect

# Navigate to the cloned directory.
cd nodeodm-automation

# Install the necessary Python dependencies.
pip install -r requirements.txt

# Database Setup
-	Install MySQL workbench
-	Run the create query script 

# Running the Application
-	To start the image processing script, run:
python main.py
-	Launch the web server and place the PHP files in the web directory (e.g., htdocs for XAMPP).

# Web Interface
Access the results page at http://localhost/nodeodm_results/results.php.

Features
-	Search functionality to quickly find specific outputs.
-	Download buttons for each file to easily retrieve outputs.

# Code Structure
-	nodeodm.py: Handles the interaction with NodeODM's API, including image upload, status checks, and output downloading.
-	database.py: Contains functions related to database operations such as inserting jobs and outputs.
-	main.py: The entry point of the application, which coordinates the process flow.
-	results.php: The web interface for displaying and downloading NodeODM outputs.

#	Common Tasks
-	Adding Images: Place new images in the specified directory and run the Python script to start processing.
-	Checking Job Status: The script will print the job status to the console. For web interface, refresh the results page.
-	Downloading Outputs: Use the download buttons next to each file on the web interface.

#Documentation
For a detailed explanation of the functions and the architecture, please refer to the Documentation file.