import os

pyfiles=[]

print("- Looking For Files -")

for root, dirs, files in os.walk("."):

    for file in files:

        print(file, end=" - ")

        if file.lower().endswith(".py") and file.split("/")[-1] not in ("login.py", "setup.py", "setup-termux.py", "runner.py"):

            pyfiles.append(file)

    break

print("")

print("-- Validating Files --")

bashfile = "/data/data/com.termux/files/usr/etc/bash.bashrc" if os.path.exists("/data/data/com.termux/") else os.path.expanduser("~/.bashrc")

print(f"-- Searching {pyfiles} --")

with open(bashfile, "r") as bash:

    bash2=bash.readlines()

def inval(bash2):

    global pyfiles

    a=0

    for file in pyfiles:

        for line in bash2:

            try:

                if (os.path.abspath(file) in line and not line.startswith("#")):

                    pyfiles.pop( pyfiles.index( file ) )

                elif file.replace(".py", "") in line and not line.startswith("#"):

                    pyfiles.pop( pyfiles.index( file ) )

            except:
                pass

for number in range(len(pyfiles)*2):

    inval(bash2)
 
print(f"--- Editing {bashfile} ---")

with open(bashfile, "a") as bash:

    if len(pyfiles) > 0:

        bash.write("\n")

        for file in pyfiles:

            bash.write(f"alias {file.replace('.py', '')}=\"python3 {os.path.abspath(file)}\"\n")

print("Done!")

