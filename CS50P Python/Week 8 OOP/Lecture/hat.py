import random

class Hat:
	houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

	@classmethod
	def sort(cls, name): #We don't call it self, we call cls
		print(name, "is in", random.choice(cls.houses))

#hat = Hat() # We don't instanciate
Hat.sort("Harry")