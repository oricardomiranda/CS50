def main():
	yell("This", "is", "CS50")


def yell(*words):
	uppercased = [word.upper() for word in words] #for loop inside a list -> List comprehension
	print(*uppercased)


if __name__ == "__main__":
	main()
