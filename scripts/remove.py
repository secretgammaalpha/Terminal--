import json
class remove():
    def removeall():
        with open('Password.json',"r") as f:
            content = json.load(f)
        content = {
            }
        with open('Password.json',"w")as f:
            json.dump(content,f,indent=4)
        print("\nAll data cleared!\n")
    def selremove():
        platform = str(input("Select Platfrom: ")).lower()
        with open('Password.json',"r") as f:
            content = json.load(f)
        del content[platform]
        with open('Password.json',"w")as f:
            json.dump(content,f,indent=4)
        print(f'\n{platform} is removed!\n')