#Input from user
phrase = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

# Input to lowercase
phrase = str.lower(phrase)
phrase = str.strip(phrase)

#Test
#print(phrase)

# Matching the answers
match phrase:
	case "42" | "forty-two" | "forty two":
		print("Yes")
	case _:
		print("No")