import os
import time
import datetime

scripts = ['add_new_data.py','backup.py','exit.py','passwordGenerator.py','reload.py','remove.py','show.py']
def Verify():
    with os.scandir('scripts/') as scan_Scripts:
        foundFiles = [entry.name for entry in scan_Scripts if entry.is_file()]
        for script in scripts:
            if script in foundFiles:
                time.sleep(1)
                print(f'Found {script}!','\n')
                with open('Log.txt',"a") as log:
                    log.writelines(f'{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Found {script}\n')
            else:
                print(f'\n\n{script} is missing!')
                with open('Log.txt',"a") as log:
                    log.writelines(f'{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {script} is missing\n')
                