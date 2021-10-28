from objects.cards.card import Card


class Empty(Card):
    name = 'Empty'

    def __init__(self, hand_position):
        self.hand_position = hand_position

    def __str__(self):
        return f'{self.hand_position} - {self.name}'

    __repr__ = __str__

