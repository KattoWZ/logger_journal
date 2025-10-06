import json
from datetime import datetime, date
from config import  JOURNAL_DIR, ri, pt, JJSON_DIR
from utils.uxHelper import pause_and_clear as pclss
from journal.core.convert import converter_title

#creating a journal file
def create_journal():
    pt("Create Journal")
    while True:
        print("Insert '!' to return to main menu")            
        date_call = date.today()
        filename = date_call.strftime("%d-%m-%Y") 
        file_path = JOURNAL_DIR / f"{filename}.journal"
        json_path = JJSON_DIR / f"{filename}.json"

        if json_path.exists():
            print("The journal file is already exists, you already made one today.")
            pclss()
            return
        else:
            #no same file name, proceed to create new file
            break 
       
    author = ri("Input the author name: ").upper()
    timestamp = datetime.now().replace(microsecond=0)

    json_entry = [
        {
            "Title" : f"JOURNAL {filename}",
            "Date of Creation" : f"{timestamp}",
            "Author" : author,
            "Content" : []
        }
    ]

    with open(json_path,"w") as file:
        json.dump(json_entry, file, indent=4)
    
    # Convert to raw text
    raw_text = converter_title(json_path)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(raw_text)
    file_path.chmod(0o444) #lock the .journal file to be read-only
#EOL create journal file
