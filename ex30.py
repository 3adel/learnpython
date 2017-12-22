people = 10
cars = 1000
trucks = 15


if not (cars > people or cars == people):
    print("We should take the cars.")
#elif checks the previous condition, and if it's false, executes the following statement
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
