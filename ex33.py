def myWhileLoop(myNumber):
    numbers = []
    i = 0
    while i < myNumber:
        numbers.append(i)
        i = i + 1
    return numbers

i = int(input("Enter number: "))
print(repr(myWhileLoop(i)))
