print("How old are you?", end=' ')
age = input("---> ")
print("How tall are you?", end =' ')
height = input("---> ")
print("How much do you weigh?", end=' ')
weight = input("---> ")

print(f"So, you're {age} old. {height} tall and {weight} heavy.")

#We use repr() to show the python representation of a variable value
#We use casting int(value) to convert it into an int

#Study drill 2 and 3
print("What's your age?", end=' ')
age = input("--->")

#3 ways to do the same thing:
print("Your name is " + age)
print(f"Your age is {age}")
print("Your age is {}".format(age))




       

