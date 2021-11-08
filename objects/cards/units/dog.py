from objects.cards.unit import Unit


class Dog(Unit):
    def pre_combat_action(self):
        pass

    def pre_turn_action(self):
        pass

    name = "Dog"
    tier = 2
    base_attack = 1
    base_health = 3
