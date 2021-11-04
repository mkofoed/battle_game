from __future__ import annotations
from abc import ABC, abstractmethod

import objects.hand


class Card(ABC):
    name: str
    type: str
    value: int
    hand_position: int
    hand: objects.hand.Hand

    def __init__(self, hand: objects.hand.Hand):
        self.hand = hand

    def set_position(self, index: int):
        self.hand_position = index

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError
