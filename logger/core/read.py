import subprocess
import shutil
from pathlib import Path
from config import LOG_DIR
from utils.inputValidator import input_menu, input_filename
from utils.titleUI import print_title as pt
from utils.uxHelper import clear_screen as cl

def read_log():
    
    while True:
        VALID_OPTIONS = {
            "n" : "nano",
            "m" : "micro",
            "g" : "gedit"
            
        }
        VISIBLE_OPTIONS = ["Nano", "Micro", "Gedit", "!"]
        filename = input_filename("Insert file name : ")
        file_path = LOG_DIR / f"{filename}.txt"
    
        print(" "*10 +  "Choose Editor")
        print("\n (N) Nano")
        print(" (M) Micro")
        
        choice = input_menu("> ", valid_keys=VALID_OPTIONS, visible_choices=VISIBLE_OPTIONS).strip().lower()
        # editor = editor_opt.get(choice)
    
        if shutil.which(choice) is None:
            print(f"Editor '{editor}' is not installed.")
            return
    
        try:
            subprocess.run([choice, file_path])
        except Exception as e:
            print(f"Something went wrong: {e}")

        again = input_menu("\n Do you want to edit another file? (Y/N): ",valid_keys=["y","n","yes","no"], visible_choices=["Yes","No"]).strip().lower()
        if again not in ("y","yes"):
            print("\n session ended.")
            cl()
            break
