class Employee:     
	def __init__(self, first, last, pay):
		self.first = first
		self.last =  last
		self.pay = pay
		self.email = first + '.' + last + '@company.com' 

#each method within a class will take self as an argument
	def fullName(self): 
		return self.first + ' ' + self.last



#When we create objects, self is passed automatically. Also the init method will be run automatically
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)


print(emp_1.email)

#these two lines doe the exact same thing, the first calls the method with self automatically passed in the method call to the specific instance emp_1, the secondis calling the class, hence we need to provide which instance we want to apply the method to
print(emp_1.fullName())
print(Employee.fullName(emp_1))


