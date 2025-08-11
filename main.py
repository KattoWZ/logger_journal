from journal.main import main as journal_main
from logger.main import main as logger_main
from utils.uxHelper import clear_screen as clss
from core.quit import quit_program
from utils.inputValidator import input_menu, ReturnToMenu as rm

def main():
    clss()
    #menu actions dictionary
    MENU_ACTIONS = {
        "l" : journal_main,
        "logger program" : journal_main,
        "j" : logger_main,
        "journal program" : logger_main,
        "q" : quit_program,
        "quit" : quit_program
    }
        
    while True:
        try:
            pt("LOGGING AND JOURNALING SYSTEM by KattoWilkatz")
            print(" "*10 +  "MAIN MENU")
            print("Insert '!' to return to main menu")
            print("Type the option below or press 'Tab' to show the dropdown option")            
            print("\n (L) Run Logger Program")
            print(" (J) Run Journaling Program")
            print(" (Q) Quit")
            
        
            VISIBLE_OPTIONS=[
               "Journal Program"
               "Logger Program"
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
