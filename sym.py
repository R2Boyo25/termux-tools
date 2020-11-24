import sys, runner

filesMoved=0

for file in sys.argv[1:]:
    
    runner.run(f"mv -i {file} ~/storage/external-1/{file} 2> /dev/null", f"Transferred {file}... Now symlinking...", f"Failed to transfer {file}!")

    runner.run(f"ln -s -i ~/storage/external-1/{file} {file} 2> /dev/null", f"{file} successfully transferred and symlinked.", f"Failed to symlink {file}!")

    filesMoved+=1

print(f"{filesMoved} files successfully transferred and symlinked")