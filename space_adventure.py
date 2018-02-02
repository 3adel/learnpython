# Adel Shehadeh
# 2018-01-25
# Text-based space adventure game

import random
import time

print("Hello")
time.sleep(3)
print("There")

def displayIntro():
    print("This is an intro to the game.")

def choosePath():
    path = ""

    #input validation trick
    while path != '1' and path != '2':
        path = input("Which path will you shooose? (1 or 2) ")
    return path

def checkPath(chosenPath):
    print("You head down the path...")
    time.sleep(2)
    print("Approaching...")
    time.sleep(2)
    print("Oh, somethig is happening ...")
    time.sleep(2)

    correctPath = str(random.randint(1,2))
    print(">>>> correct path is", correctPath)

    if chosenPath == correctPath:
        print("That tingling was just admirations of citizens")
    else:
        print("You're fucked")

playAgain = "yes"

while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice)
    playAgain = input("Do you want to play again?")
