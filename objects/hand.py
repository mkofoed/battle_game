from typing import Optional

from objects.cards.card import Card, Empty
from objects.cards.units.units import Unit
from settings import HAND_SIZE


class Hand:
    name: str
    _cards: list[Unit]

    def __init__(self, name="HAND 1"):
        self.name = name
        self._cards = []
        self._add_initial_cards()

    def _add_initial_cards(self):
        for i in range(HAND_SIZE):
            self._cards.append(Empty(i))

    def get_hand(self) -> list[Unit]:
        return self._cards

    @property
    def is_empty(self) -> bool:
        return all(card.is_empty() for card in self.get_hand())

    def swap_card(self, start: int, end: int):
        self.get_hand()[start], self.get_hand()[end] = self.get_hand()[end], self.get_hand()[start]

    def add_card(self, unit: Unit, index: int):
        self._cards[index] = unit(index)

    def remove_card(self, index: int):
        self._cards[index] = Empty(index)

    def get_first_card(self) -> Optional[Unit]:
        non_empty_cards = [x for x in self.get_hand() if not x.is_empty() and x.combat_health > 0]
        if len(non_empty_cards) == 0:
            return None
        return non_empty_cards[-1]

    def initialize_combat(self) -> None:
        for card in self.get_non_empty():
            card.combat_attack = card.hand_attack
            card.combat_health = card.hand_health

    def is_defeated(self):
        return not any(x.combat_health > 0 for x in self.get_hand() if not x.is_empty())

    def get_non_empty(self):
        return [card for card in self.get_hand() if not card.is_empty()]

    def __str__(self):
        print_string = f'{self.name}: Cards in hand:\n'
        for card in self.get_hand():
            print_string += str(card) + '\n'
        return print_string
