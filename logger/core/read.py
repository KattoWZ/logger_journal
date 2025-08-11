from config import LOG_DIR,ri
from pathlib import Path
from utils.titleUI import print_title as pt
import subprocess
import shutil
from utils.uxHelper import clear_screen as cl

def read_log():
    
    while True:
        editor_opt = {
            "n" : "nano",
            "m" : "micro",
            "g" : "gedit"
            
        }
        filename = ri("Insert file name : ")
        file_path = log_dir / f"{filename}.txt"
    
        print(" "*10 +  "Choose Editor")
        print("\n (N) Nano")
        print(" (M) Micro")
        
        choice = ri("> ").strip().lower()
        editor = editor_opt.get(choice)
    
        if shutil.which(editor) is None:
            print(f"Editor '{editor}' is not installed.")
            return
    
        try:
            subprocess.run([editor, file_path])
        except Exception as e:
            print(f"Something went wrong: {e}")

        again = input("\n Do you want to edit another file? (Y/N): ").strip().lower()
        if again != "y":
            print("\n session ended.")
            cl()
            break
