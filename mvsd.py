import sys, runner

filesMoved=0

for file in sys.argv[1:]:
    
    runner.run(f"mv -i {file} ~/storage/external-1/{file} 2> /dev/null", f"Transferred {file}...", f"Failed to transfer {file}!")

    filesMoved+=1

print(f"{filesMoved} files successfully transferred")
