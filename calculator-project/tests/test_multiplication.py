import unittest
from src.operations.multiplication import multiply

class TestMultiplication(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(multiply(2, -3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(multiply(2.5, 0.4), 1.0)

if __name__ == '__main__':
    unittest.main()