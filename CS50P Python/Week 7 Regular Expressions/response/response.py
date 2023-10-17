import validators

def main():
	print(validator(input("What's your email address? ")))


def validator(s):
	if validators.email(s) == True:
		return f"Valid"
	else:
		return f"Invalid"

if __name__ == "__main__":
	main()