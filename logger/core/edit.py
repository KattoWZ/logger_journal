import json
from config import LJSON_DIR, ri, pt, rm, LOG_DIR
from utils.uxHelper import pause_and_clear as pcl, clear_screen as clss
from utils.inputValidator import input_menu, input_filename
from logger.core.convert import converter_entry as ce, converter_title as ct, convert
from logger.utils.progress_status import get_progress_optional

def edit_entries():
    filename = input_filename("Input the file name: ",LJSON_DIR)
    json_path = LJSON_DIR / f"{filename}.json"
    with open(json_path, "r") as f:
        data = json.load(f)
        
    #to print the title
    title = data[0]["Title"]
    clss()
    pt(f"{title}")
    while True:
        #Loop throught the "Content" field to grab all content
        for i, entry in enumerate(data[0]["Content"], start=1):
            
            
            task = entry.get("Task", "Unknown")
            status = entry.get("Status", "")
            progress = entry.get("Progress", "-")
            detail = entry.get("Detail", "")
                       
            print(f"[entry number {i}]")        
            print(f"Task     : {task}")
            print(f"Status   : {status}")
            print(f"Progress : {progress}")
            print(f"Detail   : {detail}")
            print("-" * 40)
        
        numbers = [str(i) for i, _ in enumerate(data[0]["Content"], start=1)]
        choice = int(input_menu("\nWhich task number do you want to edit? ",valid_keys=numbers, visible_choices=numbers))-1 #-1 is because index start with 0, not 1
        edit_entry = data[0]["Content"][choice]
        
        while True:
            task = edit_entry.get("Task", "Unknown")
            status = edit_entry.get("Status", "")
            progress = edit_entry.get("Progress", "-")
            detail = edit_entry.get("Detail", "")
            
            print(f"\nCurrent Task     : {task}")
            print(f"Current Status   : {status}")
            print(f"Current Progress : {progress}")
            print(f"Current Detail   : {detail}")
            print("-" * 40)

            print("\nChoose what field do you want to edit")
            print(" (T) Task")
            print(" (S) Status and Progress")
            print(" (D) Detail")

            EDIT_OPTIONS = ["Task", "Status and Progress", "Detail","!"]
            edit_choice = input_menu("> ", valid_keys=EDIT_OPTIONS, visible_choices=EDIT_OPTIONS).strip()
            if edit_choice in ("t", "Task"):
                edit_entry['Task'] = input(f"New Task (current: {edit_entry['Task']}): ") or edit_entry['Task']
            
            elif edit_choice in ("s" ,"Status and Progress"):
                print(f"Current Status: {edit_entry['Status']}")
                STATUS_OPTION = ["On Progress", "Finish", "Plan", "Canceled","!"]
                edit_entry['Status'] = input_menu("Choose new Status (press TAB): ",valid_keys=STATUS_OPTION, visible_choices=STATUS_OPTION) or edit_entry['Status']
                print(f"New Status: {edit_entry['Status']}")
        
                print(f"Current Progress: {edit_entry['Progress']}")
                edit_entry['Progress'] = get_progress_optional(edit_entry['Status'], edit_entry['Progress'])
                print(f"New Progress: {edit_entry['Progress']}")

            elif edit_choice in ("d" , "Detail"):
                 edit_entry['Detail'] = input(f"New Detail (current: {edit_entry['Detail']}): ") or edit_entry['Detail']
                 print(f"New Detail: {edit_entry['Detail']}")
            else:
                
                print(f"'{edit_choice}' is an Invalid option. Please enter the correct options.")
            
        
            with open(json_path, 'w') as f:
                json.dump(data, f, indent=4)
        
            #convert everything back to .log
            raw_path = LOG_DIR / f"{filename}.log"
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

