#animal is an object
class Animal(object):
	pass

#Dog is-a Animal
class Dog(Animal):
	def __init__(self, name):
		#Dog has-a name
		self.name = name


#Cat is-a Animal
class Cat(Animal):
	def __ini__(self, name):
		#Cat has-a name
		self.name = name

#a Person is an object
class Person(object):
	def __init__(self, name, pet):
		#Person has-a name
		self.name = name

		#Person has a pet of some kind
		self.pet = pet

#Employee is a Person
class Employee(Person):
	def __init__(self, name, pet, salary):
		#using super helps us avoid repetition
		super().__init__(name, pet)

		#Emplyee has a salary
		self.salary = salary



emp1 = Employee('adel',True, 434343)
print(emp1.__dict__)


