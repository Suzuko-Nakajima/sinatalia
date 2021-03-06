import profile
import json
import sys
import os
import random
import datetime
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

print(quote)

name = input("Enter your name:\n")
age = input("Enter your age:\n")
dob = input("Enter your date of birth:\n")
gender = input("Enter your gender:\n")
bio = input("Bio:\n")


file = input("Enter the file name you want to create.\n")
if os.path.exists(file):
    print("This file already exists.")
    delete0 = input("Do you want to delete the existing file?")
    if delete0 == 'Y':
        os.remove(file)
        print(f"\"{file}\" has been deleted.")
    else:
        print(f"\"{file}\" still has not been tampered with.")
else:
    f = open(file + ".json", "x")
    f.close()
    

x = {
    "Name": f"{name}",
    "Age:": f"{age}",
    "Date of birth:": f"{dob}",
    "Gender:": f"{gender}",
    "Bio:": f"{bio}"
}

y = json.dumps(x)
print(y)

f = open(file + ".json", "w")
f.write(y)
f.close()