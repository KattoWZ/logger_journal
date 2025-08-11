from config import JSON_DIR, ri, pt, rm, JOURNAL_DIR
from core.convert import converter_entry as ce, converter_title as ct, convert
from utils.uxHelper import pause_and_clear as pcl, clear_screen as clss
# from utils.progress_status import get_progress_optional,get_status_optional
from utils.inputValidator import input_edit, input_tags
from pathlib import Path
import json
from datetime import datetime
import readline

def edit_entries():
    date_call = datetime.today()
    filename = date_call.strftime("%d-%m-%Y")
    json_path = JSON_DIR / f"{filename}.json"
    
    with open(json_path, "r") as f:
        data = json.load(f)
        
    #to print the title
    title = data[0]["Title"]
    clss()
    pt(f"{title}")
    while True:
        #Loop throught the "Content" field to grab all content
        for i, entry in enumerate(data[0]["Content"], start=1):
            
            
            tags = entry.get("Tags", "Unknown")
            journal = entry.get("Journal", "")
                       
            print(f"[entry number {i}]")        
            print(f"Tags     : {tags}")
            print(f"Journal   : {journal}")
            print("-" * 40)
    
        choice = int(ri("\nWhich entry number do you want to edit? "))-1 #-1 is because index start with 0, not 1
        edit_entry = data[0]["Content"][choice]
        
        while True:
            tags = entry.get("Tags", "Unknown")
            journal = entry.get("Journal", "")
            
            print(f"\nCurrent Tags     : {tags}")
            print(f"Current Journal   : {journal}")
            print("-" * 40)

            print("\nChoose what field do you want to edit")
            print(" (T) Tags")
            print(" (J) Journal")

            VALID_KEYS = [
                "t",
                "j",
                "tags",
                "journal"
            ]
            VISIBLE_CHOICES = [
                "Tags",
                "Journal",
                "!"
            ]
            edit_choice = input_edit("> ", valid_keys=VALID_KEYS, visible_choices=VISIBLE_CHOICES).strip().lower()
            if edit_choice == "t" or "tags":
                edit_entry['Tags'] = input_tags(f"New Tags: ") or edit_entry['Tags']
            elif edit_choice == "j" or "journal":
                edit_entry['Journal'] = input(f"New Journal: ") or edit_entry['Journal']
            else:
                clss()
                print(f"'{edit_choice}' is an Invalid option. Please enter the correct options.")
            
        
            with open(json_path, 'w') as f:
                json.dump(data, f, indent=4)
        
            #convert everything back to .log
            raw_path = JOURNAL_DIR / f"{filename}.journal"
            raw_path.chmod(0o666) #unlock the file to be writeable
            convert(json_path, raw_path)
            raw_path.chmod(0o444) #re-lock the file to be read-only
            print("\n✅ Task updated!")
            #continue edit, but start over from choosing field of the entry
            again = input("\n Do you want to edit another field of the log entry? (Y/N): ").strip().lower()
            if again != "y":
                print("\n Edit log entry session ended.")
                break

        #continue edit, but start over from choosing entry
        again_edit = input("\n Do you want to edit another log entry? (Y/N): ").strip().lower()
        if again_edit != "y":
            clss()
            print("\n Edit log session ended.")
            break

