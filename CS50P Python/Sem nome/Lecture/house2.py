with open("house.csv") as file:
	for line in file:
		name, house = line.rstrip().split(",") # We can name each variable while creating them 
		print(f"{name} is in {house}")