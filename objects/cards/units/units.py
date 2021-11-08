from objects.cards.unit import Unit


class TestUnit1(Unit):
    def pre_combat_action(self):
        pass

    def pre_turn_action(self):
        pass

    name = "Test unit 1/1"
    tier = 1
    base_attack = 1
    base_health = 1


class TestUnit2(Unit):
    def pre_turn_action(self):
        pass

    def pre_combat_action(self):
        pass

    name = "Test unit 2/2"
    tier = 2
    base_attack = 2
    base_health = 2
