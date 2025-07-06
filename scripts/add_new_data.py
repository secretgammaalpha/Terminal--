import json
from scripts.passwordGenerator import Generate
from scripts.backup import backup
import time

class add():
    def data():
        file = 'Password.json'
        platform = str(input("Add a platform: ")).lower()
        platform_email = str(input("Add platform e-mail: "))
        password = Generate()
        platform_data = {
            "email": platform_email,
            "password": password
        }
        with open(file,"r") as f:
            content = json.load(f)
        content[platform] = platform_data
        with open(file,"w")as f:
            json.dump(content, f, indent=4)
        print("\n\nPlatform Added!\n\n")
        print('Creating Backup...')
        time.sleep(2)
        backup.compress()
        