

from operations import *
print("Running test_add_operation_returns_correct_value")

from operations import add

def test_add():
    assert add(2, 3) == 5

if __name__ == "__main__":
    print("Running test_add_operation_returns_correct_value")
    test_add()
