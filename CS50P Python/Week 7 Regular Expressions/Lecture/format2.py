import re

name = input("What's your name? ").strip()
if matches := re.search(r"(.+), ?(.+)$", name): #UALRUS operator is recent in python. Makes it more concise
	name = matches.group(2) + " " + matches.group(1) #second set of parenthesis in line 4 + space + first set of parenthesis in line 4
print(f"hello, {name}")
