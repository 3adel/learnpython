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
    while path !=1 and path != 2:
        try:
            path = int(input("Which path will you shooose? (1 or 2) "))
        except:
            print("Learn to type a number!")
    return path

displayInto()
choosePath()
