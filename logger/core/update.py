from config import LOG_DIR, JSON_DIR, ri,pt,lt, datetime, rm
from utils.inputValidator import input_filename, input_status
from core.convert import converter_entry as ce
from utils.completer import enable_autocomplete
from utils.uxHelper import clear_screen as clss
from utils.progress_status import get_status, get_progress
from utils.task_lists import load_tasks, get_task_with_autocomplete
from pathlib import Path
import os
import json
import readline
import uuid

def json_update():
    # enable_autocomplete()
    input_name = input_filename("Input log name: ",JSON_DIR)
    # input_name = ri("Input log name: ").strip().lower()
    filename = f"{input_name}"
    json_path = JSON_DIR / f"{filename}.json"

    #Check if the file is exist or not, returning to main menu when not found
    if not json_path.exists():
        clss()
        print(f"Log file '{filename}.log' not found !!")
        print("Please create the log file first")
        return
    print(f"Log file '{filename}.log' found! Now updating..")

    with open(json_path,"r") as file:
        data = json.load(file)

    while True:
        #Creating or adding new log entry
        pt("Adding log entry")
        task_list=load_tasks(json_path)
        task = get_task_with_autocomplete(task_list)
        # status = get_status()
        status = input_status("Input Status: ")
        print(status)
        progress = get_progress(status)
        print(progress)
        detail = input("Input the detail(optional): ")
        timestamp = datetime.now().replace(microsecond=0)
        
        #the Entry
        json_entry = {
                "UUID" : str(uuid.uuid4()),
                "Date and Time" : f"{timestamp}",
                "Task" : task,
                "Status" : status,
                "Progress" : progress,
                "Detail" : detail
            }
        data[0]["Content"].append(json_entry)
    
        with open(json_path,"w") as file:
            json.dump(data, file, indent=4)
    
        #convert JSON to txt
        if filename.endswith(".json"):
            filename = filename[:-5] + ".log"
        raw_text = ce(json_path)
        raw_path = LOG_DIR / f"{filename}.log"
        raw_path.chmod(0o666) #unlock the file to be writeable
        with open(raw_path, "a") as file:
            file.write(raw_text)
        raw_path.chmod(0o444) #re-lock the file to be read-only
        print(f"\n Log file updated")
        again = input("\n Do you want to add another log entry? (Y/N): ").strip().lower()
        if again != "y":
            clss()
            print("\n Log update session ended.")
            break
