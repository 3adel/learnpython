from sys import argv
#read the WYSS section for how to run this

#unpack argv. Take whatever in argv and assign it to those 4 variables
script, city, population, country, continent = argv

#What's in argv?
print(">>>> argv holds this: ", repr(argv))

print("The script is called:", script)
print("Your city is:", city)
print("Your city population is:", population)
print("Your country is:", country)
print("Your continent is:", continent)

#get the planet using input() instead of argv
planet = input("What's your planet?")
print("Your planet is: ", planet)
