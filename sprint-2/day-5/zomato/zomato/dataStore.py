import json;

path = "database.json"

def getMenu():
    with open(path,'r') as file:
        return json.load(file);

myDB = getMenu()

def write(data):
    with open(path,'w') as file:
        json.dump(data,file)



