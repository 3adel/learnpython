#define a function that receives two arguments. Those two arguments will be printed
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #debug the passed  number of cheese_count and the number of boxes of crackers
    print(">>>> Enter cheese_and_crackers function. cheese_count = ", cheese_count, "boxes_of_crackers = ", boxes_of_crackers)
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.")
    #indicate that the function exited
    print("<<<< Exit cheese_and_crackers function.\n")

#first call of the function with passing just numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#Don't forget that global variables are independent form the funtion. They can still have the same name, and this wouldn't affect the variables inside the function with the same name.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

#call the function with the global variables passed
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#call the function with some math as arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#call the function with some math that includes global variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 1000)

#solving exercise 3. I will make a function that will reveive first and last name, then spits out the full name.

def fullNameCreator(firstName, initial, lastName):
    print(f"Your full name is {firstName} {initial} {lastName}")
    return (firstName + " " + initial + " " + lastName)

fullNameCreator("Adel", 'A', "Shehadeh")
print(f"Calling a function: {fullNameCreator('Adel', 'A', 'Shehadeh')}")

#now calling the function with an input from the user
fullNameCreator(input("Enter first name: > "), input("Enter your initial: > "), input("Enter last name: > "))
