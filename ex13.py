from sys import argv
#read the WYSS section for how to run this

#unpack argv. Take whatever in argv and assign it to those 4 variables
script, first, second, third = argv

#What's in argv?
print(">>>> argv holds this: ", repr(argv))

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your second variable is:", third)
