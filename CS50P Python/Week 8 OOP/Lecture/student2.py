def main():
	student = get_student() #Tuple
	#if student[0] == "Padma":        THIS WILL NOT WORK BECAUSE A TUPLE IS NOT MUTABLE. LET'S USE A LIST INSTEAD
	#	student[1] = "Ravenclaw"
	print(f"{student[0]} from {student[1]}") #Indexing a tuple


def get_student():
	name = input("Name: ")
	house = input("House: ")
	return (name, house) #This () says it's a tuple

if __name__ == "__main__":
	main()

