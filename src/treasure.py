from tools import calculate_roll
from tools import load_cr_based_table
from tools import load_flat_table
from tools import filter_table_by_key
from random import randint
from spell_list import SpellList
import random


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

        self.spells = SpellList()

        # load the list of possible coins available
        self.coin_type = ['copper', 'silver', 'electrum', 'gold', 'platinum']

    def get_coins(self):
        """returns a dictionary with the quantity of each type of coin in the treasure hoard"""

        temp = load_cr_based_table('../tables/coins.csv', self.cr)
        # presently there is no d100 rolling for coins, but the table is loaded as a list to be consistent
        # with other tables
        coins_to_roll = temp[0]
        payout = {}

        for coin in self.coin_type:
            if coin in coins_to_roll:
                payout[coin] = calculate_roll(coins_to_roll[coin])

        return payout

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
        # roll and determine what magic items are in the stash
        if 'magic-roll' in payout:
            payout['magic-qty'] = calculate_roll(payout['magic-roll'])
            if 'magic-table' in payout:
                count = 1
                payout['magic-items'] = []
                while count <= payout['magic-qty']:
                    item_to_add = self.get_random_magic_item(payout['magic-table'])
                    # check for special logic
                    if 'logic' in item_to_add:
                        if item_to_add['logic'] == 'pick_spell':
                            spell_to_add = self.spells.get_random_spell_by_level(item_to_add['level'])
                            item_to_add['item'] = f"Level {item_to_add['level']} spell scroll: {spell_to_add['name']}"
                    payout['magic-items'].append(item_to_add)
                    count += 1

        if 'magic-roll2' in payout:
            payout['magic-qty2'] = calculate_roll(payout['magic-roll2'])
            if 'magic-table2' in payout:
                count = 1
                while count <= payout['magic-qty2']:
                    item_to_add = self.get_random_magic_item(payout['magic-table2'])
                    payout['magic-items'].append(item_to_add)
                    count += 1

        return payout

    def get_random_magic_item(self, table_key, roll=0):
        result = {}
        thisroll = 0
        # load the reference table
        temp_table = load_flat_table('../tables/magic_items.csv')
        """magic_item_table = []
        for row in temp_table:
            if row['key'] == table_key:
                magic_item_table.append(row)"""
        magic_item_table = filter_table_by_key(temp_table, table_key)


        # If a roll is not specified, pick a number between 1 and 100
        if roll == 0:
            # determine the maximum value for the roll, as it may be more than 100 with new content
            #thisroll = randint(1, 100)
            seq = [x['d100-max'] for x in magic_item_table]
            maxroll = max(seq)
            thisroll = randint(1, maxroll)
        else:
            thisroll = roll

        # Iterate through the list of magic items until the roll is matched
        for row in magic_item_table:
            if int(row['d100-min']) <= thisroll <= int(row['d100-max']):
                result['item'] = row['item']
                result['source'] = row['source']
                if 'logic' in row:
                    result['logic'] = row['logic']
                if 'level' in row:
                    result['level'] = row['level']
                break
        return result


if __name__ == "__main__":
    while (cr := input("Challenge Rating: ")) != "quit":
        myloot = TreasureHoard(cr)

        print(f"You rolled {myloot.roll}. Here is your challenge rating {cr} treasure hoard!")
        coin_stash = myloot.get_coins()
        for coin_type in coin_stash:
            print(f"   {coin_stash[coin_type]:,} pieces of {coin_type}")

        item_stash = myloot.get_items()
        if 'artifact-qty' in item_stash:
            print(
                f"   {item_stash['artifact-qty']} {item_stash['artifact-type']} worth {item_stash['artifact-gp-value']:,}"
                f" gold pieces each")
        if 'magic-qty' in item_stash:
            print(
                f"   {item_stash['magic-qty']} magical {'items' if item_stash['magic-qty']>1 else 'item'} from the "
                f"wondrous Magical Item table {item_stash['magic-table']}")
        if 'magic-qty2' in item_stash:
            print(
                f"   {item_stash['magic-qty2']} magical {'items' if item_stash['magic-qty2']>1 else 'item'} from the "
                f"wondrous Magical Item table {item_stash['magic-table2']}")
        if 'magic-items' in item_stash:
            for item in item_stash['magic-items']:
                print(f"   {item['item']} (source: {item['source']})")

        characteristic_list = ['friendly ', 'cantankerous', 'drunken', 'boisterous', 'jolly', 'merry', 'joyous',
                               'affectionate', 'genial', 'benevolent']
        monster_list = ['ogre', 'dragon', 'hydra', 'vampire', 'giant', 'beholder', 'tarrasque', 'lich', 'aboleth',
                        'gelatinous cube']
        pub_item = random.choice(characteristic_list)

        pub_item_2 = random.choice(monster_list)
        print("Now off to the", pub_item, pub_item_2, "to celebrate")
