expression = input("Expression: ")

x, y, z = expression.split()

x = float(x)
z = float(z)

result = None

if y == '+':
	result = x + z
elif y == '-':
	result = x - z
elif y == '*':
	result = x * z
elif y == '/':
	if z == 0:
		print("Can't divide by zero")
	else:
		result = x / z
else:
	print("Invalid operator")

if result is not None:
	print("Result:", result)