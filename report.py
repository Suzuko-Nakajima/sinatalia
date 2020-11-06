import profile
import json
import sys
import os
import random
import datetime
from numpy import random


if os.path.exists("reports.json"):
    with open("reports.json", encoding="utf-8") as f:
        report = json.load(f)
        f.close()

        reason = input("Input a reason:\n")


else:
    with open("reports.json", "x") as f:
        f.close()

        username = input("Enter username:\n")
        reason = input("Reason:\n")
        x = {
            "Username": f"{username}",
            "Reason": f"{reason}"
            }

        y = json.dumps(x, indent=4, sort_keys=True)

        with open("reports.json", "w") as f:
            f.write(y)
        