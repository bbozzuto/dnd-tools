import random
from tools import calculate_coins

class TreasureHoard:
    """Recreates the basic treasure hoard tables from D&D Dungeon master's guide... for now"""

    def __init__(self, cr = 0):
        """Creates a new treasure hoard, requires a combat rating otherwise, defaults to 0"""
        self.cr = cr
        self.coins = {}


    def get_coins(self):
        payout = {'copper': "6d6x100", 'silver': "3d6x100", 'gold': "2d6x10"}
        for loot in payout:
            print(f"{loot}: {calculate_coins(payout[loot])}")
        return payout




if __name__ == "__main__":
    myloot = TreasureHoard(0)
    print(myloot.get_coins())
