import asyncio
import os

if os.path.exists("xfile.0"):
    os.remove("xfile.0")
    print('You had a file by the name and extension \"xfile.0\", it was automatically removed to create a new file.')

else:
    print('Could not locate a clone-like file...')

def initialize():
    print('Initialzing program...')

def start():
    print('Setting up program...')
    name = input("What is your name?\n")
    if name == "Sinatalia":
        initialize()
        print(f'Username: {name}...check.')
        f = open("xfile.0", "x")
        write_file = input("Do you want to write this file? (Y/n)")
        if write_file == 'Y':
            f = open("xfile.0", "w")
            f.write(f"This file is being written...\nExecuted by: {name}")
            f.close()

            f = open("xfile.0", "r")
            print(f.read())
            write = input("Type what you want to write in this file...\n")
            if write == write:
                f = open("xfile.0", "w")
                f.write(write)
                f.close()
                print("This is the content you added:")
                f = open("xfile.0", "r")
                print(f.read())

            else:
                print("Error: Unknown")
        else:
            if os.path.exists("xfile.0"):
                os.remove("xfile.0")
            else:
                print("This file does not exist...no files deleted.")

    else:
        print('Error: Authorization declined!')

def fail():
    print('Key is invalid, please make sure you have permission to execute this file.')

app = input("Please enter the access key to setup the program.\n")
if app == 'Launch':
    start()
else:
    fail()