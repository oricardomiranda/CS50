def main():
	word = input("Input: ")
	result = shorten(word)
	print("Output: " + result)

def shorten(word):
	result = ""
	for c in word:
		if c not in 'aeiouAEIOU': #If not vowel, add to variable
			result += c
	return result

if __name__ == "__main__":
	main()