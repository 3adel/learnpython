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
		 




emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email, new_emp_1.pay, new_emp_1.first)


#raise amount before calling the class method
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)






