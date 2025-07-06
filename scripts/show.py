import json
file = 'Password.json'

class show():
    def passwd():
        with open(file,"r") as f:
            content = json.load(f)
        platform = str(input("Select platform: ")).lower()
        print(content[platform]['password'])
    def email():
        with open(file,"r") as f:
            content = json.load(f)
        platform = str(input("Select platform: ")).lower()
        print(content[platform]['email'])
    def all():
        with open(file,"r") as f:
            content = json.load(f)
        platform = str(input("Select platform: ")).lower()
        print(content[platform])