#first class functions. 
# A function is described as first class when it's treated in the realm of the prgramming languag as first class citizen. Meaning it can be returned, passed as an argument or assigned to a variable


def square(x):
	return x ** 2

def cube(x):
	return x ** 3

# A sample map function. It takes a function as an argument
def my_map(func, arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result

#note that when we're passing square function as an argument, we don't include the parenthesis. The reason is that we are not execution the function square, but rather we're just passing it to another function.
squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)

cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)
