from objects.cards.card import Card
from objects.cards.empty import Empty
from settings import *


class Hand:
    _cards: list[Card]

    def __init__(self):
        self._cards = []
        self._add_initial_cards()

    def _add_initial_cards(self):
        for i in range(HAND_SIZE):
            self._cards.append(Empty(i))

    @property
    def hand(self) -> list[Card]:
        return self._cards

    def swap_card(self, start: int, end: int):
        self.hand[start], self.hand[end] = self.hand[end], self.hand[start]

    def add_card(self, card: Card, index: int):
        self._cards[index] = card(index)

    def remove_card(self, index: int):
        raise NotImplementedError

    def __str__(self):
        print_string = 'Cards in hand:\n'
        for card in self.hand:
            print_string += str(card) + '\n'
        return print_string






