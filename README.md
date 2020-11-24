This is a simple collection of python programs that I wrote for managing file in termux.

They are what I use for moving things to my SD card. There is also a few other programs like mmv, used like:

`mmv origin,destination origin2,destination2...`

To be able to use this you must have run `termux-setup-storage`. (And you must be running Termux :P)

Other examples:

`sym hello.txt file2.py`
`msym hello.txt textfiles/hello.txt`
`mvsd hello.txt file2.py`

To make these available everywhere run:
```bash
python3 setup.py
```
