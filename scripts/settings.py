import os
import time
import json

class Settings:
    def SelectSavingFile():
        os.system('cls')
        print('\n\nSelect saving file...\n\n')
        fileName = str(input("File Name(without file extension!): "))
        time.sleep(1)
        settingsAvailable = {
            "SSF":{
                "file name":fileName
            }
        }
        with open('Settings.json',"w") as set:
            json.dump(settingsAvailable,set,indent=4)
        print('File Name Selected Sucessfuly!')
        time.sleep(3)
        os.system('cls')
    