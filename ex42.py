#animal is an object
class Animal(object):
	def walk(self):
		print('I am walking')
	pass

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





#Fish is an object
class Fish(object):
	pass

#Salmon is a Fish
class Salmon(Fish):
	pass

#Hailbut is a Fish
class Halibut(Fish):
	pass

#rover is a dog
rover = Dog('Rover')

#satan is a Cat
satan = Cat('Satan')

#mary is a person
mary =Person('Mary', None)

#mary has a pet named satan
mary.pet = satan

print(mary.pet.__dict__)

#frank is an employee with no pets and with a salary of 434343
frank = Employee('Frank',None, 434343)
#frank has a pet named rover
frank.pet = rover


#flipper is a fish
flipper = Fish()

#crouse is a Salmon
crouse = Salmon()

#harry is Halibut
harry =  Halibut()

myAnimal = Animal()
myAnimal.walk()

myDog = Dog('Sami')
myDog.walk()
myDog.bark()

