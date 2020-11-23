import os, sys

count=0

file=sys.argv[1]
file2=sys.argv[2]

file2=file2 if not file2.startswith("/") else file2[1:]

if True:
    os.system(f"mv -i {file} ~/storage/external-1/{file2} 2> /dev/null")
    print(f"Transferred {file}... Now symlinking...")
    os.system(f"ln -s -i ~/storage/external-1/{file2} {file} 2> /dev/null")
    print(f"{file} successfully transferred and symlinked.")
