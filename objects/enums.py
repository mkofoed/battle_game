from enum import Enum


class HandTarget(Enum):
    friendly = 'friendly'
    enemy = 'enemy'


class SingleUnitOrMultiple(Enum):
    single = 'single'
    multiple = 'multiple'


class UnitTargets(Enum):
    all = 'all'
    previous = 'previous'
    subsequent = 'subsequent'
    first = 'first'
    last = 'last'
    self = 'self'
    others = 'others'
