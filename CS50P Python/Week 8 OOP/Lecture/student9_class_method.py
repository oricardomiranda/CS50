class Student: #By convention we use capital letters
	def __init__(self, name, house): #opening a method. __ is called dunder
		self.name = name
		self.house = house #This is the function that will be called

	def __str__(self): #Only uses one argument
		return f"{self.name} from {self.house}" #We use this class to print strings

	@classmethod
	def get(cls):
		name = input("Name: ")
		house = input("House: ")
		return cls(name, house)


def main():
	student = Student.get()
	print(student)


if __name__ == "__main__":
	main()

