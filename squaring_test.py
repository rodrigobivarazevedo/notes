import unittest

from squaring import (
    square_visual,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class SquareVisual(unittest.TestCase):
    def test_three_digits(self):
        integer = 123
        self.assertRaises(ValueError, square_visual, integer)

    def test_nine_digits(self):
        integer = 123_889_999
        squared = [['1','2','3'],['8','8','9'],['9','9','9']]
        self.assertEqual(square_visual(integer), squared)

    def test_ten_digits(self):
        integer = 1234567891
        squared = [['1','2','3'],['4','5','6'],['7','8','9']]
        self.assertEqual(square_visual(integer), squared)

    # For extra points. CAUTION though, str() will cut off after 18 digits ;-)
    def test_long_float(self):
        floating = 1.234567891011121314151617181920
        squared = [['1','.','2','3','4'],['5','6','7','8','9'],['1','0','1','1','1'],['2','1','3','1','4'],['1','5','1', '6', '1']]
        self.assertEqual(square_visual(floating), squared)

    def test_short_float(self):
        floating = 1.234567891011121
        squared = [['1','.','2','3'],['4','5','6','7'],['8','9','1','0'],['1','1','1','2']]
        self.assertEqual(square_visual(floating), squared)


if __name__ == "__main__":
    unittest.main()
