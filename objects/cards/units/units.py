from objects.cards.card import Card


class Unit(Card):
    name: str
    base_attack: int
    base_health: int
    hand_attack: int
    hand_health: int
    combat_attack: int
    combat_health: int

    def __init__(self, hand_position):
        self.hand_position = hand_position
        self.hand_attack = self.base_attack
        self.hand_health = self.base_health

    def is_alive(self):
        return self.combat_health > 0

    def set_combat_stats(self):
        self.combat_health = self.hand_health
        self.combat_attack = self.hand_attack

    def take_damage(self, damage: int):
        self.combat_health -= damage

    def buff(self, attack: int, health: int):
        self.base_attack += attack
        self.base_health += health

    def __str__(self):
        return f'Spot: {self.hand_position} - Name: {self.name} - Atk/HP: {self.hand_attack}/{self.hand_health}'

    def __repr__(self):
        return self.__str__()


class TestUnit1(Unit):
    name = "1/1"
    base_attack = 1
    base_health = 1


class TestUnit2(Unit):
    name = "2/2"
    base_attack = 2
    base_health = 2


class Fish(Unit):
    name = "Fish"
    base_attack = 1
    base_health = 2


class Cat(Unit):
    name = "Cat"
    base_attack = 2
    base_health = 1


unit_pool = [
    Cat,
    Fish
]
