from abc import ABC
from typing import Optional

from objects.cards.card import Empty, Card
from objects.cards.units.units import Unit
from settings import HAND_SIZE


class Hand(ABC):
    """
    Base class for the different types of Hands
    """
    name: str
    _cards: list[Card]

    def __init__(self, name="HAND"):
        self.name = name

    def get_hand(self) -> list[Card]:
        return self._cards

    def is_empty(self) -> bool:
        return all(card.is_empty() for card in self.get_hand())

    def swap_card(self, start: int, end: int) -> None:
        hand = self.get_hand()
        hand[start], hand[end] = hand[end], hand[start]

    def add_card(self, unit: Unit, index: int) -> None:
        self._cards[index] = unit
        unit.hand_position = index

    def remove_card(self, index: int) -> None:
        self._cards[index] = Empty(index)

    def get_non_empty(self) -> list[Card]:
        return [card for card in self.get_hand() if not card.is_empty()]

    def __str__(self) -> str:
        print_string = f'{self.name}: Cards in hand:\n'
        for card in self.get_hand():
            print_string += str(card) + '\n'
        return print_string


class RunHand(Hand):
    """
    The hand used in a run. This hand is used in multiple rounds.
    """

    def __init__(self, name="HAND"):
        super().__init__(name)
        self._cards = []
        self._add_initial_cards()

    def _add_initial_cards(self):
        for i in range(HAND_SIZE):
            self._cards.append(Empty(i))

    def get_first_card(self):
        non_empty = self.get_non_empty()
        return None if non_empty is None else non_empty[-1]

    def to_combat_hand(self):
        return CombatHand(self)


class CombatHand(Hand):
    """
    A hand used for a single combat generated from a RunHand
    """

    def __init__(self, run_hand: RunHand):
        super().__init__(run_hand.name)
        self._cards = run_hand.get_hand()

    def get_active_unit(self) -> Optional[Unit]:
        non_empty_cards = [card for card in self.get_non_empty() if card.is_alive() is True]
        if len(non_empty_cards) == 0:
            return None
        return non_empty_cards[-1]

    def is_defeated(self):
        return not any(x.combat_health > 0 for x in self.get_hand() if not x.is_empty())

    def initialize_combat(self) -> None:
        for card in self.get_non_empty():
            card.combat_attack = card.hand_attack
            card.combat_health = card.hand_health
