from tools import load_flat_table
from random import choice


class SpellList:

    def __init__(self):
        self.all_spells = load_flat_table('../tables/spells.csv')

    def get_random_spell_by_level(self, level):
        # return {'name':'test spell', 'level':1}
        random_spell = choice(self.get_spells_by_levels([level]))
        return random_spell

    def get_spells_by_levels(self, level_list):
        """takes a list of levels and only returns spells within that list"""
        spell_list = [s for s in self.all_spells if s['level'] in level_list]

        return spell_list
