# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
groceries = {}
# Then output the user’s grocery list in all uppercase,
while True:
	try:
		# Treat the user’s input case-insensitively.
		item = input().upper().strip()
		if item not in groceries:
			# Initiate count with 1
			groceries[item] = 1
		else:
			# Add 1 to count
			# No need to pluralize the items.
			groceries[item] += 1
	except EOFError:
		# How to deal with ctrl+d
		# sorted alphabetically by item
		sorted_groceries = dict(sorted(list(groceries.items())))
		# prefixing each line with the number of times the user inputted that item.
		for item in sorted_groceries:
			print(sorted_groceries[item], item, sep=" ")
		break
	except KeyError:
		pass





