import unittest
from treasure import TreasureHoard


class TreasureHoardTests(unittest.TestCase):
    """Test for the treasure hoard class"""

    def test_get_coins_invalid_parameters(self):
        """when creating a treasure hoard with an invalid parameter, it should create based on a CR or 0"""
        testhoard = TreasureHoard('x')
        testcoins = testhoard.get_coins()
        self.assertGreaterEqual(testcoins['gold'], 20)  # there should be at least 2 gold coins
        self.assertLessEqual(testcoins['gold'], 120)  # there should not be more than 120 cold coins
        self.assertGreaterEqual(testcoins['silver'], 300)  # there should be at least 300 silver coins
        self.assertLessEqual(testcoins['silver'], 1800)  # there should not be more than 1800 cold coins
        self.assertGreaterEqual(testcoins['copper'], 600)  # there should be at least 600 copper coins
        self.assertLessEqual(testcoins['copper'], 3600)  # there should not be more than 3600 copper coins
        self.assertNotIn('electrum', testcoins)
        self.assertNotIn('platinum', testcoins)

    def test_get_coins_no_parameters(self):
        """when creating a treasure hoard with no parameters, it should create based on a CR or 0"""
        testhoard = TreasureHoard()
        testcoins = testhoard.get_coins()
        self.assertGreaterEqual(testcoins['gold'], 20)  # there should be at least 2 gold coins
        self.assertLessEqual(testcoins['gold'], 120)  # there should not be more than 120 cold coins
        self.assertGreaterEqual(testcoins['silver'], 300)  # there should be at least 300 silver coins
        self.assertLessEqual(testcoins['silver'], 1800)  # there should not be more than 1800 cold coins
        self.assertGreaterEqual(testcoins['copper'], 600)  # there should be at least 600 copper coins
        self.assertLessEqual(testcoins['copper'], 3600)  # there should not be more than 3600 copper coins
        self.assertNotIn('electrum', testcoins)
        self.assertNotIn('platinum', testcoins)

    def test_get_coins_cr_ten(self):
        """The coints returned should vary based on the CR rating passed. This will test based on the value
        for a CR of 10"""
        testhoard = TreasureHoard(10)
        testcoins = testhoard.get_coins()
        self.assertGreaterEqual(testcoins['copper'], 200)  # there should be at least 200 copper coins
        self.assertLessEqual(testcoins['copper'], 1200)  # there should not be more than 1200 copper coins
        self.assertGreaterEqual(testcoins['silver'], 2000)  # there should be at least 2000 silver coins
        self.assertLessEqual(testcoins['silver'], 12000)  # there should not be more than 12000 cold coins
        self.assertGreaterEqual(testcoins['gold'], 600)  # there should be at least 600 gold coins
        self.assertLessEqual(testcoins['gold'], 3600)  # there should not be more than 3600 cold coins
        self.assertGreaterEqual(testcoins['platinum'], 30)  # there should be at least 30 platinum coins
        self.assertLessEqual(testcoins['platinum'], 180)  # there should not be more than 180 platinum coins
        self.assertNotIn('electrum', testcoins)

    def test_get_coins_cr_twenty(self):
        """The coins returned should vary based on the CR rating passed. This will test based on the value
        for a CR of 20"""
        testhoard = TreasureHoard(20)
        testcoins = testhoard.get_coins()
        self.assertGreaterEqual(testcoins['gold'], 12000)  # there should be at least 4000 gold coins
        self.assertLessEqual(testcoins['gold'], 72000)  # there should not be more than 24000 cold coins
        self.assertGreaterEqual(testcoins['platinum'], 8000)  # there should be at least 30 platinum coins
        self.assertLessEqual(testcoins['platinum'], 48000)  # there should not be more than 180 platinum coins
        self.assertNotIn('copper', testcoins)
        self.assertNotIn('silver', testcoins)
        self.assertNotIn('electrum', testcoins)

if __name__ == '__main__':
    unittest.main()
