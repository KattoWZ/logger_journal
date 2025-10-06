from pathlib import Path

from config import JOURNAL_DIR, pt, rm,JJSON_DIR
from utils.uxHelper import clear_screen as clss
from utils.inputValidator import input_menu
from core.quit import quit_program as qp

from journal.core.create import create_journal as jc
from journal.core.update import update_journal as ju
from journal.core.edit import edit_entries as ee
from journal.core.convert import convert_whole as cw


def main():
    Path(JOURNAL_DIR).mkdir(parents=True, exist_ok=True)
    Path(JJSON_DIR).mkdir(parents=True, exist_ok=True)
    MENU_ACTIONS = {
        "n" : jc,
        "new journal" :jc,
        "update journal":ju,
        "u" : ju,
        "q" : qp,
        "quit" : qp,
        "e" : ee,
        "edit" : ee,
        "c" : cw,
        "convert json to journal" : cw
    }

    while True:
        try:
            pt("JOURNALING SYSTEM by KattoWilkatz")
            print(" "*10 +  "MAIN MENU")
            print("Insert '!' to return to main menu")            
            print("\n (N) Create New Journal")
            print(" (U) Update Journal")
            print(" (E) Edit Today's Journal")
            print(" (Q) Quit Program")

            VISIBLE_OPTIONS = [
                "New Journal",
                "Update Journal",
                "Quit",
                "Edit",
                "Convert json to journal"
            ]

            choice = input_menu("> ", valid_keys=MENU_ACTIONS, visible_choices=VISIBLE_OPTIONS).strip().lower()
            action = MENU_ACTIONS.get(choice)

            if action:
                action()
            else:
                print("Invalid option. Please enter the correct options.")
        except rm:
            continue
        except KeyboardInterrupt:
            print("\n Exit program, exited by user. No changes made.")
            break
                
if __name__ == "__main__":
    main()
