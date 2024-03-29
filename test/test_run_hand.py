import unittest

import settings
from objects.cards.card import Card
from objects.cards.units.units import TestUnit1, TestUnit2
from objects.hand import RunHand
from settings import HAND_SIZE
from utils import card_is_empty, card_is_specific_unit


class TestRunHand(unittest.TestCase):

    def setUp(self) -> None:
        self.run_hand = RunHand("TEST HAND")

    def test_handsize(self):
        self.assertEqual(len(self.run_hand.get_hand()), settings.HAND_SIZE)

    def test_hand_is_empty(self):
        self.assertEqual(self.run_hand.is_empty(), True)
        for i in range(settings.HAND_SIZE):
            self.assertTrue(card_is_empty(self.run_hand, i))

    def test_add_single_unit(self):
        self.run_hand.add_card(TestUnit1, 0)
        self.assert_is_unit(0, TestUnit1)

    def test_add_two_units(self):
        self.run_hand.add_card(TestUnit2, 0)
        self.run_hand.add_card(TestUnit1, 1)
        self.assert_is_unit(0, TestUnit2)
        self.assert_is_unit(1, TestUnit1)

    def test_full_hand(self):
        for i in range(HAND_SIZE):
            self.run_hand.add_card(TestUnit1, i)
        for i in range(HAND_SIZE):
            self.assert_is_unit(i, TestUnit1)

    def test_swap_cards(self):
        self.run_hand.add_card(TestUnit2, 0)
        self.run_hand.add_card(TestUnit1, 1)
        self.assert_is_unit(0, TestUnit2)
        self.assert_is_unit(1, TestUnit1)
        self.run_hand.swap_card(0, 1)
        self.assert_is_unit(0, TestUnit1)
        self.assert_is_unit(1, TestUnit2)

    def test_swap_empty(self):
        self.run_hand.add_card(TestUnit1, 0)
        self.assertTrue(card_is_specific_unit(self.run_hand, 0, TestUnit1))
        self.assertTrue(card_is_empty(self.run_hand, 1))

    def assert_is_unit(self, index: int, card: Card):
        self.assertTrue(card_is_specific_unit(self.run_hand, index, card))


if __name__ == '__main__':
    unittest.main()
