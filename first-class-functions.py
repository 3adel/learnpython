#first class functions. 
# A function is described as first class when it's treated in the realm of the prgramming languag as first class citizen. Meaning it can be returned, passed as an argument or assigned to a variable


def square(x):
	return x * x

#you can assign a function to a variable
f = square

#same thing
print(square)
print(f)

#you can also treat the variable as a function now
print(square(5))

