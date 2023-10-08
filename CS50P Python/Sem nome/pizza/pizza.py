from tabulate import tabulate
import csv
import sys

# one argument of a csv file and output as ASCII art using tabulate
# format the table using grid format
# sys.exit if not end in .csv or does not exist
def main():
	if len(sys.argv) < 2:
		sys.exit("Too few arguments")
	elif len(sys.argv) > 2:
		sys.exit("Too many arguments")
	elif sys.argv[1][-4:] != ".csv":
		sys.exit("Not a csv file")
	else:
		print(table(sys.argv[1]))

def table(file):
	try:
		with open(file) as f:
			reader = csv.reader(f)
			tbl = tabulate(reader, headers="firstrow", tablefmt="grid")
			return tbl
	except FileNotFoundError:
		sys.exit("File does not exist")

if __name__ == "__main__":
	main()