from random import randint

def main():
	answers = 10
	score = 0
	chances = 3
	lvl = get_level()

	while answers != 0:
		if chances == 3:
			x, y = generate_integer(lvl)
		try:
			user_answer = int(input(f"{x} + {y} = "))
			correct = x + y
			if user_answer == correct:
				answers -= 1
				score += 1
				chances = 3
				continue
			else:
				raise ValueError
		except (ValueError, NameError):
			print("EEE")
			chances -= 1
			pass
		if chances == 0:
			print((f"{x} + {y} = {correct}"))
			chances = 3
			answers -= 1
	print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                print("Select a level between 1 and 3")
        except ValueError:
            print("Invalid input")


def generate_integer(level):
	if level == 1:
		x = randint(0, 9)
		y = randint(0, 9)
	elif level == 2:
		x = randint(10, 99)
		y = randint(10, 99)
	elif level == 3:
		x = randint(100, 999)
		y = randint(100, 999)
	return x, y

if __name__ == "__main__":
    main()