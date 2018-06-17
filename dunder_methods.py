class Employee: 

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay

	def fullname(self):
		return '{} {}'. format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * raise_amt)

	#this is the str() fallbackmethod when you try to print the object
	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)


	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Adel', 'Shehadeh', 20000)

#it calls __str__() first, then if doesn't exist, falls back to __repr__()
print(emp_1)

print(str(emp_1))
print(repr(emp_1))

#same as
print(emp_1.__str__())
print(emp_1.__repr__())


 

