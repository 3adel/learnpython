def myWhileLoop(myNumber, increment):
    numbers = []
    for i in range(0, myNumber, increment):
        print(">>>> While is running: ", i)
        numbers.append(i)
        print(">>>> i after increment: ", i)
    return numbers

i, myIncrement = int(input("Enter number: ")), int(input("Enter increment: "))
print(repr(myWhileLoop(i, myIncrement)))
