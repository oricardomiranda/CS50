import re

#re.search(pattern,string,flags=0)

def main():
	email = input("What's your email? ").strip()

	if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
		#A|B either A or B
		#(...) a group
		#(?:...) non-capturing version
		# . any char except \n
		# * 0 or more
		# + 1 or more
		# ? 0 or 1
		# {m} n repetitions
		# {m,n} m-n repetitions
		# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
		print("Valid")
	else:
		print("Invalid")

if __name__ == "__main__":
	main()