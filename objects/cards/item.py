from objects.cards.card import Card


class Item(Card):
    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
