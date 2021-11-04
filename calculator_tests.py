"""Tests the methods of the Calculator class.

Typical usage example (in command-line interface):
>> python calculator_tests.py

"""

import unittest
from src.calculator import Calculator


class CalculatorTests(unittest.TestCase):
    """The CalculatorTests class is used to conduct unit tests on the Calculator class.
    """

    def setUp(self) -> None:
        self.calc = Calculator(3, 5)

    def test_add(self):
        """Tests the correctness of the addition operation."""
        self.assertEqual((8, None), self.calc.add())

    def test_subtract(self):
        """Tests the correctness of the subtraction operation."""
        self.assertEqual((-2, None), self.calc.subtract())

    def test_multiply(self):
        """Tests the correctness of the multiplication operation."""
        self.assertEqual((15, None), self.calc.multiply())

    def test_divide(self):
        """Tests the correctness of the division operation."""
        self.assertEqual((0.6, None), self.calc.divide())

    def test_divide_by_zero(self):
        """Tests the correctness of the ZeroDivisionError error response."""
        calc = Calculator(3, 0)
        self.assertEqual(
            (None, "Cannot divide by zero. Please select another operator or choose option 5 to reset inputs."),
            calc.divide()
        )


if __name__ == '__main__':
    unittest.main()

