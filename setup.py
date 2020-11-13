import profile
import json
import sys
import os
import random
import datetime
import time
from numpy import random

time.sleep(3)

dt = datetime.datetime.now()
print(dt.strftime("%A, %B %d, %Y | %H:%M:%S - %Z"))

if os.path.exists("user_profile.json"):
    print("User profile already exists.")
    ask_change = input("Would you like to update the file? (Y/n)\n")
    if ask_change == 'Y':
        username = input("Username:\n")
        age = input("Age:\n")
        dob = input("Date of birth:\n")
        gender = input("Gender:\n")
        bio = input("Bio:\n")
        email = input("Email:\n")
        phone = input("Phone number:\n")
        confirm = input("Execute changes? (This will overwrite your previous changes.) (Y/n)\n")
        if confirm == 'Y':
            update_x = {
                "Username:": f"{username}",
                "Age:": f"{age}",
                "Date of birth:": f"{dob}",
                "Gender:": f"{gender}",
                "Bio:": f"{bio}",
                "Email:": f"{email}",
                "Phone number:": f"{phone}"
                }

            y = json.dumps(update_x, indent=4, sort_keys=True)

            with open("user_profile.json", "w+") as f:
                f.write(y)
                f.close()
        else:
            print("No changes were made to \"user_profile.json\".")
    else:
        print("Changes haven't been executed, therefore, no change has occured.")
        

else:
    f = open("user_profile.json", "x")
    f.close()
    username = input("Username:\n")
    age = input("Age:\n")
    dob = input("Date of birth:\n")
    gender = input("Gender:\n")
    bio = input("Bio:\n")
    email = input("Email:\n")
    phone = input("Phone number:\n")
    confirm = input("Execute information? (Y/n)\n")

    x = {
    "Username:": f"{username}",
    "Age:": f"{age}",
    "Date of birth:": f"{dob}",
    "Gender:": f"{gender}",
    "Bio:": f"{bio}",
    "Email:": f"{email}",
    "Phone number:": f"{phone}"
    }

    y = json.dumps(x, indent=4, sort_keys=True)

    if confirm == 'Y':
        with open("user_profile.json", "w") as f:
            f.write(y)
            f.close()
            print("\"user_profile.json\" has been updated.")
    else:
        print("No changes have been made to \"user_profile.json\".")