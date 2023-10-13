import re

#re.search(pattern,string,flags=0)


email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
	#One or more repetitions @ one or more repetitions #r for raw string
	#[a-zA-Z_] can be traded by \w
	# other searches \d decimal \D non decimal \s whitespace \S non white space \w word+number + underscore \w not a word
	# re.IGNORECASE to make case insensitive
	print("Valid")
else:
	print("Invalid")