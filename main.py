# Chad Verbus
# CSC325 - Python
# 10292025

import os
import re
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
            print(white_output("VPHS is shutting down. Goodbye!"))
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
            output("python_funct_cheatsheet.txt")
        case "if":
            output("python_if_statement.txt")
        case "match":
            output("python_match_statement.txt")
        case "python":
            output("python_python_general.txt")
        case "input":
            output("python_input_cheatsheet.txt")
        case "regex":
            output("python_regex_cheatsheet.txt")
        case "sqlite":
            output("python_sqlite_cheatsheet.txt")
        case "variables":
            output("python_variables_cheatsheet.txt")
        case _:
            print(gray_output("For help, type 'help', else quit, or type q followed by enter to exit."))


def output(someFile):
    cnt :int = 0
    with open(someFile, "r") as file:
        lines = file.readlines()
    for line in lines:
        #regex func goes here
        mod_output = parse_titles(line)
        print(green_output(mod_output))
        cnt += 1
        if cnt == 17:
            getInput = input(gray_output("Press enter to continue or type 'q' to quit:"))
            if getInput == 'q' or getInput == 'quit' or getInput == 'exit':
                break
            else:
                cnt = 0
            print(line)

# NOT working
def parse_titles(someLine):
    title_regex = r"\*\*.*\*\*"
    title_match = re.search(title_regex, someLine)
    if title_match:
        return bold_output(gray_output(someLine))
    else:
        return someLine

def green_output(someData) -> str:
    GREEN = "\x1b[32m"
    processedData = GREEN + someData + GREEN
    return processedData

def white_output(someData) -> str:
    WHITE = "\x1b[37m"
    processedData = WHITE + someData + WHITE
    return processedData

def gray_output(someData) -> str:
    GRAY = "\x1b[37m"
    processedData = GRAY + someData + GRAY
    return processedData

def bold_output(someData) -> str:
    BOLD = "\x1b[1m"
    processedData = BOLD + someData + BOLD
    return processedData

def reset_output(someData) -> str:
    RESET = "\x1b[0m"
    processedData = RESET + someData + RESET
    return processedData


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
