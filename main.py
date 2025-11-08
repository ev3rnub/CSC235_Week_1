# Chad Verbus
# CSC325 - Python
# 11082025




# interact os libs so we can clear the terminal screen etc.
import os

#main loop
def main():
    isrunning: bool = True
    while isrunning:
        getInput = input(blue_output("Enter a keyword, followed by the enter key:"))
        if getInput == "exit" or getInput == "q" or getInput == "quit":
            help("goodbye")
            isrunning = False
        else:
            help(getInput)

# helper function
def help(name):
    match name:
        case "goodbye":
            print(blue_output("VPHS is shutting down. Goodbye!"))
        case "information":
            print(blue_output("Sample CLI APP for CSC325: Prof Hinton: Assignment .5.1: Your First Python Application: Verbose Python Help System: Chad Verbus"))
        case "help":
            display_welcome_message()
        case "takeNote":
            take_note()
            print(white_output(f"note written successfully."))
        case "readNote":
            read_note()
        case "q":
            isrunning = False
        case "quit":
            isrunning = False
        case "exit":
            isrunning = False
        case _:
            read_python_text(name)

# record a note
def take_note():
    date = input(blue_output("Enter a unique note name:"))
    note = input(blue_output("Type your note here:"))
    with open(f"note/{date}_note.txt", "a") as file:
        file.write(note)
        file.write("\n")

# read a note
def read_note():
    # list files in note directory
    files = os.listdir("note")
    for file in files:
        print(white_output(file))
    print("\n\n")
    # ask user to enter a file name to read.
    aFile = input(gray_output("Enter a file name to read:"))
    # output the file to the terminal using our output
    if aFile != "":
        output(f"note/{aFile}")
    elif aFile == "q" or aFile == "quit" or aFile == "exit":
        return
    else:
        print(f"note/{aFile} file")

# match aType and print help text accordingly.
def read_python_text(aType):
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
           print(blue_output("For help, type 'help', else quit, or type q followed by enter to exit."))

# limit the amount of lines printed at one time for easier reading.
def output(someFile):
    # define variable of type in and initilize it to 0.
    cnt :int = 0
    # open some file and push it into a list of lines.
    with open(someFile, "r") as file:
        lines = file.readlines()
    # for each line, print to terminal.
    for line in lines:
        #regex func goes here
        print(white_output(line))
        # increment cnt
        cnt += 1
        # if cnt is 17, then ask user to press enter to continue to print next 17 lines.
        if cnt == 17:
            getInput = input(white_output("Press enter to continue or type 'q' to quit:"))
            if getInput == 'q' or getInput == 'quit' or getInput == 'exit':
                break
            else:
                cnt = 0


 # colorize terminal output
def green_output(someData) -> str:
    GREEN = "\x1b[32m"
    processedData = GREEN + someData + GREEN
    return processedData
# red
def red_output(someData) -> str:
    RED = "\x1b[31m"
    processedData = RED + someData + RED
    return processedData
# white
def white_output(someData) -> str:
    WHITE = "\x1b[38;2;255;255;255m"
    processedData = WHITE + someData + WHITE
    return processedData
# gray
def gray_output(someData) -> str:
    GRAY = "\x1b[37m"
    processedData = GRAY + someData + GRAY
    return processedData
#bold
def bold_output(someData) -> str:
    BOLD = "\x1b[1m"
    processedData = BOLD + someData + BOLD
    return processedData
#blue
def blue_output(someData) -> str:
    BLUE = "\x1b[34m"
    processedData = BLUE + someData + BLUE
    return processedData
# reset
def reset_output(someData) -> str:
    RESET = "\x1b[0m"
    processedData = RESET + someData + RESET
    return processedData

# welcome message dialog
def display_welcome_message():
    os.system("clear")
    print(green_output("Welcome to Verbose Python Help System (VPHS)."))
    print(white_output("This is the early initial stages of development. Please report any bugs or issues to Chad."))
    print(white_output("You can type key words followed by the enter key, the system will display simple text related to the keyword"))
    print("\n\n")
    print(bold_output(white_output("Working Key Words:\n")))
    print(gray_output("- help - displays help information"))
    print(gray_output("- python - what is python?"))
    print(gray_output("- def - functions and classes in python"))
    print(gray_output("- if - if statement in python"))
    print(gray_output("- match - match statement in python"))
    print(gray_output("- input - input methods in python, accept user input"))
    print(gray_output("- regex - regular expressions, parses patterns and searches strings"))
    print(gray_output("- sqlite - general interaction with a local sqlite database"))
    print(gray_output("- variables - variables in python"))
    print("\n\n\n")
    print(bold_output(white_output("Read and Record Notes:\n")))
    print(gray_output("- readNote - read a note"))
    print(gray_output("- takeNote - take a note"))
    print("\n\n\n")


# ensure note folder exists
def folderCheck():
    if not os.path.exists("note"):
        os.mkdir("note")
        print(green_output("Created note folder."))

# if our python script is run directly, then run main()
if __name__ == '__main__':
    display_welcome_message()
    folderCheck()
    main()
