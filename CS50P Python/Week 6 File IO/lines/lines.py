import sys

# Expect one command line argument with the path or name of a python file
def main():
	if len(sys.argv) < 2:
		sys.exit("Too few arguments")
	elif len(sys.argv) > 2:
		sys.exit("Too many arguments")
	else:
		if sys.argv[1][-3:] != ".py":
			sys.exit("Not a python file")
		else:
			print(count_lines(sys.argv[1]))

# Output the nuber of lines of code
# Exclude empty lines and comments
def count_lines(file):
	try:
		counter = 0
		with open(file, "r") as f:
			for line in f:
				if not (line.lstrip().startswith("#") or line.strip() == ""):
					counter += 1
			return counter
	except FileNotFoundError:
		sys.exit("File does not exist")

# sys.exit if:
# arguments are not as spec
# inexistent file

if __name__ == "__main__":
	main()