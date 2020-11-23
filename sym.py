import os, sys

count=0

for file in sys.argv[1:]:
    os.system(f"mv -i {file} ~/storage/external-1/{file} 2> /dev/null")
    print(f"Transferred {file}... Now symlinking...")
    os.system(f"ln -s -i ~/storage/external-1/{file} {file} 2> /dev/null")
    print(f"{file} successfully transferred and symlinked.")
    count=count+1
print(f"{count} files successfully transferred and symlinked")
