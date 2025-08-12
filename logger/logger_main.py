from pathlib import Path

from config import LOG_DIR, JSON_DIR, pt, rm
from core.quit  import quit_program as qp
from utils.uxHelper import clear_screen as clss
from utils.inputValidator import input_menu

from logger.core.create import json_create as jc
from logger.core.update import json_update as ju
from logger.core.lists import list_log as ll
from logger.core.delete import delete as dl
from logger.core.export2excell import export_to_excel as ex
from logger.core.read import read_log as rd
from logger.core.entryListJSON import list_entries as le
from logger.core.edit import edit_entries as ee
from logger.core.convert import convert_whole as cw


def main():
    clss()
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
    Path(JSON_DIR).mkdir(parents=True, exist_ok=True)
    
    #menu actions dictionary
    MENU_ACTIONS = {
        "n" : jc,
        "new" : jc,
        "u" : ju,
        "update" : ju,
        "e" : ee,
        "edit" : ee,
        "l" : ll,
        "list log" : ll,
        "q" : qp,
        "quit" : qp,
        "x" : ex,
        "export to excell" : ex,
        "d" : dl,
        "delete" : dl,
        "r" : rd,
        "read" :rd,
        "le": le,
        "list entries" : le,
        "cw" : cw,
        "convert json to log" :cw,
        "!" : rm
    }
        
    while True:
        try:
            pt("LOG SYSTEM by KattoWilkatz")
            print(" "*10 +  "MAIN MENU")
            print("Insert '!' to return to main menu")
            print("Type the option below or press 'Tab' to show the dropdown option")            
            print("\n (N) Create New Log")
            print(" (U) Update Exisiting Log")
            print(" (R) Read Exisiting Log")
            print(" (E) Edit Exisiting Log")
            print(" (L) Show List Existing Logs")
            print(" (X) Export to excel[WIP_don't use]")
            print(" (D) Delete files")
            print(" (Q) Quit")
            print(" (LE) lists entries")
            print(" (CW) Convert JSON to log")
        
            VISIBLE_OPTIONS=[
                "New",
                "Update",
                "Edit",
                "Delete",
                "List log",
                "List entries",
                "Quit",
                "Export to excell",
                "Convert json to log",
                "!"
            ]
            
            choice = input_menu("> ", valid_keys=MENU_ACTIONS, visible_choices=VISIBLE_OPTIONS).strip().lower()
            action = MENU_ACTIONS.get(choice)
        
            if action:
                action() #Call the corresponding function!
            
        except rm:
            continue
        except KeyboardInterrupt:
            print("\n Exit program, exited by user. No changes made.")
            break
if __name__ == "__main__":
    main()
