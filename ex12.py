age = int(input("How old are you?"))
height = input(f"You are {age} years old. Now tell us how tall are you?")
weight = input("How much do you weigh?")

print(f"So, you're {age} old. {height} tall and {weight} heavy.")

#all argument expressions are evaluated before the call is attempted. This is why input() function is called first in the print statement
print("How old are you?" , input()) #initially, input() has no value
