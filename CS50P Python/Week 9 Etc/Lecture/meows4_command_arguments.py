import sys

if len(sys.argv) == 1:
	print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n": #Makes it easier to understand how we interact with the program
	n = int(sys.argv[2])
	for _ in range(n):
		print("meow")
else:
	print("usage: meows.py")
