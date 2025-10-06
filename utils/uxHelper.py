import platform
import subprocess
import shutil
#simple funtion to clear the screen
def clear_screen():
    clear_cmd = shutil.which("clear")
    if clear_cmd:
        subprocess.run([clear_cmd])
        
#pause before moving the screen
def pause(msg="Press 'Enter' to continue..."):
    input(msg)
    
#pause before moving the screen and clear the screen after prompt inserted
def pause_and_clear(msg="Press 'Enter' to contine..."):
    input(msg)
    clear_screen()
