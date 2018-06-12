#decorator functions allows us to easily add functionality to our existing function by adding it inside our wrapper

def decorator_function(original_function):
	def wrapper_function(*args):
		print('---> extra functionality in wrapper function ran')
		return original_function(*args)
	return wrapper_function

@decorator_function
def display():
	print('---> display function ran')

@decorator_function
def display_info(name, age):
	print('---> display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
display()