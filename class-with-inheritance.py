#aggregation example
class Salary: 
	def __init__(self, pay):
		self.pay = pay

	def get_total(self):
		return self.pay*12


class Employee:
	def __init__(self, pay, bonus):
		self.pay = pay
		self.bonus = bonus

	def annual_salary(self):
		return self.obj_salary.get_total() + self.bonus

obj_sal = Salary(100)
print(obj_sal.__dict__)

obj_emp = Employee(obj_sal, 10)
print(obj_emp.__dict__)

#This is a simple example of composition. A Salary cannot exist on its own. You need an employee to be able to have a salary. If we destroy the employee, the salary will be also destroyed. So a asalary is tightly coupled to an employee
