with open("house.csv") as file:
	for line in file:
		row = line.rstrip().split(",") # normal to name rows and columns
		print(f"{row[0]} is in {row[1]}")
