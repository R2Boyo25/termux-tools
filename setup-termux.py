import os, runner

def run(command):
    runner.run(command, f"{command} run successfully!", f"{command} failed to run!")

if not os.path.exists("/data/data/com.termux"): os.system("tput setaf 1");print("This is not a Termux environment! Exiting...");os.system("tput sgr0");quit()

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

print("Editing PS1 in bash.bashrc")

with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "r") as file:
    if not "PS1='\w \$ '" in file.read():
        with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "a") as file2:
            file2.write("\n"+r"PS1='\w \$ '")

print("-- Done!--")


