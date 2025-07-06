from scripts.exit import exit_and_save
import time
import os
dev = True
def reload():
    exit_and_save()
    time.sleep(2)
    os.system('cls')
    if dev:
        os.system('python main.py')
    else:os.system('main.exe')