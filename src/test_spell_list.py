import unittest
import spell_list

class SpellListTests(unittest.TestCase):
    """Tests for the spell list class, which is used to get a selection of spells based on different criteria"""

    def test_get_random_spell_by_level(self):
        """Specify a level and return a spell that is according to that level"""
        test_spell_list = spell_list.SpellList()
        level_one_test_spell = test_spell_list.get_random_spell_by_level(1)
        level_five_test_spell = test_spell_list.get_random_spell_by_level(5)
        level_nine_test_spell = test_spell_list.get_random_spell_by_level(9)
        self.assertEqual(1, level_one_test_spell['level'])
        self.assertEqual(5, level_five_test_spell['level'])
        self.assertEqual(9, level_nine_test_spell['level'])