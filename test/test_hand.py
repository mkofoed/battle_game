import unittest

from objects.cards.card import Empty
from objects.cards.units.units import *
from objects.hand import Hand
from settings import HAND_SIZE


class TestModels(unittest.TestCase):

    def setUp(self) -> None:
        self.hand = Hand("NAME")

    def test_handsize(self):
        self.assertEqual(len(self.hand.hand), 5)

    def test_is_defeated(self):
        self.assertEqual(self.hand.is_defeated(), True)

    def test_empty_card(self):
        self.assert_index_is_card(0, Empty)

    def test_hand_is_empty(self):
        self.assertEqual(self.hand.is_empty, True)

    def test_add_single_fish(self):
        self.hand.add_card(TestUnit1, 0)
        self.assert_index_is_card(0, TestUnit1)

    def test_add_single_cat(self):
        self.hand.add_card(TestUnit1, 0)
        self.assert_index_is_card(0, TestUnit1)

    def test_add_two_units(self):
        self.hand.add_card(TestUnit2, 0)
        self.hand.add_card(TestUnit1, 1)
        self.assert_index_is_card(0, TestUnit2)
        self.assert_index_is_card(1, TestUnit1)

    def test_add_all_fish(self):
        for i in range(HAND_SIZE):
            self.hand.add_card(TestUnit1, i)
        for i in range(HAND_SIZE):
            self.assert_index_is_card(i, TestUnit1)

    def test_swap_cards(self):
        self.hand.add_card(TestUnit2, 0)
        self.hand.add_card(TestUnit1, 1)
        self.assert_index_is_card(0, TestUnit2)
        self.assert_index_is_card(1, TestUnit1)
        self.hand.swap_card(0, 1)
        self.assert_index_is_card(0, TestUnit1)
        self.assert_index_is_card(1, TestUnit2)

    def assert_index_is_card(self, index: int, card: Card):
        self.assertIsInstance(self.hand.hand[index], card)


if __name__ == '__main__':
    unittest.main()
