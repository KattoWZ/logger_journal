from config import JSON_DIR
import readline

def completer(text, state):
    files = [f.name[:-5] for f in JSON_DIR.iterdir() if f.name.endswith('.json') and f.name.startswith(text)] 
    if state < len(files):
        return files[state]
    return None


def enable_autocomplete():
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

    
