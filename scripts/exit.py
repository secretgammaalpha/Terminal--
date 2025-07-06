import os
import time
def exit_and_save():
    print('Exiting...')
    os.remove('Password.json')
    time.sleep(2)
    os.system('cls')