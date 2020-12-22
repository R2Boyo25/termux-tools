#!/data/data/com.termux/files/usr/bin/python3

import os

def motd():

    os.system("cat /data/data/com.termux/files/usr/etc/motd")

if not os.path.exists("/data/data/com.termux/files/password.txt"):

    with open("/data/data/com.termux/files/password.txt", "w") as file:
        while True:

            password = input("Enter new password: ")
            confirm = input("Confirm new password: ")

            if password == confirm:
                os.system("clear")
                print("Password set successfully!")

                file.write(password)
                break
            else:
                os.system("clear")
                print("Those do not match! Try again!")

    with open("/data/data/com.termux/files/pin.txt", "w") as file:

        while True:

            print("Now to set your backup pin... \nYou can use this if you ever forget your password.")

            password = input("Enter new backup pin: ")
            confirm = input("Confirm new backup pin: ")

            if password == confirm:
                os.system("clear")
                print("Backup pin set successfully!")

                file.write(password)

                break

            else:
                os.system("clear")
                print("Those do not match! Try again!")

    with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "r") as bash:

        rbash = bash.read()

    if not "login.py" in rbash:

        with open("/data/data/com.termux/files/usr/etc/bash.bashrc", "a") as bash:

            bash.write(f"\n\nalias lock=\"python3 {os.path.abspath(__file__)}\"\n\nlock")

try:

        with open("/data/data/com.termux/files/password.txt", "r") as file:
            realpassword = file.read().strip().replace("\n", "")

        while True:
            try:

                password = input("Enter password: ")
                os.system("clear")
                if password == realpassword:

                    motd()

                    break

                elif password == "forgot":

                    print("okay... ")

                    pin = input("Whats your backup pin? ")

                    with open("/data/data/com.termux/files/pin.txt", "r") as file:
                        realpin = file.read().strip().replace("\n", "")

                    if pin == realpin:

                        os.system("rm /data/data/com.termux/files/password.txt")

                        print("Password lock has been removed, the next time you start termux this program will restart and you will be prompted to set your password.")

                        motd()

                        break

                    else:

                        print("That pin is incorrect!")

                else:

                    print("That password is incorrect! If you forgot your password, but remember your backup pin enter 'forgot', if you forgot your pin... sorry.")

            except EOFError:
                print("\nNice Try, that doesn't work. :P")

            except KeyboardInterrupt:
                print("\nNice Try, that doesn't work. :P")

            except SystemError:
                print("\nNice Try, that doesn't work. :P")

except EOFError:
    print("\nNice Try, that doesn't work. :P")

except KeyboardInterrupt:
    print("\nNice Try, that doesn't work. :P")
