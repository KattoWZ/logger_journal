from core.convert import converter_title as ct
from config import LOG_DIR, JSON_DIR, ri,pt,lt, datetime, rm
from pathlib import Path
import os
import json

def json_create():
    pt("Create Log")
    while True:
        print("Insert '!' to return to main menu")            
        filename = ri("Input file name to generate (without .log): ").lower()
        json_path = JSON_DIR / f"{filename}.json"

        if json_path.exists(): #change this to use pathlib later
            print("The file is already exists, Try a different name.")
        else:
            break #no same file name, proceed to create new file
       
    title = ri("Input title for HEADER: ").upper()
    author = ri("Input the author name: ").upper()
    timestamp = datetime.now().replace(microsecond=0)


    json_entry = [
        {
            "Title" : title,
            "Time of Creation" : f"{timestamp}",
            "Author" : author,
            "Content" : []
        }
    ]
    
    with open(json_path,"w") as file:
        json.dump(json_entry, file, indent=4)
        # print(f"\n '{doc}.txt' file sucessfully created in '{log_dir}/{doc}.txt'")

    #Convert to txt
    raw_text = ct(json_path)
    raw_path = LOG_DIR / f"{filename}.log"
    with open(raw_path, 'w', encoding='utf-8') as file:
        file.write(raw_text)
    raw_path.chmod(0o444) #lock the .log file to be read-only
#EOL create file lo
