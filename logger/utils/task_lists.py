from config import rm
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError
from utils.uxHelper import clear_screen as clss
import json

# Load existing tasks
def load_tasks(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    tasks = [entry.get("Task", "Unknown") for entry in data[0]["Content"]]
    return list(set(tasks))  # remove duplicates

# Main input function with autocomplete
def get_task_with_autocomplete(task_list, allow_return=True):
    task_completer = WordCompleter(task_list, ignore_case=True)
    session = PromptSession()

    class TaskValidator(Validator):
        def validate(self, document):
            text = document.text.strip()
            if not text:
                raise ValidationError(message="Task cannot be empty", cursor_position=0)

    while True:
        task = session.prompt(
            "Enter task: ",
            completer=task_completer,
            validator=TaskValidator(),
            validate_while_typing=False
        ).strip()

        if allow_return and task == "!":
            clss()
            print("\nReturning to main menu....")
            raise rm()
        return task

# Example usage
if __name__ == "__main__":
    json_path = "your_log.json"  # Change to your actual path
    task_list = load_tasks(json_path)
    selected_task = input_task_with_autocomplete(task_list)
    print(f"Selected task: {selected_task}")
