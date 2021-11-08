from abc import ABC

from objects.enums import HandTarget


class Action(ABC):
    target_hand: HandTarget


class FriendlyAction:
    target_hand = HandTarget.friendly


class EnemyAction:
    target_hand = HandTarget.enemy


class FullHandAction(Action):
    pass


class SingleUnitAction(Action):
    pass


class BuffMySingleUnit(Action):
    pass


class BuffEnemySingleUnit(Action):
    pass


class DamageMySingleUnit(Action):
    pass
