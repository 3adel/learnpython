def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")



#Calculate the area of a triangle
#1/2 base * heigh

def areOfTriangle(base, height):
    return 0.5 * base * height

base = float(input("What's the base length of the triangle?:"))
height = float(input("What's the height of the triangle?:"))
print(f"The calculated area of this triangle is: {areOfTriangle(base, height)}")
