from objects.cards.units.units import Unit
from objects.hand import Hand
from settings import PLAYER_INITIAL_COINS, PLAYER_INITIAL_HEALTH


class Player:
    name: str
    coins: int
    hand: Hand
    wins: int
    losses: int
    health: int
    _cards: list[Unit]

    def __init__(self, name: str):
        self.name = name
        self.coins = PLAYER_INITIAL_COINS
        self.wins = 0
        self.losses = 0
        self.health = PLAYER_INITIAL_HEALTH
        self.hand = Hand(name)

    def __str__(self):
        return f'PLAYER: {self.name}'
