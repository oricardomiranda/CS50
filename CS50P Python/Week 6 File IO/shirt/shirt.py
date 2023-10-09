import sys
from PIL import Image, ImageOps
import os

def main():
	if len(sys.argv) < 3:
		sys.exit("Too few arguments")
	elif len(sys.argv) > 3:
		sys.exit("too many arguments")
	else:
		format = [".jpg",".jpeg",".png"]
		before = os.path.splitext(sys.argv[1])
		after = os.path.splitext(sys.argv[2])
		if after[1].lower() not in format: # [1] searches the second element, in this case the extension
			sys.exit("Invalid output extension")
		elif before[1].lower() != after[1].lower():
			sys.exit("Files have different extensions")
		else:
			shirt(sys.argv[1], sys.argv[2])

def shirt(before, after):
	try:
		shirt = Image.open("shirt.png")
		with Image.open(before) as before:
			before_crop = ImageOps.fit(before, shirt.size)
			before_crop.paste(shirt, mask = shirt)
			before_crop.save(after)
	except FileNotFoundError:
		sys.exit("File not found")

if __name__ == "__main__":
	main()