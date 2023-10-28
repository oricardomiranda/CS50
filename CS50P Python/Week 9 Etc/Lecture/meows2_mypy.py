#run with mypy explains types errors
def meow(n: int) -> str: #We define that we are return a str
	return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end ="")
# Mypy: Success: no issues found in 1 source file
