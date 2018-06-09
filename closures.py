def outer_func(msg):
	#the variable message is so called free variable
	message = msg

	#a closure in simple terms is an inner function that remembers and has access to the
	#variables in local scope in which it was created
	def inner_func():
		print (message)

	#here we return the function without executing it
	return inner_func
	
	#here, we return the function executed
	#return inner_func()

hi_func =  outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()