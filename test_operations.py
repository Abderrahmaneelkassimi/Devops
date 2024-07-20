import unittest
from operations import add, subtract, multiply, divide

class TestOperations(unittest.TestCase):

    def test_add_operation_returns_correct_value(self):
        print("Running test_add_operation_returns_correct_value")
        self.assertEqual(add(10, 90), 100)

    def test_subtract_operation_returns_correct_value(self):
        print("Running test_subtract_operation_returns_correct_value")
        self.assertEqual(subtract(100, 90), 10)  # This should fail

    def test_multiply_operation_returns_correct_value(self):
        print("Running test_multiply_operation_returns_correct_value")
        self.assertEqual(multiply(10, 10), 100)

    def test_division_operation_returns_correct_value(self):
        print("Running test_division_operation_returns_correct_value")
        self.assertEqual(divide(100, 10), 10)

    def test_division_operation_returns_error_when_divided_by_zero(self):
        print("Running test_division_operation_returns_error_when_divided_by_zero")
        self.assertEqual(divide(10, 0), "Zero Division Error!")

if __name__ == '__main__':
    unittest.main()

