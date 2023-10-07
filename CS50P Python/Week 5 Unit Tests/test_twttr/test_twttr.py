from twttr import shorten

def main():
	test_upper()
	test_lower()
	test_vogal()
	test_consonant()
	test_number()
	test_special()

def test_upper():
	assert shorten("TWITTER") == "TWTTR"
def	test_lower():
	assert shorten("twitter") == "twttr"
def	test_vogal():
	assert shorten("aeiou") == ""
def	test_consonant():
	assert shorten("bcdfghjklpqrtvwxyz") == "bcdfghjklpqrtvwxyz"
def	test_number():
	assert shorten("0123456789") == "0123456789"
def	test_special():
	assert shorten("!#$%&/()=?*") == "!#$%&/()=?*"

if __name__ == "__main__":
	main()