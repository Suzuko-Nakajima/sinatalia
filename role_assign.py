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
    "16",
    "22",
    "43",
    "64",
    "58"
])


print('Initializing program...')
time.sleep(1.5)
username = input("Enter a username:\n")
time.sleep(1)
print('Checking username...\n')
time.sleep(1)
print(f'Logging username {username}...check.')
time.sleep(1.5)
if integer == '16':
    print('You are 16th.')
else:
    print('You are an ordinary.')