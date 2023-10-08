name = input("What's your name? ")

# open is the tool to access memory like double click
#file = open("names.txt", "w") #name of the file and write permission, if does not exist, will be created. It erases the previous file
file = open("names.txt", "a")
file.write(f"{name}\n") #making changes
file.close() #save and close

#there is a better way to open and close in names3.py

