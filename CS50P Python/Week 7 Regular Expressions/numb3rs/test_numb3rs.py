from numb3rs import validate

def main():
	test_zero()
	test_mid()
	test_max()
	test_over()
	test_dotless()
	test_comma()
	test_first_byte()
	test_four_digits()
	test_letter()
	test_one_to_four()
	test_first_correct()

def test_zero():
	assert validate("0.0.0.0")

def test_mid():
	assert validate("127.0.0.1")

def test_max():
	assert validate("255.255.255.255")

def test_over():
	assert not validate("256.256.256.256")

def test_dotless():
	assert not validate("255255255255")

def test_comma():
	assert not validate("255,255,255,255")

def test_first_byte():
    assert not validate("256.0.0.0")

def test_four_digits():
	assert not validate("1.2.3.1000")

def test_letter():
	assert not validate("cat")

def test_one_to_four():
	assert validate("1.2.3.4")

def test_first_correct():
    assert not validate("199.911.288.882")


if __name__ == "__main__":
	main()

