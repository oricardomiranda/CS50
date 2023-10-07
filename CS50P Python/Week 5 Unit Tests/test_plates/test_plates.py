from plates import is_valid

def main():
	test_is_valid()

def test_is_valid():
	assert is_valid("CS50") is True
	assert is_valid("CS05") is False
	assert is_valid("CS50P") is False
	assert is_valid("PI3.14") is False
	assert is_valid("H") is False
	assert is_valid("OUTATIME") is False

if __name__ == "__main__":
    main()