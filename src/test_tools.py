import unittest
from tools import calculate_roll


class Calculate_Coins_Tests(unittest.TestCase):
    def test_basic_coin_calculations(self):
        """the basic function expects [number of dice]d[dice faces]x[modifier] and returns a random number
        as if the dice were rolled"""
        result = calculate_roll('3d6x10')

        self.assertGreaterEqual(result, 30)
        self.assertLessEqual(result, 180)

    def test_calculation_no_multiplier(self):
        """"the function should work with no multiplier provided"""
        result = calculate_roll('10d4')

        self.assertGreaterEqual(result, 10)
        self.assertLessEqual(result, 40)

    def test_calculation_invalid_format(self):
        """"if the format is not respected, the function should throw a type error"""
        with self.assertRaises(Exception): calculate_roll("xyz")
        with self.assertRaises(Exception): calculate_roll("18x6d10")
        with self.assertRaises(Exception): calculate_roll("6d10x10x")
        with self.assertRaises(Exception): calculate_roll("1dx10")


if __name__ == '__main__':
    unittest.main()
