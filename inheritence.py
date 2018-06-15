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

#inheritence
class Developer(Employee):
	raise_amount = 1.1

dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('Adel', 'Shehadeh', 120000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)