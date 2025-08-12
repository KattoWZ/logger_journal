from utils.uxHelper import clear_screen as clss
from pathlib import Path
from prompt_toolkit import prompt, PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError
from typing import Union

class ReturnToMenu(Exception):
    pass

#for general usage, where there is no restriction for user to input any value
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

# for anything that has valid_keys declared and visible_choices declared
# valid_keys = string that is valid to run something or allowed to be inserted (can be in form of dict or list)
# visible_choices = for what will be shown on the dropdown, the string must be included on valid_keys (mostly in form of list)
# this method is to strict user to only inserting acceptable value

def input_menu(message, valid_keys: Union[list[str], dict], visible_choices: list[str] = None, allow_return: bool=True):
    
    keys_list = list(valid_keys.keys()) if isinstance(valid_keys, dict) else list(valid_keys)
    
    # Only show the "long" commands in the autocomplete
    visible_choices = visible_choices or list(set(keys_list) - {k for k in keys_list if len(k) <= 2}) + list("!")
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
