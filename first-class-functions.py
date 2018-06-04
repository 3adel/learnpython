#first class functions. 
# A function is described as first class when it's treated in the realm of the prgramming languag as first class citizen. Meaning it can be returned, passed as an argument or assigned to a variable


def logger(msg):

	def log_message():
		print('Log:', msg)

	return log_message

log_hi = logger('Hi')
print(">>> log _hi is actually a function now: ",log_hi)

#now we can execute log_hi. Notice how log_hi remembered our messag passed to it, i.e., "Hi"
log_hi()
