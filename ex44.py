#implicit inheritence

class Parent(object):

	def __init__(self, name):
		self.name = name

	def implicit(self):
		print("Parent implicit()")

class Child(Parent):
	pass


dad = Parent('Ahmed')
son = Child('Sami')

dad.implicit()
son.implicit()

print(dad.name)
print(son.name)

