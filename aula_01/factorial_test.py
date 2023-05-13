import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_positive(self):
        self.assertEqual(factorial(5), 120)
        
    def test_negative(self):
        self.assertEqual(factorial(-3), None)
        
    def test_float(self):
        self.assertEqual(factorial(2.5), None)
        
    def test_string(self):
        self.assertEqual(factorial('abc'), None)
        
    def test_large_number(self):
        self.assertEqual(factorial(1000), None)