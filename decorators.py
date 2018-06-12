#decorator functions allows us to easily add functionality to our existing function by adding it inside our wrapper

def decorator_function(original_function):
	def wrapper_function():
		print('---> extra functionality in wrapper function ran')
		return original_function()
	return wrapper_function

@decorator_function
def display():
	print('---> display function ran')

#or can be written without the @ directive instead as: 
#display = decorator_function(display)

display()

