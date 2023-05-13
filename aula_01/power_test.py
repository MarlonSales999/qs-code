import unittest
from power import power

class TestPower(unittest.TestCase):
    def test_base_zero(self):
        self.assertEqual(power(0, 2), 0)
        
    def test_expoente_zero(self):
        self.assertEqual(power(2, 0), 1)

    def test_base_negative(self):
        self.assertEqual(power(-2, 3), -8)
        
    def test_expoente_negative(self):
        self.assertEqual(power(2, -3), 0.125)
        
    def test_base_positive_expoente_negative(self):
        self.assertEqual(power(3, -2), 1/9)