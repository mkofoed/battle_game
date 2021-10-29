import unittest

from objects.player import Player
from settings import PLAYER_INITIAL_COINS, PLAYER_INITIAL_HEALTH


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_initial(self):
        player1 = Player("Player 1")
        self.assertEqual(player1.coins, PLAYER_INITIAL_COINS)
        self.assertEqual(player1.health, PLAYER_INITIAL_HEALTH)
        self.assertEqual(player1.wins, 0)
        self.assertEqual(player1.losses, 0)
        self.assertTrue(player1.hand.is_empty)


if __name__ == '__main__':
    unittest.main()
