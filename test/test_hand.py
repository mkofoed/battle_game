import unittest

from objects.cards.card import Empty, Card
from objects.cards.units.units import TestUnit1, TestUnit2, Unit
from objects.hand import RunHand
from settings import HAND_SIZE


class TestRunHand(unittest.TestCase):

    def setUp(self) -> None:
        self.run_hand = RunHand("TEST HAND")

    def test_handsize(self):
        self.assertEqual(len(self.run_hand.get_hand()), 5)

    def test_hand_is_empty(self):
        self.assertEqual(self.run_hand.is_empty(), True)

    def test_add_single_unit(self):
        self.run_hand.add_card(TestUnit1, 0)
        self.assert_is_unit(0, TestUnit1)

    def test_add_two_units(self):
        self.run_hand.add_card(TestUnit2, 0)
        self.run_hand.add_card(TestUnit1, 1)
        self.assert_is_unit(0, TestUnit2)
        self.assert_is_unit(1, TestUnit1)

    def test_add_all_fish(self):
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

    def assert_is_unit(self, index: int, card: Card):
        self.assertIsInstance(self.run_hand.get_hand()[index], card.__class__)


if __name__ == '__main__':
    unittest.main()
