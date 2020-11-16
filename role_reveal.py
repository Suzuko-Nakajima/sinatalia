import asyncio
import profile
import json
import sys
import os
import random
import datetime
import time
from numpy import random

integer = random.choice([
    "1",
    "2",
    "3",
    "4",
    "5"
])


print('Initializing program...')
time.sleep(2)
username = input("Enter a username:\n")
time.sleep(1)
password = input("Enter a password:\n")
time.sleep(1)

print('Checking for \"creditials.json\"...')
time.sleep(1)
if os.path.exists("creditials.json"):
    print('File \"creditials.json\" has been located in this directory.')
else:
    print('File not found...')
    time.sleep(1)
    with open("creditials.json", "x") as f:
        f.close()
        print('File \"creditials.json\" has been created.')

creditials = {
    "username": f"{username}",
    "password": f"{password}"
}

y = json.dumps(creditials, indent=4)

with open("creditials.json", "w+") as f:
    f.write(y)
    f.close()