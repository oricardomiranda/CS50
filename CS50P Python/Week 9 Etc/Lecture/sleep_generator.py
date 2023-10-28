
def main():
	n = int(input("What's n? "))
	for s in sheep(n):
		print(s)


def sheep(n):
	for i in range(n):
		yield "🐑" * i #Generators. Similar to return but won't send all at once to main. Saves processing

if __name__ == "__main__":
	main()
