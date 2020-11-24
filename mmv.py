import sys, runner

filesMoved=0

for entry in sys.argv[1:]:

    for file, dest in entry.split(","):
        
        runner.run(f"mv -i {file} {dest} 2> /dev/null", f"Transferred {file} to {dest}...", f"Failed to transfer {file} to {dest}!")

        filesMoved+=1

print(f"{filesMoved} files successfully transferred")
