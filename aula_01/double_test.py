import unittest
from double import double

class TestDouble(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(double(2), 4)
        
    def test_negative_number(self):
        self.assertEqual(double(-2), 4)
        
    def test_zero(self):
        self.assertEqual(double(0), 0)




