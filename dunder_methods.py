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


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Adel', 'Shehadeh', 20000)

print(repr(emp_1))
print(str(emp_1))



