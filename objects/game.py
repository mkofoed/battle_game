from objects.hand import Hand
from objects.shop import Shop


class Game:
    current_round: int
    hand: Hand
    shop: Shop

    def __init__(self):
        current_round = 1
        hand = Hand()
        shop = Shop()
