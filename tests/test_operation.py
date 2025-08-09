from src.math_operations import add, subtract ,multiplication, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 0) == 0
def test_divide():
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(0, 0) == None
