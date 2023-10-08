import csv # this will deal with a lot of corner cases for us

students = []

with open("house.csv") as file:
	reader = csv.reader(file)
	for name, house in reader:
		students.append({"name": name, "house": house})

#Sorting with lambda
for student in sorted(students, key=lambda student: student["name"]): #lambda in an anonymous function
	print(f"{student['name']} is in {student['house']}")