import os

pyfiles=[]

print("- Looking For Files -")

for root, dirs, files in os.walk("."):
    for file in files:
        print(file, end=" - ")
        if file.lower().endswith(".py") and file.split("/")[-1]!="setup.py":
            pyfiles.append(file)
    break

print("")

print("-- Validating Files --")

with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "r") as bash:
    print(f"-- Searching {pyfiles} --")
    bash2=bash.readlines()

def inval(bash2):
    a=0
    global pyfiles
    for file in pyfiles:
        print(f"Selecting {file}...")
        for line in bash2:
            line2=line.replace("\n", "")
            try:
                if (os.path.abspath(file) in line and not line.startswith("#")):
                    print(f"{pyfiles.pop(pyfiles.index(file))} is invalid! Line: {line2}")
                elif file.replace(".py", "") in line and not line.startswith("#"):
                    print(f"{pyfiles.pop(pyfiles.index(file))} is invalid! Line: {line2}")
            except:a=a+1
                   #print(f"{file} already invalidated!")
        print(f"Ending {file}...")

for number in range(len(pyfiles)*2):
    inval(bash2)
 
for file in pyfiles:
    print(f"{file} is valid!")

print(f"--- Editing /data/data/com.termux/files/usr/etc/bash.bashrc ---")

with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "a") as bash:
    if len(pyfiles)>0:
        bash.write("\n")
        for file in pyfiles:
            bash.write(f"alias {file.replace('.py', '')}=\"python3 {os.path.abspath(file)}\"\n")
            #print(f"alias {file.replace('.py', '')}=\"python3 {os.path.abspath(file)}\" >> $PREFIX/etc/bash.bashrc\n")

print("Done!")

