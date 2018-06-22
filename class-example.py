class Human:

	def __init__(self, species, legs, hands, head, first_name, last_name):
		self.species = species
		self.legs = legs
		self.hands = hands
		self.head = head
		self.first_name = first_name
		self.last_name = last_name


person_1 = Human('Home Sapiens', 2, 2, 1, 'adel', 'shehadeh')


class Male(Human):
	def __init__(self, has_penis):
		self.has_penis = has_penis

person_2 = Male(True)
person_2.species, person_2.legs, person_2.hands, person_2.head, person_2.first_name, person_2.last_name = 'Homo Erectus', 2, 2, 1, 'adel', 'shehadeh'
person_2.last_name = 'Samer'

print(person_1.__dict__)
print(person_2.__dict__)