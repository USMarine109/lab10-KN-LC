# https://github.com/USMarine109/lab10-swe
# Partner 1: Kenneth Nguyen
# Partner 2: Lauren Castello

import unittest
from calculator import add, subtract, mul, div, logarithm, hypotenuse, square_root
import math


class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-6, 7), 1)
        self.assertEqual(add(0, 2), 2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(6, 3), 3)
        self.assertEqual(subtract(-2, -2), 0)
        self.assertEqual(subtract(0, 5), -5)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(12, 12), 144)

    def test_divide(self): 
        self.assertAlmostEqual(div(3, 0), 0),# 3 assertions
        self.assertEqual(div(12, 3), 4)
        self.assertAlmostEqual(div(12, 5), 2.4)
    # ##########################

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 9)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(math.e, math.e**2), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    
    ######## Partner 1
    def test_log_invalid_argument(self):
        self.assertEqual(logarithm(0,4)) # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): 
        self.assertAlmostEqual(hypotenuse(7,6), 9.22)# 3 assertions
        self.assertEqual(hypotenuse(8,6), 10)
        self.assertAlmostEqual(hypotenuse(2,5), 5.39)


    def test_sqrt(self): 
        self.assertEqual(square_root(-4))
        self.assertAlmostEqual(square_root(1))
        self.assertEqual(square_root(16))
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()