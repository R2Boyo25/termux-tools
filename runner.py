import os

def run(command, success="", error=""):

    if not os.system(command):

        os.system("tput setaf 2")
        
        print(success)

        os.system("tput sgr0")

    else:

        os.system("tput setaf 1")

        print(error)

        os.system("tput sgr0")

def checktermux():

    if not os.path.exists("/data/data/com.termux"): 
        
        os.system("tput setaf 1")

        print("This is not a Termux environment! Exiting...")

        os.system("tput sgr0")
        
        quit()

def checksd():
    if not os.path.exists("/storage/extSdCard/Android/data/com.termux/"): 
        
        os.system("tput setaf 1")

        print("SD card not found! Exiting...")

        os.system("tput sgr0")
        
        quit()

def checkreqs():
    
    checktermux()

    checksd()

def cprint(text, color):
    c=str(color)

    if not c.isdigit():
        
        raise Exception("Argument 'color' must be a number")

    os.system(f"tput setaf {c}")

    print(text)

    os.system("tput sgr0")
