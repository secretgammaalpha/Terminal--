import os
import shutil
import time
import json
class backup():
    def LoadFileName():
        with open('Settings.json',"r") as set:
            content = json.load(set)
        global filename
        filename = content["SSF"]["file name"]
    def decompress():
        os.rename(f'{filename}.docx',f'{filename}.zip')
        time.sleep(3)
        shutil.unpack_archive(f'{filename}.zip','C:/Windows/Temp/temp_PasswdManager1.1/')
    def compress():
        backup.decompress()
        shutil.copy('Password.json', 'C:/Windows/Temp/temp_PasswdManager1.1/')
        shutil.make_archive(f'{filename}','zip','C:/Windows/Temp/temp_PasswdManager1.1/')
        os.rename(f'{filename}.zip',f'{filename}.docx')
        shutil.rmtree('C:/Windows/Temp/temp_PasswdManager1.1/')
        print('backup is Done!')
    def on_start_decompress():
        os.rename(f'{filename}.docx',f'{filename}.zip')
        print('unpacking...')
        shutil.unpack_archive(f'{filename}.zip','C:/Windows/Temp/temp_PasswdManager1.1/')
        time.sleep(2)
        print('copying...')
        shutil.copy('C:/Windows/Temp/temp_PasswdManager1.1/Password.json','C:/Users/Admin/Documents/PythonProjects/PasswordManager2.0/')
        time.sleep(2)
        os.rename(f'{filename}.zip',f'{filename}.docx')
        print('cleaning...')
        shutil.rmtree('C:/Windows/Temp/temp_PasswdManager1.1/')
        time.sleep(2)
        print('Done!')
        time.sleep(3)
        
        