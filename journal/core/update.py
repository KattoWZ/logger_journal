import uuid
import json
from config import JOURNAL_DIR, ri, pt, datetime, JJSON_DIR
from journal.core.convert import converter_entry
from utils.inputValidator import input_menu
from utils.uxHelper import pause_and_clear as psc, clear_screen as clss

#updating existing Journal file
def update_journal():
    print("Insert '!' to return to main menu")            
    pt("Journal Updater")
    date_call = datetime.today()
    filename = date_call.strftime("%d-%m-%Y")
    file_path = JOURNAL_DIR /  f"{filename}.journal"
    json_path = JJSON_DIR /  f"{filename}.json"
    
    #check if file exists
    if not file_path.exists():
        print(f"Journal file '{filename}.journal' not found in '{JOURNAL_DIR}/' directory")
        print("Please create the journal file first before updating.")
        psc()
        return #Don't continue, just exit the function
    print(f"journal file found! Now updating '{filename}.journal'...")
    
    # Open JSON and read it
    with open(json_path,"r") as file:
        data = json.load(file)

    while True:
        pt("\nAdding journal entry")
        entry_id = str(uuid.uuid4())
        TAGS_OPTION = ["Issue","Notes","!"]
        tags = input_menu("Input tags: ", valid_keys=TAGS_OPTION, visible_choices=TAGS_OPTION)
        journal = ri("Input the journal: ")
        clock = datetime.now()
        timestamp = clock.strftime("%H:%M:%S")

        json_entry = {
                "UUID" : entry_id,
                "Clock" : timestamp,
                "Tags" : tags,
                "Journal" : journal
            }
        data[0]["Content"].append(json_entry)
        
        with open(json_path,"w") as file:
            json.dump(data, file, indent=4)
        
        # Convert to raw text
        if filename.endswith(".json"):
            filename = filename[:-5] + ".journal"
        raw_text = converter_entry(json_path)
        file_path.chmod(0o666) #unlock the file to be writeable
        with open(file_path, "a") as file:
            file.write(raw_text)
        file_path.chmod(0o444) #re-lock the file to be read-only
        print(f"\n Log file updated")
        again = input("\n Do you want to add another log entry? (Y/N): ").strip().lower()
        if again != "y":
            clss()
            print("\n Log update session ended.")
            break
        
#EOL Updating journal funtion        

