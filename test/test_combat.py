import unittest

from utils import add_hand_of_units, add_hand_of_random_units
from objects.cards.units.units import TestUnit1, TestUnit2
from objects.combat import Combat
from objects.hand import Hand


class TestCombat(unittest.TestCase):

    def test_combat_1(self):
        hand1 = add_hand_of_units('1', TestUnit1)
        hand2 = add_hand_of_units('2', TestUnit2)
        combat = Combat(hand1, hand2)
        combat.perform_combat()
        self.assertIsInstance(combat.winner, Hand)
        self.assertIs(combat.winner, hand2)

    def test_combat_2(self):
        hand1 = add_hand_of_units('1', TestUnit2)
        hand2 = add_hand_of_units('2', TestUnit1)
        combat = Combat(hand1, hand2)
        combat.perform_combat()
        self.assertIsInstance(combat.winner, Hand)
        self.assertIs(combat.winner, hand1)

    def test_self_draw(self):
        hand = add_hand_of_units('1', TestUnit1)
        combat = Combat(hand, hand)
        combat.perform_combat()
        self.assertIsNone(combat.winner)

    def test_lol(self):
        hand1 = add_hand_of_random_units("Hand 1")
        hand2 = add_hand_of_random_units("Hand 2")
        combat = Combat(hand1, hand2)
        combat.perform_combat()


if __name__ == '__main__':
    unittest.main()
