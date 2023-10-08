name = input("What's your name? ")

# open is the tool to access memory like double click
# best way to open and close the file automatically
with open("names.txt", "a") as file:
	file.write(f"{name}\n")

