import objects.cards.card as card_cls
import objects.hand as hand_cls


class Unit(card_cls.Card):
    name: str
    base_attack: int
    base_health: int
    run_attack: int
    run_health: int
    combat_attack: int
    combat_health: int

    def __init__(self, hand_position: int, hand: hand_cls.Hand):
        super().__init__(hand)
        self.hand_position = hand_position
        self.run_attack = self.base_attack
        self.run_health = self.base_health

    def is_alive(self):
        return self.combat_health > 0

    def set_combat_stats(self):
        self.combat_health = self.run_health
        self.combat_attack = self.run_attack

    def take_damage(self, damage: int):
        self.combat_health -= damage

    def buff(self, attack: int, health: int):
        self.base_attack += attack
        self.base_health += health

    def __str__(self):
        return f'[{self.hand_position}]: {self.name}({self.run_attack}/{self.run_health})'

    def __repr__(self):
        return self.__str__()
