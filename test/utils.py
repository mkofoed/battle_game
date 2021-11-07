from objects.cards.card import Card
from objects.cards.unit import Unit
from objects.hand import Hand


class TestHelpers:

    @staticmethod
    def card_is_specific_unit(hand: Hand, index: int, card: Card):
        return isinstance(hand.get_hand()[index], card)

    @staticmethod
    def card_is_any_unit(hand: Hand, index: int):
        return hand.get_hand()[index] is Unit

    @staticmethod
    def card_is_empty(hand: Hand, index: int):
        return hand.get_hand()[index] is None


