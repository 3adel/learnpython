class Employee:  
	
	#class variables
	raise_amount = 1.04
	number_of_employees = 0

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

#When we create objects, self is passed automatically. Also the init method will be run automatically
print(">>> Number of employees before =", Employee.number_of_employees)

emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)

print(">>> Number of employees after =", Employee.number_of_employees)

print(">>> Employee 1 pay before raise =",emp_1.pay)
emp_1.apply_raise()
print(">>> Employee 1 pay after raise =",emp_1.pay)


#how to show class or instance namespaces
print("\n>>> Employee class namespace:\n", Employee.__dict__)
print("\n\n>>> Emp1 instance namespace:\n", emp_1.__dict__)



