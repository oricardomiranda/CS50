def converter(text):
	# :)
	text = text.replace(":)" , "🙂")

	# :(
	text = text.replace(":(", "🙁")

	return text

def main():

	emoji_text = input("Enter you text with emojis: ")

	emoji_text = converter(emoji_text)

	print(emoji_text)


if __name__ == "__main__":
	main()