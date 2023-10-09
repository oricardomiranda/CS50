import csv
import sys

#Expects the user to provide two command-line arguments:
def main():
	if len(sys.argv) < 3:
		sys.exit("Too few arguments")
	if len(sys.argv) > 3:
		sys.exit("Too many arguments")
	if sys.argv[1][-4:] != ".csv":
		sys.exit("Not a CSV file")
	else:
		scourgify(sys.argv[1], sys.argv[2])
#original CSV: name and house
#new CSV: first, last, and house.
#Converts that input to that output, splitting each name into a first name and last name.

def scourgify(before, after):
	try:
		with open(before) as before: #Opens the original CSV
			reader = csv.DictReader(before) #Opens csv as reader
			with open(after, "w") as after: #Open the new CSV
				header = ["first", "last", "house"] #Define the header
				writer = csv.DictWriter(after, fieldnames=header) #Creates a object to write data and define header
				writer.writeheader() #Writes the header to the file
				for student in reader: #Iterate through the csv
					last, first = student["name"].split(", ") #Separate name into two parts by ,
					house = student["house"] #House is direct
					writer.writerow({"first": first, "last": last, "house": house}) #Write each row in the new csv
	except FileNotFoundError:
		sys.exit("Could not read {before}")

if __name__ == "__main__":
	main()