
#this decorator can be used for any new function as a logger
def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
		return orig_func(*args, **kwargs)

	return wrapper


@my_logger
def display_info(name, age):
	print('---> display_info ran with arguments ({}, {})'.format(name, age))

@my_logger
def add_numbers(x, y):
	print('---> add_numbes ran with arguments ({}, {})'.format(x, y))
	return x + y

display_info('John', 25)
add_numbers(1, 2)
