import unittest
from figuree import calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = calc()
    def test_s_circl(self):
        self.assertEqual(self.calc.calc_S_circkl(5), 78.53982)
    def test_s_tring(self):
        self.assertEqual(self.calc.calc_S_tringle(3,7,5), 6.49519)
    
if __name__ == "__main__":
    unittest.main()
