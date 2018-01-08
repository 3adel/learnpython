def myWhileLoop(myNumber, increment):
    numbers = []
    i = 0
    while i < myNumber:
        print(">>>> While is running: ", i)
        numbers.append(i)
        i = i + increment
    return numbers

i, myIncrement = int(input("Enter number: ")), int(input("Enter increment: "))
print(repr(myWhileLoop(i, myIncrement)))
