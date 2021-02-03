import json
from tools import calculate_coins
from tools import load_table

class TreasureHoard:
    """Recreates the basic treasure hoard tables from D&D Dungeon master's guide... for now"""

    def __init__(self, cr=0):
        """Creates a new treasure hoard, requires a combat rating otherwise, defaults to 0"""
        self.cr = int(cr)
        self.coins = {}

        # load the coin payout table
        self.cointablekey = \
            [{'min': 0, 'max': 4, 'table': 'a'},
             {'min': 5, 'max': 10, 'table': 'b'},
             {'min': 11, 'max': 16, 'table': 'c'},
             {'min': 17, 'max': 99, 'table': 'd'}]

    def get_coins(self):
        payout = {}
        cointable = load_table('../tables/coins.csv')
        for set in self.cointablekey:
            if set['min'] <= self.cr <= set['max']:
                payout = cointable[set['table']]
        for loot in payout:
            self.coins[loot] = calculate_coins(payout[loot])
        return self.coins


if __name__ == "__main__":
    while (cr := input("Combat Rating: ")) != "quit":
        myloot = TreasureHoard(cr)
        print(myloot.get_coins())
