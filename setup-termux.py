import os

def run(command):
    if not os.system(command):
        os.system("tput setaf 2");print(f"{command} run successfully!");os.system("tput sgr0")
    else:
        os.system("tput setaf 1");print(f"{command} failed to run!");os.system("tput sgr0")

print("-- Starting Installer --")

#progs = ["git", "python", "openssh", "nano", "root-repo"]

progs = []

with open("./resources/installs", "r") as file:
    for line in file.readlines():
        if line != "\n":
            progs.append(line.replace("\n", ""))

commands = []

for program in progs:
    commands.append(f"pkg install -y {program}")

for command in commands:
    run(command)

print("-- Done!--")
