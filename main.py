# Chad Verbus
# CSC325 - Python
# 10292025

import os

# future
def init():
    pass
#main loop
def main():
    isrunning: bool = True
    while isrunning:
        getInput = input("Enter a keyword, followed by the enter key:")
        if getInput == "exit" or getInput == "q" or getInput == "quit":
            help("goodbye")
            isrunning = False
        else:
            help(getInput)

def help(name):
    match name:
        case "goodbye":
            print("VPHS is shutting down. Goodbye!")
        case "information":
            print("Sample CLI APP for CSC325: Prof Hinton: Assignment .5.1: Your First Python Application: Verbose Python Help System: Chad Verbus")
        case "help":
            display_welcome_message()
        case "q":
            isrunning = False
        case "quit":
            isrunning = False
        case "exit":
            isrunning = False
        case _:
            read_help_text(name)


def read_help_text(aType):
    match aType:
        case "def":
            display_help_text("python_funct_cheatsheet.txt")
        case "if":
            display_help_text("python_if_statement.txt")
        case "match":
            display_help_text("python_match_statement.txt")
        case "python":
            display_help_text("python_python_general.txt")
        case "input":
            display_help_text("python_input_cheatsheet.txt")
        case "regex":
            display_help_text("python_regex_cheatsheet.txt")
        case "sqlite":
            display_help_text("python_sqlite_cheatsheet.txt")
        case "variables":
            display_help_text("python_variables_cheatsheet.txt")
        case _:
            print("For help, type 'help', else quit, or type q followed by enter to exit.")


def display_help_text(aFile):
    cnt :int = 0
    with open(aFile, "r") as file:
        lines = file.readlines()
    for line in lines:
        print(line)
        cnt += 1
        if cnt == 15:
            getInput = input("Press enter to continue or type 'q' to quit:")
            if getInput == 'q' or getInput == 'quit' or getInput == 'exit':
                break
            else:
                cnt = 0
            print(line)

def display_welcome_message():
    os.system("clear")
    print("Welcome to Verbose Python Help System (VPHS).")
    print("This is the early initial stages of development. Please report any bugs or issues to Chad Verbus.")
    print("You can type key words followed by the enter key, the system will display simple text related to the keyword")
    print("\n")
    print("Working Key Words:\n")
    print("- help - displays help information")
    print("- python - what is python?")
    print("- def - functions and classes in python")
    print("- if - if statement in python")
    print("- match - match statement in python")
    print("- input - input methods in python, accept user input")
    print("- regex - regular expressions, parses patterns and searches strings")
    print("- sqlite - general interaction with a local sqlite database")
    print("- variables - variables in python")
    print("\n\n\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_welcome_message()
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
