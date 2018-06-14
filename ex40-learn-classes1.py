class Employee:  
	
	#class variables
	number_of_employees = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last =  last
		self.pay = pay
		self.email = first + '.' + last + '@company.com' 

		Employee.number_of_employees += 1

	def fullName(self): 
		return self.first + ' ' + self.last

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


	#class methods using a decorator. In this method, we take the class as an
	#rgument. Class variable nameis cls by convention
	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#set a class variable through a class method. It's equal to saying
#Employee.raise_amount = 1.1
#You can also run class methods from instances, but nobody does it
#emp_1.set_raise_amount(1.1)
Employee.set_raise_amount(1.1)


#raise amount before calling the class method
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)






