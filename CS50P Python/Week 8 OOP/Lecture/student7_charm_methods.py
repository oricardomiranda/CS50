class Student: #By convention we use capital letters
	def __init__(self, name, house, patronus): #opening a method. __ is called dunder
		if not name:
			raise ValueError("Missing name") #We handle the rule here and the values in the function
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid house")
		# The argument self implies access to the current object that was just created so we can store data
		self.name = name
		self.house = house #This is the function that will be called
		self.patronus = patronus


	def __str__(self): #Only uses one argument
		return f"{self.name} from {self.house}" #We use this class to print strings


	def charm(self):
		match self.patronus:
			case "Stag":
				return "🐴"
			case "Otter":
				return "🦦"
			case "Jack Russel Terrier":
				return "🐶"
			case _:
				return "🪄"



def main():
	student = get_student()
	print("Expecto Patronum!")
	print(student.charm())


def get_student():
	name = input("Name: ")
	house = input("House: ")
	patronus = input("Patronus: ")
	return Student(name, house, patronus)


if __name__ == "__main__":
	main()

