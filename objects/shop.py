from random import random

from objects.cards.units.units import Unit, unit_pool
from settings import UNITS_IN_SHOP


class Shop:
    _units: list[Unit]

    def __init__(self):
        self.roll_shop()

    def roll_shop(self):
        self._units = random.choices(unit_pool, k=UNITS_IN_SHOP)

    @property
    def units(self):
        return self._units

