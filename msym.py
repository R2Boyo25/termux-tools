import sys, runner

file=sys.argv[1]
file2=sys.argv[2]

file2=file2 if not file2.startswith("/") else file2[1:]

if True:
    
    runner.run(f"mv -i {file} ~/storage/external-1/{file2} 2> /dev/null", f"Transferred {file}... Now symlinking...", f"Failed to transfer {file}")

    runner.run(f"ln -s -i ~/storage/external-1/{file2} {file} 2> /dev/null", f"{file} successfully transferred and symlinked.", f"Failed to symlink {file}")
