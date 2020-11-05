import profile
import json
import sys
import os
import random
import datetime

d = datetime.datetime.now()
print(d.strftime("%A, %B %d, %Y | %H:%M:%S - %Z"))

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