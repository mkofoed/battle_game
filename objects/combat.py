from typing import Optional

from objects.cards.units.units import Unit
from objects.hand import CombatHand


class Combat:
    hand1: CombatHand
    hand2: CombatHand
    is_finished: bool
    winner: Optional[CombatHand]
    print_result: bool

    def __init__(self, hand1: CombatHand, hand2: CombatHand, print_result=False):
        self.hand1 = hand1
        self.hand2 = hand2
        self.is_finished = False
        self.hand1.initialize_combat()
        self.hand2.initialize_combat()
        self.print_result = print_result

    def perform_combat(self):
        self.pre_combat()

        i = 0
        while not self.hand1.is_defeated() and not self.hand2.is_defeated():
            if self.print_result:
                print(f'Performing Combat Round {i}')
            i += 1
            self.perform_turn()

        self.post_combat()

    def pre_combat(self) -> None:
        if self.print_result:
            print(f'COMBAT!\n{self.hand1.name} vs. {self.hand2.name}')

    def post_combat(self):
        self.is_finished = True
        self.set_winner()

        if self.print_result:
            result_str = "DRAW!" if self.winner is None else self.winner.name
            print('COMBAT OVER - RESULT IS: ' + result_str)

    def perform_turn(self) -> None:
        card1, card2 = self.get_first_cards()
        card1.take_damage(card2.combat_attack)
        card2.take_damage(card1.combat_attack)
        if self.print_result:
            print(f'{self.hand1.name}: Card 1 - {card1} takes {card2.combat_attack} damage')
            print(f'{self.hand2.name}: Card 2 - {card2} takes {card1.combat_attack} damage')
            if card1.is_alive() is False:
                print(f'FATALITY for {self.hand1.name}: {card1.name}')
            if card2.is_alive() is False:
                print(f'FATALITY for {self.hand2.name}: {card2.name}')

    def get_first_cards(self) -> tuple[Unit, Unit]:
        return self.hand1.get_active_unit(), self.hand2.get_active_unit()

    def set_winner(self) -> None:
        if self.hand1.is_defeated() and self.hand2.is_defeated():
            self.winner = None
        else:
            self.winner = self.hand1 if self.hand2.is_defeated() else self.hand2
