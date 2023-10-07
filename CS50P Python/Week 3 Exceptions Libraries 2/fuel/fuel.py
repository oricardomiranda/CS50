def main():
	fraction = get_fraction("Fraction: ")
	print(fraction)

def get_fraction(fraction):
	while True:
		try:
			x, y = input(fraction).split("/")
			if 0 <= int(x)/int(y) <= 0.1:
				return ("E")
			elif 0.9 <= int (x)/int(y) <= 1:
				return("F")
			elif 0.1 < int(x)/int(y) < 0.9:
				return str(round(int(x)/int(y)*100)) + "%"
		except (ValueError, ZeroDivisionError):
			pass

main()
