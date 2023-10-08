import csv # this will deal with a lot of corner cases for us

students = []

with open("house.csv") as file:
	reader = csv.DictReader(file) #We name the header in the file and apped using the name of the key
	for row in reader:
		students.append({"name": row["name"], "house": row["house"]})

#Sorting with lambda
for student in sorted(students, key=lambda student: student["name"]): #lambda in an anonymous function
	print(f"{student['name']} is in {student['house']}")