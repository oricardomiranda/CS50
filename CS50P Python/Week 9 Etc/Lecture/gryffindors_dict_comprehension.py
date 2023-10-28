students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
	print(i + 1, students[i])


for i, student in enumerate(students): #This replaces the use of len
	print(i + 1, student)
