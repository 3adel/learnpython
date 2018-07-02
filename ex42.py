#animal is an object
class Animal(object):
	def walk(self):
		print('I am walking')
	

#Dog is-a Animal
class Dog(Animal):
	def __init__(self, name):
		#Dog has-a name
		self.name = name

	def bark(self):
		print("I am barking")
		


#Cat is-a Animal
class Cat(Animal):
	def __init__(self, name):
		#Cat has-a name
		self.name = name

#a Person is an object
class Person(object):
	def __init__(self, name, pet, kids):
		#Person has-a name
		self.name = name

		#Person has a pet of some kind
		self.pet = pet
		self.kids = kids

#Employee is a Person
class Employee(Person):
	def __init__(self, name, pet, kids, salary):
		#using super helps us avoid repetition
		super().__init__(name, pet, kids)

		#Emplyee has a salary
		self.salary = salary





#Fish is an object
class Fish(object):
	pass

#Salmon is a Fish
class Salmon(Fish):
	pass

#Hailbut is a Fish
class Halibut(Fish):
	pass

hoh_hof = Dog('Stinger')

emp1 = Employee('Rami', hoh_hof, ['Amal','Samir','Dali'], 50000)

print(emp1.__dict__)
print(emp1.name)
print(emp1.pet.__dict__)
print(emp1.kids)
print(emp1.salary)
print(emp1.pet.bark())

#add children 
emp1.kids.append('Mahmoud')
print(emp1.kids)
k = emp1.kids.pop()
print(emp1.kids)
print(k)

