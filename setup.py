import os
import requests
import shutil
from pathlib import Path
import time
import json
from scripts.backup import backup
from scripts.reload import reload

def downloading_and_installing():
    os.system('cls')
    print('Installation Set-up')
    global Install_directory
    Install_directory = str(input("Installation Directory: "))
    global setting0
    setting0 = {"INSTALL_DIR":Install_directory}
    # Configuration
    DOWNLOAD_URL = 'https://github.com/secretgammaalpha/Terminal--/archive/refs/tags/2.01.zip'
    TEMP_DOWNLOAD_DIR = 'C:/Windows/Temp/temp_download'
    INSTALL_DIR = Install_directory
    ZIP_FILE_PATH = os.path.join(TEMP_DOWNLOAD_DIR, '2.0.zip')
    
    
    def create_directory(path):
        """Create directory if it doesn't exist"""
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            print(f"Error creating directory {path}: {e}")
            return False

    def download_file():
        """Download the file from GitHub"""
        try:
            # Create temp directory if it doesn't exist
            if not create_directory(TEMP_DOWNLOAD_DIR):
                return False

            print(f"Downloading from {DOWNLOAD_URL}...")
            response = requests.get(DOWNLOAD_URL, stream=True, timeout=30)
            
            # Check if the request was successful
            response.raise_for_status()  # Will raise HTTPError for bad status codes

            # Save the file
            with open(ZIP_FILE_PATH, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # Filter out keep-alive chunks
                        f.write(chunk)
            
            print(f"File successfully downloaded to {ZIP_FILE_PATH}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"Download failed: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error during download: {e}")
            return False

    def install_file():
        """Extract the downloaded ZIP file"""
        try:
            # Check if the zip file exists
            if not os.path.exists(ZIP_FILE_PATH):
                print("Downloaded ZIP file not found!")
                return False

            # Create installation directory if it doesn't exist
            if not create_directory(INSTALL_DIR):
                return False

            print(f"Extracting to {INSTALL_DIR}...")
            shutil.unpack_archive(ZIP_FILE_PATH, INSTALL_DIR)
            print("Extraction completed successfully!")
            return True
            
        except shutil.ReadError as e:
            print(f"Failed to extract ZIP file: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error during extraction: {e}")
            return False

    def cleanup():
        """Remove temporary files"""
        try:
            if os.path.exists(ZIP_FILE_PATH):
                os.remove(ZIP_FILE_PATH)
                print("Temporary files cleaned up")
        except Exception as e:
            print(f"Error during cleanup: {e}")

    # Execute the process
    if download_file():
        if install_file():
            print("Installation completed successfully!")
            time.sleep(2)
        else:
            print("Installation failed")
            time.sleep(2)
    else:
        print("Download failed - installation aborted")
        time.sleep(2)
    
    cleanup()

def setup_settings():
    os.system('cls')
    fileName = str(input('select saving file name(without file extension): '))
    setting1 = {"file_name":fileName}
    time.sleep(1)
    with open(f'{Install_directory}/Terminal---2.01/scripts/Settings.json',"w") as set:
        json.dump({},set,indent=4)
    with open(f'{Install_directory}/Terminal---2.01/scripts/Settings.json',"r") as set:
        content = json.load(set)
    content["default_settings"]= setting0
    content["user_settings"] = setting1
    with open(f'{Install_directory}/Terminal---2.01/scripts/Settings.json',"w") as set:
        json.dump(content,set,indent=4)
    time.sleep(1)
    print('\n\nSaved!\n\n')
    with open('Password.json',"w") as f:
        json.dump({},f,indent=4)
    time.sleep(1)
    print('\n\nSaved!\n\n')
    time.sleep(2)
    backup.LoadFileName()
    backup.compress()
    reload()


if __name__ == '__main__':
    downloading_and_installing()
    setup_settings()
    