import clipboard 
import json
import sys
import os

#it is our database atm
STORAGE = "clipboard.json"

#creating new one if there hadn't been one 
if not os.path.exists(STORAGE):
    with open(STORAGE, 'w') as f:
        f.write("{ }")
        
#creating a dict from our json file
with open(STORAGE,'r') as f:
    READ_JSON = json.load(f)
    

def add_item(path: str,key: int, value: str) -> None: 
    with open(path, 'w') as file:
        READ_JSON[key] = value

        file.write(
             json.dumps(READ_JSON) 
            )

def list_item(file_path: str) -> None:
    print('{')
    for key,value in json.load(file_path).items():
        print(f"    {key} : {value}")
    
    print('}')

def load_item(key: str) -> None: 
    clipboard.copy(READ_JSON[key]) 


def delete_key(path, key:str) -> None: 
     with open(path, 'w') as file:
        READ_JSON.pop(key)

        file.write(
             json.dumps(READ_JSON) 
            )
        

if len(sys.argv) == 2: 
    command = sys.argv[1]

    match command:
        case "add":
            key = input('Please, give me a key \n >>> ')
            value = clipboard.paste()
            add_item(STORAGE,key = key, value = value)
        
        case "load":
            key = input('Please, give me a key \n >>> ')
            try:
                load_item(key = key)
            except:
                print("ERROR")

        case "list":
            with open(STORAGE, 'r') as file:
                list_item(file)
        
        case "delete": 
            key = input('Please, give me a key \n >>> ')
            try:
                delete_key(STORAGE,key = key)
            except: 
                print("ERROR")


        case _:
            print("ERROR")

else: 
    print('Error, you must give a command (add/ load / list)')