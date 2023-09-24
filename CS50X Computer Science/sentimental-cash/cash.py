import cs50

while True:
    amount = cs50.get_float("Owed amount: ")
    if amount > 0:
        break

coins = round(amount * 100)

coin_amount = 0
while coins > 0:
    if coins >= 25:
        coins -= 25
        coin_amount += 1
    elif coins >= 10:
        coins -= 10
        coin_amount += 1
    elif coins >= 5:
        coins -= 5
        coin_amount += 1
    else:
        coins -= 1
        coin_amount += 1

print(coin_amount)