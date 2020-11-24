import os, runner

cprint = runner.cprint

def run(command):
    
    runner.run(command, f"{command} run successfully!", f"{command} failed to run!")

runner.checkreqs()

if not os.path.exists(os.path.expanduser('~/.bashrc')):

    runner.run(f"ln -s /data/data/com.termux/files/usr/etc/bash.bashrc {os.path.expanduser('~/.bashrc')}")

else:
    runner.cprint(f"{os.path.expanduser('~/.bashrc')} already symlinked!", 3)

cprint("-- Starting Installer --", 3)

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

cprint("Editing PS1 in bash.bashrc", "3")

with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "r") as file:

    if not "PS1='\w \$ '" in file.read():

        with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "a") as file2:

            file2.write("\n"+r"PS1='\w \$ '")

cprint("-- Done!--", 3)


