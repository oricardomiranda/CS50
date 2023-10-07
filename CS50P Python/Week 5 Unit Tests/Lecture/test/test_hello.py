#Testing folder. we need __init__.py file
from hello import hello

def test_default():
	assert hello() == "hello, world"

def test_argument():
	assert hello("Ric") == "hello, Ric"