import os
import readline

def completer(text, state):
    files = [f for f in os.listdir() if f.startswith(text)]
    if state < len(files):
        return files[state]
    return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

filename = input("Enter filename: ")
print(f"You chose: {filename}")
