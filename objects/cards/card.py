from abc import ABC, abstractmethod


class Card(ABC):
    name: str
    type: str
    value: int
    hand_position: int

    def is_empty(self):
        return isinstance(self, Empty)

    def set_position(self, index: int):
        self.hand_position = index

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError


class Empty(Card):
    name = 'Empty'

    def __init__(self, hand_position):
        self.hand_position = hand_position

    def __str__(self):
        return f'{self.hand_position} - {self.name}'

    __repr__ = __str__
