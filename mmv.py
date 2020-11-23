import os, sys

count=0

for entry in sys.argv[1:]:
    for file, dest in entry.split(","):
        os.system(f"mv -i {file} {dest} 2> /dev/null")
        print(f"Transferred {file} to {dest}...")
        count=count+1

print(f"{count} files successfully transferred")
