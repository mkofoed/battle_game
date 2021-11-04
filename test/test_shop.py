import unittest

from objects.shop import Shop


class TestShop(unittest.TestCase):

    def setUp(self) -> None:
        self.shop = Shop()

    def test_shop_hand_length(self):
        self.assertEqual(len(self.shop.get_hand()), 5)

    def lol(self):
        pass


if __name__ == '__main__':
    unittest.main()
