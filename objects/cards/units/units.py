from objects.cards.card import Card


class Unit(Card):
    name: str
    attack: int
    health: int
    alive: bool = True

    def __init__(self, hand_position):
        self.hand_position = hand_position

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def buff(self, attack: int, health: int):
        self.attack += attack
        self.health += health

    def __str__(self):
        return f'{self.hand_position} - {self.name} - {self.attack}/{self.health}'

    def __repr__(self):
        return self.__str__()


class TestUnit1(Unit):
    name = "TEST1"
    attack = 0
    health = 0


class TestUnit2(Unit):
    name = "TEST2"
    attack = 0
    health = 0


class Fish(Unit):
    name = "Fish"
    attack = 1
    health = 2


class Cat(Unit):
    name = "Cat"
    attack = 2
    health = 1
