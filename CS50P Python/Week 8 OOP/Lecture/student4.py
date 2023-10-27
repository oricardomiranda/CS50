def main():
	student = get_student()
	if student["name"] == "Padma":
		student["house"] = "Ravenclaw" #Override for Ravenclaw
	print(f"{student['name']} from {student['house']}")


def get_student():
	name = input("Name: ")
	house = input("House: ")
	return {"name": name, "house": house} #Simple way to create the dictionary


if __name__ == "__main__":
	main()

