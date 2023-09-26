# Input to lower
phrase = input("Input: ")
phrase = str(phrase)

# Initialize variable
result = ""

# Run the string and skip vowels
for c in phrase:
	if c not in 'aeiouAEIOU': #If not vowel, add to variable
		result += c

# Print
print("Output: " + result)