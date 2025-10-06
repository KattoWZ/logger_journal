import json
from config import JOURNAL_DIR, JJSON_DIR
from utils.inputValidator import input_filename

def converter_title(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        filename = data[0].get("Title", "Unknown")
        time = data[0].get("Date of Creation", "Unknown")
        author = data[0].get("Author", "Unknown") 

        raw_text = (
            f"Title            : {filename}\n"
            f"Date of Creation : {time}\n"
            f"Author           : {author}\n\n"
            ">>> Begin Journal <<<\n\n"
            
        )
        
        return raw_text 
             
    except FileNotFoundError:
        return "[Error] File not found."
    except json.JSONDecodeError:
        return "[Error] Invalid JSON."
def converter_entry(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        raw_text = ""
        for entry in data[0]["Content"]:

            uuid = entry.get("UUID", "Unknown")
            clock = entry.get("Clock", "Unknown")
            tags = entry.get("Tags", "Unknown")
            journal = entry.get("Journal", "")

        raw_text = (
            f"UUID    : {uuid}\n"
            f"Clock   : {clock}\n"
            f"Tags    : {tags}\n"
            f"Journal : {journal}\n"
            "-------------------------\n"
        )
        # raw_text = f"UUID: {uuid}\nClock: {clock}\nTags: {tags}\nJournal: {journal}"
        return raw_text
            
    except FileNotFoundError:
        return "[Error] File not found."
    except json.JSONDecodeError:
        return "[Error] Invalid JSON."
    
#Both of these are special for converting .json to .journal manually
def convert(json_path, raw_path):
    #convert the header first        
    header = converter_title(json_path)
    with open(raw_path, 'w', encoding='utf-8') as file:
        file.write(header)

    #convert the entries after
    entries = converter_entry(json_path)
    with open(raw_path, 'a') as f:
        f.write(entries) 

# to convert json file into journal file
def convert_whole():
    # ea()
    filename = input_filename("Input the file to convert to .log from .json: ",JJSON_DIR).strip().lower()
    json_path = JJSON_DIR / f"{filename}.json"
    raw_path = JOURNAL_DIR / f"{filename}.journal"
    #convert the header first        
    convert(json_path, raw_path) 
    raw_path.chmod(0o444)
