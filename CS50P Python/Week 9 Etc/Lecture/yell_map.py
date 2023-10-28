def main():
	yell("This", "is", "CS50")


def yell(*words):
	uppercased = map(str.upper, words) #Properties passed to map which creates a list
	print(*uppercased)#Unpacks the list


if __name__ == "__main__":
	main()
