import os, runner, subprocess

cprint = runner.cprint

def run(command):
    
    runner.run(command, f"{command} run successfully!", f"{command} failed to run!")

runner.checkreqs()

info=subprocess.check_output("termux-info".split()).decode().split("\n")

devicename=info[info.index("Device model:")+1]

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

runner.run("cp $PREFIX/etc/bash.bashrc $PREFIX/etc/bash.bashrc.backup")

with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "r") as file:

    read = file.read()

    if "PS1='\$ '" in read or "PS1=\"\$ \"" in read:

        with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "a") as file2:

            file2.write(f'\n'+"PS1="+"\'$(tput setaf 2)termux@"+devicename+r": $(tput setaf 4)\w $(tput sgr0)\$ '")

with open ("/data/data/com.termux/files/usr/etc/bash.bashrc", "r") as file2:

    file2d = file2.read()

    print(file2d)

    with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "w") as file:

        file.write(file2d.replace("PS1='\$ '", "").replace("PS1=\"\$ \"", "")) 

if not os.path.exists("/"+"/".join(os.path.abspath(__file__).split("/")[:-1])+"/gite"):

    runner.run("git clone https://github.com/r2boyo25/gite")

else:

    runner.run(f'rm -r {"/"+"/".join(os.path.abspath(__file__).split("/")[:-1])+"/gite"}')

with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "r") as file:

    if not "/"+"/".join(os.path.abspath(__file__).split("/")[:-1])+"/gite/gite.py" in file.read():

        with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "a") as file2:

            file2.write(f"\n\nalias gite=\"python3 {'/'+'/'.join(os.path.abspath(__file__).split('/')[:-1])+'/gite/gite.py'}\"")

runner.run("source /data/data/com.termux/files/usr/etc/bash.bashrc")

cprint("-- Done!--", 3)

