#Using pytest
#In terminal: pytest <file.py>
from calculator import square
import pytest

#Calling tests
def main():
    test_square_positive()
    test_square_negative()
    test_square_null()

#Test 1
def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9
#Test2
def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9
#Test3
def test_square_null():
    assert square(0) == 0
#Test string(for this we need to import pytest.raises())
def test_str():
    with pytest.raises(TypeError):
        square("cat") #We give an example of string

#Calling main
if __name__ == "__main__":
    main()
