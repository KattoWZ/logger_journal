from utils.inputValidator import reqInput as ri, ReturnToMenu as rm
from utils.titleUI import print_title as pt, logTitle as lt
from datetime import datetime
from pathlib import Path
import os
#Function to scan the root folder if the default path is not met
def find_project_root(marker="main.py"):
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / marker).exists():
            return current
        current = current.parent
    raise FileNotFoundError("Project root not found")

#Get the path of the current script's dir
BASE_DIR = find_project_root()

#Define logs dir
LOG_DIR = BASE_DIR / "logs"

#Define json dir
JSON_DIR = BASE_DIR / "json"

#Define utils dir
utils_dir = BASE_DIR / "utils"
