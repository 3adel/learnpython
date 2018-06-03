class Employee:  
	
	#class variables
	number_of_employees = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last =  last
		self.pay = pay
		self.email = first + '.' + last + '@company.com' 

		#a new employee is created
		Employee.number_of_employees += 1

#each method within a class will take self as an argument
	def fullName(self): 
		return self.first + ' ' + self.last

#try to apply a raise method
	def apply_raise(self):

		#using self here gives the flexibility to change the raise amount later for a specific employee
		self.pay = int(self.pay * self.raise_amount)

		# you can use the class instead of self if you're absolutely sure that the raise won't change at all form any eimployee
		#self.pay = int(self.pay * Employee.raise_amount)
	

	#class methods using a decorator. In this method, we take the class as an
	#rgument
	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount


#When we create objects, self is passed automatically. Also the init method will be run automatically
print(">>> Number of employees before =", Employee.number_of_employees)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


#raise amount before calling the class method
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#calling the class method
Employee.set_raise_amount(1.05)

#you can also run class methods from instances, but nobody does it really
#emp_1..set_raise_amount(1.05)

#raise amount before calling the class method
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)




