import random

from exceptions.exceptions import HandActionNotAllowedException
from objects.cards.units.cat import Cat
from objects.cards.units.dog import Dog
from objects.cards.units.fish import Fish
from objects.cards.units.units import Unit
from objects.hand import Hand
from settings import UNITS_IN_SHOP, shop_unit_pool

unit_pool = [unit for unit in [Cat, Fish, Dog] if unit.name in shop_unit_pool]


class Shop(Hand):
    """
    Object to store the cards in the shop. Behaves much like a RoundHand.
    """

    def __init__(self) -> None:
        super().__init__()
        self.roll_shop_hand(1)

    def roll_shop_hand(self) -> None:
        self._cards = random.choices(shop_unit_pool, k=UNITS_IN_SHOP)

    def swap_card(self, start: int, end: int) -> None:
        raise HandActionNotAllowedException(self, f'Not allowed to swap cards in Shop')

    def add_card(self, unit: Unit, index: int) -> None:
        raise HandActionNotAllowedException(self, f'Not allowed to add cards in Shop')
