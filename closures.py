def outer_func():
	#the variable message is so called free variable
	message = 'Hi'

	#a closure in simple terms is an inner function that remembers and has access to the
	#variables in local scope in which it was created
	def inner_func():
		print (message)

	#here we return the function without executing it
	return inner_func
	
	#here, we return the function executed
	#return inner_func()

my_func = outer_func()
my_func()

print(my_func.__name__)
print(outer_func().__name__)