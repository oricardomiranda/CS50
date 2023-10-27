class Student: #By convention we use capital letters
	def __init__(self, name, house): #opening a method. __ is called dunder
		self.name = name
		self.house = house #This is the function that will be called

	def __str__(self): #Only uses one argument
		return f"{self.name} from {self.house}" #We use this class to print strings

	@property #These property deal with what the user can input
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		if not name:
			raise ValueError("Missing name")
		self._name = name

	# Getter
	@property
	def house(self):
		return self._house # _ is the convention no to have the same name in both functions. One _ means don't alter. Two __ means really shouldn't change this

	# Setter
	@house.setter
	def house(self, house): #We choose which values are able to be called
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid house")
		self._house = house


def main():
	student = get_student()
	print(student)


def get_student():
	name = input("Name: ")
	house = input("House: ")
	return Student(name, house)


if __name__ == "__main__":
	main()

