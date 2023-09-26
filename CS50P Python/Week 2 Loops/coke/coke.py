# Initialize variables
insert = 0
price = 50
amount_due = 50  # Amount due for a coke in cents

# Coin prompt
while insert < price:
    coin = input("Insert coin (5, 10, or 25 cents): ")
    coin = int(coin)
	# Accepted coins and withdraw
    if coin == 5 or coin == 10 or coin == 25:
        insert += coin
        amount_due -= coin
        print(f"Amount Due: {amount_due}")
    # Invalid coins
    else:
        print("Can only accept coins of 5, 10, and 25 cents")
        print(f"Amount Due: {amount_due}")

# Calculate change owed
change = insert - price
print(f"Change Owed: {change}")
