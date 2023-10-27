def main():
	student = get_student() #Tuple
	print(f"{student[0]} from {student[1]}") #Indexing a tuple


def get_student():
	name = input("Name: ")
	house = input("House: ")
	return (name, house) #This () says it's a tuple

if __name__ == "__main__":
	main()