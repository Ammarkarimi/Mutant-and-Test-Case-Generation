from unittest import TestCase
from input.calculator import mul

class CalculatorTest(TestCase):

    def test_mul(self):
        self.assertEqual(mul(2, 2), 4)
        