from config import ri

def status():
    status = ri("Input Status (O:On Progress, F: Finish, P: Plan, C: Canceled): ").strip().lower()
    if status == "o":
        status_text = "On Progress"
        progress = ri("Progress: ")
        if not progress.endswith("%"): #Check if the % is present or typed by the user or not
            progress += "%"
    elif status == "f":
        status_text = "Finish"
        progress = "100%"
    elif status == "p":
        status_text = "Plan"
        progress = "0%"
    elif status == "c":
        status_text = "Canceled"
        progress = "Canceled"
    else:
        status_text = "Unknown"
        progress = "-"
        print("!!!! Invalid status input, Defaulting to Unknown, update the status ASAP!")
    if progress.endswith("%"):
        # try:
        #Remove the %, and then calculate it for the bar, and re-add the %, the % on previous prompt is act as a flag for this
        percent_value = int(progress.strip('%'))
        filled_blocks = percent_value // 10
        empty_block = 10 - filled_blocks
        bar = "█" * filled_blocks + "." * empty_block
        progress_bar = f"[{bar}] {percent_value}%"
    else:
        progress_bar = f"[{progress}]"


def progress(progress_bar):
    progress = progress_bar 
