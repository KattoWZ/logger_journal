#Title for the program
def print_title(title, width=31, char="="):
    styled = char * width + "\n"
    styled += f"\033[1;36m{title.center(width)}\033[0m\n"
    styled += char * width

    plain = char * width + "\n"
    plain += title.center(width) + "\n"
    plain += char * width

    print(styled)
    return plain

#Title for the log file    
def logTitle(title, width=70, char="="):
    styled = char * width + "\n"
    styled += f"\033[1;36m{title.center(width)}\033[0m\n"
    styled += char * width

    plain = char * width + "\n"
    plain += title.center(width) + "\n"
    plain += char * width

    print(styled)
    return plain
