def total(galleons, sickles, knuts):
	return(galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts") # * unpacks the list into 3 individual arguments
