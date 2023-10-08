students = []

with open("house.csv") as file:
	for line in file:
		name, house = line.rstrip().split(",")
		student = {"name": name, "house": house}
#		student["name"] = name
#		student["house"] = house
		students.append(student)

#Function to get the name for sorting
def get_name(student):
	return student["name"]

#Sorting with key
for student in sorted(students, key=get_name):
	print(f"{student['name']} is in {student['house']}")