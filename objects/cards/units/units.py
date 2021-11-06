from objects.cards.unit import Unit


class TestUnit1(Unit):
    name = "Test unit 1/1"
    base_attack = 1
    base_health = 1


class TestUnit2(Unit):
    name = "Test unit 2/2"
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


class Dog(Unit):
    name = "Dog"
    base_attack = 1
    base_health = 3


unit_pool = [
    Cat,
    Fish,
    Dog
]
