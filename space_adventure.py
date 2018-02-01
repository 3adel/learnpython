# Adel Shehadeh
# 2018-01-25
# Text-based space adventure game

import random
import time

print("Hello")
time.sleep(3)
print("There")

def displayInto():
    print("This is an intro to the game.")
    print()

def choosePath():
    path = ""
    #input validation trick
    while path != "1" and path !="2":
        try:
            path = input("Which path will you shooose? (1 or 2) ")
        except:
            print("Learn to type a number!")
    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("Approaching ...")
    time.sleep(2)
    print("Oh ... somethig is happening ...")
    time.sleep(2)

    correctPath = str(random.randint(1,2))

    if choosePath == correctPath:
        print("That tingling was just admirations of citizens")
    else:
        print("You're fucked")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayInto()
    choosePath()
    choice = choosePath
    checkPath(choice)
    playAgain = input("Do you want to play again?")
