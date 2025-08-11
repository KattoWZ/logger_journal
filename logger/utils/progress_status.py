from config import ri
import re

# function to get status
def get_status():
    status = ri("Input Status (O:On Progress, F: Finish, P: Plan, C: Canceled): ").strip().lower()
    if status == "o":
        return "On Progress"
    elif status == "f":
        return "Finish"
    elif status == "p":
        return "Plan"
    elif status == "c":
        return "Canceled"
    else:
        return "Unknown"
        print("!!!! Invalid status input, Defaulting to Unknown, update the status ASAP!")

# function to get progress
def get_progress(param_status):
    if param_status == "On Progress":
        progress = ri("Progress: ")
        if not progress.endswith("%"):
            progress += "%"
    elif param_status == "Finish":
        progress = "100%"
    elif param_status == "Plan":
        progress = "0%"
    elif param_status == "Canceled":
        progress = "Canceled"
    else:
        progress = "-"

    if progress.endswith("%"):
        try:
        #Remove the %, and then calculate it for the bar, and re-add the %, the % on previous prompt is act as a flag for this
            percent_value = int(progress.strip('%'))
            filled_blocks = percent_value // 10
            empty_block = 10 - filled_blocks
            bar = "█" * filled_blocks + "." * empty_block
            progress_bar = f"[{bar}] {percent_value}%"
        except ValueError:
            progress_bar = "invalid"
    else:
        progress_bar = f"{progress}"
    
    return progress_bar

# get status without restriction to blank input
def get_status_optional():
    status = input("Input Status (O:On Progress, F: Finish, P: Plan, C: Canceled): ").strip().lower()
    if status == "o":
        return "On Progress"
    elif status == "f":
        return "Finish"
    elif status == "p":
        return "Plan"
    elif status == "c":
        return "Canceled"
    else:
        return "Unknown"
        print("!!!! Invalid status input, Defaulting to Unknown, update the status ASAP!")

# get progress without restriction to blank input
def get_progress_optional(param_status, current_progress):
    if param_status == "On Progress":
        progress = input("Progress: ")
        if not progress.endswith("%"):
            progress += "%"
    elif param_status == "Finish":
        progress = "100%"
    elif param_status == "Plan":
        progress = "0%"
    elif param_status == "Canceled":
        progress = "Canceled"
    else:
        progress = "-"

    if progress == "":  
        match = re.search(r"(\d+%)", current_progress)
        percent = match.group(1) if match else "0%"
        progress = percent
    else:
        progress = progress

    if progress.endswith("%"):
        try:
        #Remove the %, and then calculate it for the bar, and re-add the %, the % on previous prompt is act as a flag for this
            percent_value = int(progress.strip('%'))
            filled_blocks = percent_value // 10
            empty_block = 10 - filled_blocks
            bar = "█" * filled_blocks + "." * empty_block
            progress_bar = f"[{bar}] {percent_value}%"
        except ValueError:
            progress_bar = "invalid"
    else:
        progress_bar = f"{progress}"
    
    return progress_bar
