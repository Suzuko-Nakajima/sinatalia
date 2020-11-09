import asyncio
import profile
import json
import sys
import os
import random
import datetime
from numpy import random

msg = random.choice([
    "Vacant hallways?",
    "Are sweet dreams overrated?",
    "Nakajima-san is not only always thinking, but always learning!",
    "Nobody is perect, this will always be true regardless of one's morals and beliefs.",
    "Death is like any natural disaster, you can't prevent it from happening.",
    "Nakajima always takes time, never rushes unless unsure.",
    "True colors are always hidden within the depths of a person, that is just how it is.",
    "You know what's strange? Science, but it gives (almost) accurate details and explanations on how things are caused.",
    "Even detectives can be deceived, such a sad sight.",
    "Mysteries...mysteries...",
    "What is in a name?"
])

def ac1():
    print("1. Suzuko\n2. Inowei\n3. Tenshu\n4. Naka-Naka")

def ac2():
    print("1. C++.\n2. Java\n3. HTML\n4. NodeJS")

def ac3():
    print("1. One\n2. Two\n3. Three\n4. Sixteen")

def ac4():
    print("1. True\n2. False")

def ac5():
    print("1. Programming\n2. Developement\n3. Discord bot\n4. Ongoing")

def ac6():
    print("1. True\n2. False")

def ac7():
    print("1. Enshimaki\n2. Ichimaru\n3. Inowei\n4. Ichihara")

def ac8():
    print("1. Ichigo Kurosaki\n2. Kyoko Kirigiri\n3. Sebastian Michaelis\n4. Naruto Uzumaki")

def ac9():
    print("1. Chinese\n2. Japanese\n3. Korean\n4. Taiwanese")

def ac10():
    print("1. Sin\n2. Nis\n3. Sen\n4. Nes")

name = input("Please enter your name:\n")
if name == name:
    print(f"{name} logged in...check.")
    print(msg)



start = input("Type \'Start\' to begin the quiz.\nWhen you begin, all the answers must be written in words, no numerical or special characters shall be used or else answers will be wrong.\n")
if start == 'Start':
    print("What is Nakajima\'s first name?\n")
    ac1()
    answer1 = input()
    print("Before switching over to Python, what coding/programming language did Nakajima use?\n")
    ac2()
    answer2 = input()
    print("How long was the \"Inactivity\" gap from when Shiro Saikosaki was first created, to when she was finally hosted online?\n")
    ac3()
    answer3 = input()
    print("Nakajima has modified a game. True or False?\n")
    ac4()
    answer4 = input()
    print("What kind of project is Shiro Saikosaki (Discord bot)?\n")
    ac5()
    answer5 = input()
    print("Nakajima prefers a last name basis. True or False?\n")
    ac6()
    answer6 = input()
    print("What is Nakajima\'s middle name?\n")
    ac7()
    answer7 = input()
    print("Who is Nakajima's favorite anime character?\n")
    ac8()
    answer8 = input()
    print("What kind of name does Nakajima have?\n")
    ac9()
    answer9 = input()
    print("What word (English) does Nakajima's full name spell?\n")
    ac10()
    answer10 = input()
    
    grade = {
        "Name:": f"{name}",
        "Question 1:": f"Your answer: {answer1}",
        "Question 2:": f"Your answer: {answer2}",
        "Question 3:": f"Your answer: {answer3}",
        "Question 4:": f"Your answer: {answer4}",
        "Question 5:": f"Your answer: {answer5}",
        "Question 6:": f"Your answer: {answer6}",
        "Question 7:": f"Your answer: {answer7}",
        "Question 8:": f"Your answer: {answer8}",
        "Question 9:": f"Your answer: {answer9}",
        "Question 10:": f"Your answer: {answer10}"
    }

    submit_grade = json.dumps(grade, indent=4, sort_keys=False)

    with open(name + "\'s_grade.json", "w+") as f:
        f.write(submit_grade)
        f.close()
else:
    print("Error: Invalid key.")