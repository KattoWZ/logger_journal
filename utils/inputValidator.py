from utils.uxHelper import clear_screen as clss
from pathlib import Path
from prompt_toolkit import prompt, PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError

class ReturnToMenu(Exception):
    pass
#for general usage
def reqInput(message, choices="!", allow_return=True):
    session = PromptSession()
    completer = WordCompleter(choices, ignore_case=True) if choices else None


    class InputValidator(Validator):
        def validate(self, document):
            text = document.text.strip()

            if text == "!":
                return
            
            if not text:
                raise ValidationError(message="This field can't be empty!!!!" , cursor_position=0)

    text = session.prompt(
        message,
        completer=completer,
        validator=InputValidator(),
        validate_while_typing=False
        
    )


    if allow_return and text == "!":
        clss()
        print("\nReturning to main menu...")
        raise ReturnToMenu()
    return text

#for Inputing Filename
def input_filename(message, path:Path, allow_return=True):
    session = PromptSession()

    json_files = [f.stem for f in path.glob("*.json")] + list("!")
    completer = WordCompleter(json_files, ignore_case=True)

    class FileNameValidator(Validator):
        def validate(self, document):
            text = document.text.strip()

            if text == "!":
                return
            if not text:
                raise ValidationError(message="Filename can't be empty!", cursor_position=0)

    filename = session.prompt(
        message,
        completer=completer,
        validator=FileNameValidator(),
        validate_while_typing=False
    ).strip()

    if allow_return and filename == "!":
        clss()
        print("\nReturning to main menu...")
        raise ReturnToMenu()

    return filename

#for Status
STATUS_OPTION = ["On Progress", "Finish", "Plan", "Canceled","!"]
def input_status(message, allow_return=True):
    completer = WordCompleter(STATUS_OPTION, ignore_case=True)
    session = PromptSession()

    class StatusValidator(Validator):
        def validate(self, document):
            text = document.text.strip()
            if text == "!":
                return            
            if not text:
                raise ValidationError(message="Can't be empty !", cursor_position=0)
            if text not in STATUS_OPTION:
                raise ValidationError(message=f"'{text}' is not an option", cursor_position=0)

    status = session.prompt(
        message,
        completer=completer,
        validator=StatusValidator(),
        validate_while_typing=False
    ).strip()

    if allow_return and status == "!":
        clss()
        print("\nReturning to main menu...")
        raise ReturnToMenu()

    return status

#for main menu option
def input_menu(message, valid_keys: dict, visible_choices=None, allow_return=True):
    # Only show the "long" commands in the autocomplete
    visible_choices = visible_choices or list(set(valid_keys) - {k for k in valid_keys if len(k) <= 2}) + list("!")
    completer = WordCompleter(visible_choices, ignore_case=True)

    class MenuValidator(Validator):
        def validate(self, document):
            text = document.text.strip().lower()
            if not text:
                raise ValidationError(message="Input cannot be empty.", cursor_position=0)
            if text not in valid_keys:
                raise ValidationError(message="Invalid option. Try again.", cursor_position=0)

    session = PromptSession()
    menu = session.prompt(
        message,
        completer=completer,
        validator=MenuValidator(),
        validate_while_typing=False
    ).strip()

    if allow_return and menu == "!":
        clss()
        print("\nReturning to main menu...")
        raise ReturnToMenu()
    
    return menu
