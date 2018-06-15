class Employee:  
	
	#class variables
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last =  last
		self.pay = pay
		self.email = first + '.' + last + '@company.com' 

	def fullName(self): 
		return self.first + ' ' + self.last

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

#subclassing will change the raise ammount and add a programming language and 
class Developer(Employee):
	raise_amount = 1.1

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		# or:
		#Employee.__init__(self, first, last, pay)
		self.prog_lang = prog_lang

#a manager will manage a list of employees
class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else: 
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print('-->', emp.fullName())

		



dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
dev_2 = Developer('Adel', 'Shehadeh', 120000, 'java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print('--> Manager Email',mgr_1.email)
print(mgr_1.print_emp())
mgr_1.add_emp(dev_2)
print(mgr_1.print_emp())


