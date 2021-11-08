from objects.cards.unit import Unit


class Cat(Unit):
    def pre_combat_action(self):
        pass

    def pre_turn_action(self):
        pass

    name = "Cat"
    tier = 1
    base_attack = 2
    base_health = 1
