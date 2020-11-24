import os

def run(command, success="", error=""):
    
    if not os.system(command):

        os.system("tput setaf 2");print(success);os.system("tput sgr0")

    else:

        os.system("tput setaf 1");print(error);os.system("tput sgr0")
