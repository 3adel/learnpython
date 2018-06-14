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

	#alternative constructor
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	#static methods are created because they have some sort of logical connection with the class, but they don't take self or class as arguments
	#static methods don't operate on the instance or the class
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True
	

import datetime
my_date = datetime.date(2016, 8, 10)

print(Employee.is_workday(my_date))


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)








