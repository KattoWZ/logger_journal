from config import  LOG_DIR, ri, pt, JSON_DIR
from utils.inputValidator import input_filename
from utils.uxHelper import clear_screen as clss
from pathlib import Path

#Delete Program
def delete():
    print("Insert '!' to return to main menu")            
    pt("Purge the FILE")
    filename = input_filename("Insert the name of the file to be removed: ", JSON_DIR).strip().lower()
    file_path = LOG_DIR / f"{filename}.log"
    json_path = JSON_DIR / f"{filename}.json"
    if file_path.exists() and json_path.exists():
        print("\n===============================")
        print(f"Log file '{filename}.log' is FOUND")
        print("===============================")
    else:
        print("\n===============================")
        print(f"Log file '{filename}.log' is NOT FOUND")
        print("===============================")
        return #exit the funtion to let user to check the lists
    delConfirmation = ri(f"Are you sure to remove the {filename}.txt file? (Y/N): ").strip().lower()
    if delConfirmation == 'y':
        file_path.unlink()
        json_path.unlink()
        clss()
        print("\n===============================")
        print(f"'{filename}.log' has been removed")
        print("===============================")
    else:
        print("\n Canceling")
        return #canceling and exitting the funtion    
#EOL Delete Program
