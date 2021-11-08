from objects.cards.unit import Unit


class Fish(Unit):
    def pre_combat_action(self):
        pass

    def pre_turn_action(self):
        pass

    name = "Fish"
    tier = 1
    base_attack = 1
    base_health = 2
