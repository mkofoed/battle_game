from objects.cards.card import Card
from objects.hand import Hand


class ActionNotAllowedException(Exception):
    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'An action was not allowed'
        super().__init__(msg)


class CardActionNotAllowedException(ActionNotAllowedException):
    def __init__(self, card: Card):
        msg = f'Action was not allowed for card: {card}'
        super().__init__(msg=msg)
        self.card = card


class HandActionNotAllowedException(ActionNotAllowedException):
    def __init__(self, hand: Hand, msg: str = None):
        if msg is None:
            msg = f'Action was not allowed for hand: {hand}'
        super().__init__(msg=msg)
        self.hand = Hand
