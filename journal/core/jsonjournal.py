from config import  JOURNAL_DIR, ri, pt, jt, rm, JSON_DIR
from utils.uxHelper import pause_and_clear as pclss
from datetime import datetime
from pathlib import Path
from core.convert import converter_entry as ce, converter_title as ct
import uuid
import json
import os
import readline


def json_create():
    author = ri("Input Author name or callsign or code: ").upper()
    title_date = datetime.now().strftime("%d-%m-%Y")
    clock_now = datetime.now().strftime("%H:%M:%S")
    json_tempt = [
        {
            "Title" : f"JOURNAL {title_date}",
            "Time of Creation" : f"{title_date} {clock_now}",
            "Author" : author,
            "Content" : []
        }
    ]

    filename = f"journal_{title_date}"
    json_path = JSON_DIR / f"{filename}.json"
    with open(json_path, "w") as file:
        json.dump(json_tempt, file, indent=4)

    raw_text = ct(json_path)
    raw_path = JOURNAL_DIR / f"{filename}.txt"
    with open(raw_path, 'w', encoding='utf-8') as file:
        file.write(raw_text)

def json_update():
    #Autocomplete function
    def completer(text, state):
        files = [f.name for f in JSON_DIR.iterdir() if f.name.startswith(text)]
        if state < len(files):
            return files[state]
        return None
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")
    #load the created file
    input_name = ri("Input filename: ").strip().lower()
    filename = f"{input_name}"
    json_path = JSON_DIR / f"{filename}"

    with open(json_path, "r") as file:
        data = json.load(file)

    # Create the new journal entry
    raw_tags = ri("Input tags here (Seperate with commas for multiple tags): ").lower()
    tags = [tag.strip() for tag in raw_tags.split(",") if tag.strip()]
    journal = ri("Input the journal: ")
    new_entry = {
        "UUID" : str(uuid.uuid4()),
        "Clock" : datetime.now().strftime("%H:%M:%S"),
        "Tags" : tags,
        "Journal" : journal
    } 

    data[0]["Content"].append(new_entry)

    with open(json_path,"w") as file:
        json.dump(data, file, indent=4)

    if filename.endswith(".json"):
        filename = filename[:-5] + ".txt"
    
    raw_text = ce(json_path)
    raw_path = JOURNAL_DIR / f"{filename}"
    with open(raw_path, 'a', encoding='utf-8') as file:
        file.write(raw_text)

    
    
