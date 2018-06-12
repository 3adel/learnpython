import logging 
logging.basicConfig(filename='mylog.log', level=logging.INFO)

def logger(func):
	def log_func(*args):
		logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
		print(func(*args))
	return log_func

def add(x, y, z):
	return x + y + z

def sub(x, y, z):
	return x - y - z

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(1,2,3)

print(add_logger)
	





