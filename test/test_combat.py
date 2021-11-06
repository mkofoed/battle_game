import random
import unittest
from typing import Type

from objects.cards.units.units import TestUnit1, TestUnit2, Unit, unit_pool
from objects.combat import Combat
from objects.hand import Hand, CombatHand, RunHand
from settings import HAND_SIZE


class TestCombat(unittest.TestCase):

    def test_combat_1(self):
        hand1 = self.add_hand_of_units('1', TestUnit1)
        hand2 = self.add_hand_of_units('2', TestUnit2)
        combat = Combat(hand1, hand2)
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

    def test_lol(self):
        hand1 = self.add_hand_of_random_units("Hand 1")
        hand2 = self.add_hand_of_random_units("Hand 2")
        combat = Combat(hand1, hand2)
        combat.perform_combat()

    @staticmethod
    def add_hand_of_units(name: str, unit: Type[Unit]) -> CombatHand:
        run_hand = RunHand(name)
        combat_hand = CombatHand(run_hand)
        for i in range(HAND_SIZE):
            combat_hand.add_card(unit, i)
        return combat_hand

    @staticmethod
    def add_hand_of_random_units(name: str) -> CombatHand:
        run_hand = RunHand(name)
        cards = random.choices(unit_pool, k=HAND_SIZE)
        for i, card in enumerate(cards):
            run_hand.add_card(card, i)
        return CombatHand(run_hand)


if __name__ == '__main__':
    unittest.main()
