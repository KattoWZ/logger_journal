from utils.uxHelper import clear_screen as clss, pause
from config import  LOG_DIR, ri, pt
import os

#listing existing log file
def list_log():
    clss()
    pt("Log List")
    if not os.path.exists(LOG_DIR): #check if the log/ dir is exist, and create the dir if missing or not exist
        os.makedirs(LOG_DIR)
        print("`{LOG_DIR}/` is missing, created the directory\n")

    files = [f for f in os.listdir(LOG_DIR) if f.endswith(".txt") or f.endswith(".log")] 

    if files:
        print("Available log files: ")
        for f in files:
            print(f" - {f}")
        pause()
            # print("\n")
    else:
        print("No log files found yet. \n")
    print("===============================")
#EOL List function
