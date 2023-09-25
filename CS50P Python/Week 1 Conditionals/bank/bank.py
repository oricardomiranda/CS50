greeting = input("Greeting ")

greeting = str.strip(greeting)
greeting = str.lower(greeting)

if greeting == "hello" or greeting == "hello, newman":
	print("$0")
elif greeting[0] == "h":
	print("$20")
else:
	print("$100")