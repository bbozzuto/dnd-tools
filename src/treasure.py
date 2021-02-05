from tools import calculate_roll
from tools import load_table
from tools import load_cr_based_table
from random import randint


class TreasureHoard:
    """Recreates the basic treasure hoard tables from D&D Dungeon master's guide... for now"""

    def __init__(self, cr=0, roll=0):
        """Creates a new treasure hoard, requires a combat rating otherwise, defaults to 0"""
        if str(cr).isnumeric():
            self.cr = int(cr)
        else:
            self.cr = 0
        self.coins = {}
        if roll == 0:
            self.roll = randint(1, 100)
        else:
            self.roll = int(roll)
        # load the coin payout table
        self.cointablekey = \
            [{'min': 0, 'max': 4, 'table': 'a'},
             {'min': 5, 'max': 10, 'table': 'b'},
             {'min': 11, 'max': 16, 'table': 'c'},
             {'min': 17, 'max': 99, 'table': 'd'}]

    def get_coins(self):
        """returns a dictionary with the quantity of each type of coin in the treasure hoard"""
        payout = {}
        cointable = load_table('../tables/coins.csv')
        for set in self.cointablekey:
            if set['min'] <= self.cr <= set['max']:
                payout = cointable[set['table']]
        for loot in payout:
            self.coins[loot] = calculate_roll(payout[loot])
        return self.coins

    def get_items(self):
        """returns a dictionary including artifacts and magic items"""
        payout = {}
        loot_table = load_cr_based_table('../tables/treasure_hoard.csv', self.cr)
        for row in loot_table:
            if int(row['d100-min']) <= self.roll <= int(row['d100-max']):
                payout = row
                self.items = row
                break
        if 'artifact-roll' in payout:
            payout['artifact-qty'] = calculate_roll(payout['artifact-roll'])
        if 'magic-roll' in payout:
            payout['magic-qty'] = calculate_roll(payout['magic-roll'])
        if 'magic-roll2' in payout:
            payout['magic-qty2'] = calculate_roll(payout['magic-roll2'])



        return payout




if __name__ == "__main__":
    while (cr := input("Combat Rating: ")) != "quit":
        myloot = TreasureHoard(cr)

        print(f"You rolled {myloot.roll}. Here is your challenge rating {cr} treasure hoard!")
        coin_stash = myloot.get_coins()
        for coin_type in coin_stash:
            print(f"   {coin_stash[coin_type]} pieces of {coin_type}")

        item_stash = myloot.get_items()
        if 'artifact-qty' in item_stash:
            print(f"   {item_stash['artifact-qty']} {item_stash['artifact-type']} worth {item_stash['artifact-gp-value']}"
                  f" gold pieces each")
        if 'magic-qty' in item_stash:
            print(f"   {item_stash['magic-qty']} magical items from the wondrous Magical Item table {item_stash['magic-table']}")
        if 'magic-qty2' in item_stash:
            print(f"   {item_stash['magic-qty2']} magical items from the wondrous Magical Item table {item_stash['magic-table2']}")


        print("Now off to the Friendly Ogre pub to celebrate!\n")


