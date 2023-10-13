email = input("What's your email? ").strip()

username, domain = email.split("@") #Will split my string into two

if (username) and ("." in domain):
	print("Valid")
else:
	print("Invalid")