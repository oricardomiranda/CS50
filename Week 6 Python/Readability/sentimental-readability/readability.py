
def main():
	sentence = input("Text: ")

	letters = count_letters(sentence)
	words = count_words(sentence)
	sentences = count_sentences(sentence)

	average_letters = (100 / float(words) * float(letters))
	average_sentences = (100 / float(words) * float(sentences))

	index = calculate_index(average_letters, average_sentences)

	if index < 1:
		print("Before Grade 1")
	if index > 16:
		print("Grade 16+")
	else:
		print(f"Grade: {index}")


def count_letters(sentence):
	letters = 0

	for char in sentence:
		if char.isalpha():
			letters += 1

	return letters

def count_words(sentence):

	return len(sentence.split())

def count_sentences(sentence):
	sentences = 0

	for char in sentence:
		if char in [".", "!", "?"]:
			sentences += 1

	return sentences

def calculate_index(average_letters,average_sentences):
	index = 0.0588 * average_letters - 0.296 * average_sentences - 15.8
	return round(index)

if __name__ == "__main__":
	main()
