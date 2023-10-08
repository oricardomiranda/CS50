names = []

for _ in range(3): # Any character will do here but _ is the convention
	names.append(input("What's your name? "))

for name in sorted(names):
	print(f"hello, {name}")

# Problem here is that we don't save our names. After closing the program, they are gone.