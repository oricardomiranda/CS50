from bank import value

def main():
	test_positive()
	test_negative()
	test_corner()

def test_positive():
	assert value("Hello") == 0
	assert value("Hello, Newman") == 0
def test_negative():
	assert value("How you doing?") == 20
	assert value("What's happening?") == 100
def test_corner():
	assert value("HELLO") == 0
	assert value ("hello") == 0


if __name__ == "__main__":
	main()