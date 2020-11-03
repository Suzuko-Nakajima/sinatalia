import asyncio
import os

def initialize():
    print('Initialzing program...')
    if os.path.exists("xfile.0"):
        os.remove("xfile.0")
        print('You had a file by the name and extension \"xfile.0\", it was automatically removed to create a new file.')

    else:
        print('Could not locate a clone-like file...')

def start():
    print('Setting up program...')
    name = input("What is your name?\n")
    initialize()
    print(f'Username: {name}...check.')
    f = open("xfile.0", "x")
    write_file = input("Do you want to write this file? (Y/n)")
    if write_file == 'Y':
        f = open("xfile.0", "w")
        f.write(f"Name: {name}")
        f.close()

        question_age = input("Your age:\n")
        if question_age == question_age:
            f = open("xfile.0", "a")
            f.write("\nAge: " + question_age)
            f.close()
            
            question_dob = input("Date of birth:\n")
            if question_dob == question_dob:
                f = open("xfile.0", "a")
                f.write("\nDate of birth: " + question_dob)
                f.close()

                question_gender = input("Gender:\n")
                if question_gender == question_gender:
                    f = open("xfile.0", "a")
                    f.write("\nGender: " + question_gender)
                    f.close()

                    question_bio = input("Bio:\n")
                    if question_bio == question_bio:
                        f = open("xfile.0", "a")
                        f.write("\nBio: " + question_bio)
                        f.close()

                        f = open("xfile.0", "r")
                        print(f.read())

                        question_file = input("You have finished answering the questions, however, do you want to keep the file with the input information? (Y/n)\n")
                        if question_file == 'Y':
                            print("The file \"xfile.0\" is saved to your files.")
                        else:
                            if os.path.exists("xfile.0"):
                                os.remove("xfile.0")
                                print("\"xfile.0\" has been deleted from your files.")
                            else:
                                print("Error: File not found.")

        else:
            print("Error: Unknown")
    else:
        if os.path.exists("xfile.0"):
            os.remove("xfile.0")
            print("NOTICE: Stopped due to rejection.")
        else:
            print("This file does not exist...no files deleted.")

def fail():
    print('Key is invalid, please make sure you have permission to execute this file.')

app = input("Please enter the access key to setup the program.\nNOTE: If you have a file that with name and extension \"xfile.0\", please transfer it to another directory to make room for a new incoming file.\n")
if app == 'Launch':
    start()
else:
    fail()