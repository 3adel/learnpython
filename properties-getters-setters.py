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

emp_1 = Employee('adel', 'ahmad', 40000)



print('first:', emp_1.first)
print('last:', emp_1.last)
print('full:', emp_1.fullname())
print('email:', emp_1.email)

print('-------------')

emp_1.first = 'rahaf'
emp_1.last = 'salem'


print('first:', emp_1.first)
print('last:', emp_1.last)
print('full:', emp_1.fullname())
print('email:', emp_1.email)