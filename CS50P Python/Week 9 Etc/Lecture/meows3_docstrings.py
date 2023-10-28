def meow(n: int) -> str:
	"""Meow n times.""" #Python will make use of tools for automatic documentation if we use """ """

	"""
	Meow n times.

	:param n: Number of times to meow
	:type n: int
	:raise TypeError: If n is not an int
	:return: A string of n meows, one per line
	:rtype: str
	""" ## Popular documentation convention
	return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end ="")
