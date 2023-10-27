class Student: #By convention we use capital letters
	def __init__(self, name, house): #opening a method. __ is called dunder
		if not name:
			raise ValueError("Missing name") #We handle the rule here and the values in the function
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid house")
		self.name = name
		self.house = house #This is the function that will be called
		# The argument self implies access to the current object that was just created so we can store data

def main():
	student = get_student()
	print(f"{student.name} from {student.house}")


def get_student():
	name = input("Name: ")
	house = input("House: ")
	return Student(name, house)


if __name__ == "__main__":
	main()

