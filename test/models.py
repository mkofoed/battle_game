import unittest

from objects.cards.empty import Empty
from objects.cards.units.units import *
from objects.hand import Hand
from settings import HAND_SIZE


class TestModels(unittest.TestCase):

    def setUp(self) -> None:
        self.hand = Hand()

    def test_handsize(self):
        self.assertEqual(len(self.hand.hand), 5)

    def test_empty_card(self):
        self.assert_is_card(0, Empty)

    def test_add_single_fish(self):
        self.hand.add_card(Fish, 0)
        self.assert_is_card(0, Fish)

    def test_add_single_cat(self):
        self.hand.add_card(Cat, 0)
        self.assert_is_card(0, Cat)

    def test_add_two_units(self):
        self.hand.add_card(Cat, 0)
        self.hand.add_card(Fish, 1)
        self.assert_is_card(0, Cat)
        self.assert_is_card(1, Fish)

    def test_add_all_fishes(self):
        for i in range(HAND_SIZE):
            self.hand.add_card(Fish, i)
        for i in range(HAND_SIZE):
            self.assert_is_card(i, Fish)

    def assert_is_card(self, index: int, card: Card):
        self.assertIsInstance(self.hand.hand[index], card)


if __name__ == '__main__':
    unittest.main()
