import unittest

from exceptions import HandActionNotAllowedException
from objects.cards.units.units import TestUnit1
from objects.shop import Shop


class TestShop(unittest.TestCase):

    def setUp(self) -> None:
        self.shop = Shop()

    def test_shop_hand_length(self):
        self.assertEqual(len(self.shop.get_hand()), 5)

    def test_swap_card_raises_exception(self):
        with self.assertRaises(HandActionNotAllowedException):
            self.shop.swap_card(0, 1)

    def test_add_card_raises_exception(self):
        with self.assertRaises(HandActionNotAllowedException):
            self.shop.add_card(TestUnit1, 0)


if __name__ == '__main__':
    unittest.main()
