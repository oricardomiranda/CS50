from um import count

def test():
	assert count("Um, gotcha!") == 1
	assert count("um") == 1
	assert count("Um, yeah, um...") == 2
	assert count("Um?") == 1

if __name__ == "__main__":
    test()