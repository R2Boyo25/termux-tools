import os, runner

def run(command):
    runner.run(command, f"{command} run successfully!", f"{command} failed to run!")

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
