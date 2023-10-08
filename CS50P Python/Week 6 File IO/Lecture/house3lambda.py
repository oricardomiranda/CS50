students = []

with open("house.csv") as file:
	for line in file:
		name, house = line.rstrip().split(",")
		student = {"name": name, "house": house}
#		student["name"] = name
#		student["house"] = house
		students.append(student)

#Sorting with lambda
for student in sorted(students, key=lambda student: student["name"]): #lambda in an anonymous function
	print(f"{student['name']} is in {student['house']}")