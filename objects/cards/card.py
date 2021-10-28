from abc import ABC, abstractmethod


class Card(ABC):
    name: str
    type: str
    value: int
    hand_position: int

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

