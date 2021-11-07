import random

from exceptions.exceptions import HandActionNotAllowedException
from objects.cards.units.units import Unit, unit_pool
from objects.hand import Hand
from settings import UNITS_IN_SHOP


class Shop(Hand):
    """
    Object to store the cards in the shop. Behaves much like a RoundHand
    """

    def __init__(self) -> None:
        super().__init__()
        self.roll_shop_hand(1)

    def roll_shop_hand(self, current_round: int) -> None:
        self._cards = random.choices(unit_pool, k=UNITS_IN_SHOP)

    def swap_card(self, start: int, end: int) -> None:
        raise HandActionNotAllowedException(self, f'Not allowed to swap cards in Shop')

    def add_card(self, unit: Unit, index: int) -> None:
        raise HandActionNotAllowedException(self, f'Not allowed to add cards in Shop')
