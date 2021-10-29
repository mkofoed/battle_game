import unittest

from objects.cards.units.units import *
from objects.combat import Combat
from objects.hand import Hand
from settings import HAND_SIZE


class TestCombat(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_combat_1(self):
        hand1 = self.add_hand_of_units('1', TestUnit1)
        hand2 = self.add_hand_of_units('2', TestUnit2)
        combat = Combat(hand1, hand2)
        combat.perform_combat()
        self.assertIsInstance(combat.winner, Hand)
        self.assertIs(combat.winner, hand2)

    def test_combat_2(self):
        hand1 = self.add_hand_of_units('1', TestUnit2)
        hand2 = self.add_hand_of_units('2', TestUnit1)
        combat = Combat(hand1, hand2)
        combat.perform_combat()
        self.assertIsInstance(combat.winner, Hand)
        self.assertIs(combat.winner, hand1)

    def test_self_draw(self):
        hand = self.add_hand_of_units('1', TestUnit1)
        combat = Combat(hand, hand)
        combat.perform_combat()
        self.assertIsNone(combat.winner)

    @staticmethod
    def add_hand_of_units(name: str, unit: Unit) -> Hand:
        hand = Hand(name)
        for i in range(HAND_SIZE):
            hand.add_card(unit, i)
        return hand


if __name__ == '__main__':
    unittest.main()
