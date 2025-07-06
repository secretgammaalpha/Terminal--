import os
from scripts.add_new_data import add
from scripts.show import show
from scripts.backup import backup
from scripts.exit import exit_and_save
from scripts.remove import remove
from scripts.reload import reload
from verify import Verify
from scripts.settings import Settings
import time
def on_start():
    backup.on_start_decompress()
    os.system('cls')
    app()

def on_awake():
    os.system('cls')
    with open('Log.txt',"w") as log:
        log.write("")
    print('\n\nVerifying the available Data...\n\n')
    try:
        Verify()
    except Exception as e:
        print(f'Error!: {e}')
        time.sleep(5)
        exit(1)
    with open('Log.txt',"r") as log:
        content = log.read()
    if "missing" in content:
        print('Check Log.txt...!')
        time.sleep(5)
        os.system('cls')
        exit(0)
    else:
        os.system('cls')
        backup.LoadFileName()
        on_start()

helpCommands = ['cls:Clear','exit:Exiting the app','add:adding new data','show:showing data','backup:Creating a backup file','remove:removing all or the selected data','reload:Reloading the app','settings: Settings to change']

def app():
    print("\n\n\n\nWelcome Boss!\n\n")
    print("\n\nType h or help to show available commands\n\n")
    for command in helpCommands:
        print(command)
    while True:
        commandsInput = input(">>>").lower()
        if commandsInput == "cls":
            os.system("cls")
        elif commandsInput == "exit":
            exit_and_save()
            break
        elif commandsInput == "h" or commandsInput == "help":
            for command in helpCommands:
                print(command)
        elif commandsInput == "add":
            add.data()
            os.system('cls')
        elif commandsInput == "show":
            os.system('cls')
            command = input("[Show]>>>")
            if command == "passwd":
                show.passwd()
            elif command == "email":
                show.email()
            elif command == "all":
                show.all()
            else:
                print("\nCommand not found!\n")
        elif commandsInput == "reload":
            reload()
            break
        elif commandsInput == "remove":
            command = input('[Remove]>>>')
            if command == 'removeall':
                remove.removeall()
            elif command == 'selremove':
                remove.selremove()
            else:
                print("\nCommand not found!\n")
        elif commandsInput == "backup":
            backup.compress()
        elif commandsInput == "settings":
            os.system('cls')
            command = input("[Settings]>>> ")
            if command == "selfile":
                Settings.SelectSavingFile()
            else:
                print('\n\nCommand not found!\n\n')
        else:
            print("Command not available\n")

on_awake()
