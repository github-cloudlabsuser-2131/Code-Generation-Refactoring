import unittest
from src.operations.subtraction import subtract

class TestSubtraction(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)
        
    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -10), 5)
        
    def test_zero(self):
        self.assertEqual(subtract(0, 0), 0)
        
    def test_subtracting_zero(self):
        self.assertEqual(subtract(5, 0), 5)
        
    def test_large_numbers(self):
        self.assertEqual(subtract(1000000, 999999), 1)

if __name__ == '__main__':
    unittest.main()