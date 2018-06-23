class Human: 
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def get_name(self):
		return self.first_name + ' ' + self.last_name

	def test(self):
		return "Test Method Human"

class Employee(Human):
	
	def __init__(self, first_name, last_name, employee_no):

		#using super to save rewriting code
		super().__init__(first_name, last_name)
		self.employee_no = employee_no

	def get_info(self):
		#reusing superclass methods
		return super().get_name() + ', ' + str(self.employee_no)

	#overriding superclass method
	def test(self):
		return "Test Method Employee"

obj_human = Human("Adel", "Shehadeh")
print(obj_human.get_name())

obj_employee = Employee("Samer", "Mahmoud", 47394739)


print(obj_employee.__dict__) 
print(obj_employee.get_info())