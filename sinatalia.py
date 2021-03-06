import asyncio
import os
import sys
import random
import json
import datetime
import time
from numpy import random

quote = random.choice([
    "A lie can only travel so far before the truth unfolds.",
    "You can run from your problems, but you can never escape from them.",
    "Death is like any natural disaster, you can't prevent it from happening.",
    "The truth will always hurt much less compared to a lie.",
    "Time truly isn't real, there is no day or night...we are all living the very same \"day\".",
    "Choose a name that best suits you, does not have to be your real name."
])

d = datetime.datetime.now()
print(d.strftime("%A, %B %d, %Y | %H:%M:%S - %Z"))

time.sleep(3)

print(quote)

def initialize():
    time.sleep(2)
    print('Initialzing program...')

def start():
    print('Setting up program...')
    time.sleep(2)
    name = input("What is your name?\n")
    initialize()
    time.sleep(2)
    print(f'Username: {name}...check.')
    time.sleep(1)
    write_file = input("Do you want to write a new file? (Y/n)")
    if write_file == 'Y':
        time.sleep(1.5)
        file_name = input("Enter the file name you want, add an extension as well (\".txt\" is recommended).\n")
        if file_name == file_name:
            print('Checking for existing file...\n')
            time.sleep(1.5)
            if os.path.exists(file_name):
                print(f"You already have a file by the name and extension: \"{file_name}\".")
                q_delete_file = input("Do you want to delete this file? (Y/n)\n")
                if q_delete_file == 'Y':
                    os.remove(file_name)
                    print(f"{file_name} has been deleted, relaunch the program and rechoose your file name.")
                
                else:
                    print(f"\"{file_name}\" has not been tampered with, just relaunch the program and choose a different file name.")

            else:
                f = open(file_name, "x")
                print(f"{file_name} has been created.")
            
                question_age = input("Age:\n")
                if question_age == question_age:
                    f = open(file_name, "a")
                    f.write(f"\nName: {name}\n\nAge: " + question_age + "\n")
                    f.close()

                    question_dob = input("Date of birth:\n")
                    if question_dob == question_dob:
                        f = open(file_name, "a")
                        f.write("\nDate of birth: " + question_dob + "\n")
                        f.close()

                        question_gender = input("Gender:\n")
                        if question_gender == question_gender:
                            f = open(file_name, "a")
                            f.write("\nGender: " + question_gender + "\n")
                            f.close()

                            question_bio = input("Bio:\n")
                            if question_bio == question_bio:
                                f = open(file_name, "a")
                                f.write("\nBio: " + question_bio + "\n")
                                f.close()

                                f = open(file_name, "r")
                                print(f.read())

                                question_file = input("You have finished answering the questions, however, do you want to keep the file with the input information? (Y/n)\n")
                                if question_file == 'Y':
                                    print(f"The file \"{file_name}\" is saved to your files.")
                                else:
                                    if os.path.exists(file_name):
                                        os.remove(file_name)
                                        print(f"\"{file_name}\" has been deleted from your files.")
                                    else:
                                        print("Error: File not found.")

        else:
            print("Error: Something went wrong, possible issues:\nDuplicate file\nUnreadable code\n")
    else:
        print("You declined authorization to create a file, therefore, the program has stopped.\nFeel free to relaunch the program.")

def fail():
    print('Key is invalid, please make sure you have permission to execute this file.')

app = input("Please enter the access key to setup the program.\n")
if app == 'Launch':
    print('Checking...')
    time.sleep(3)
    start()
else:
    print('Checking...')
    time.sleep(3)
    fail()