# Receive input
def main():
	camel = input("camelCase: ")
	snake = convert(camel)
	print("snake_case:", snake)

def convert(camel):
	snake = ""
	for c in camel:
		if c.isupper():
			snake += "_" + c.lower()
		else:
			snake += c

	if snake[0] == ("_"):
		snake = snake[1:]
	return snake

if __name__ == "__main__":
	main()