from typing import Optional

from objects.cards.units.units import Unit
from objects.hand import Hand


class Combat:
    hand1: Hand
    hand2: Hand
    is_finished: bool
    winner: Optional[Hand]
    print_result: bool

    def __init__(self, hand1: Hand, hand2: Hand, print_result=False):
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
            winner = self.get_winner()
            result_str = "DRAW!" if winner is None else winner.name
            print('COMBAT OVER - RESULT IS: ' + result_str)

    def perform_turn(self) -> None:
        card1, card2 = self.get_first_cards()
        card1.take_damage(card2.combat_attack)
        card2.take_damage(card1.combat_attack)
        if self.print_result:
            print(f'{self.hand1.name}: Card 1 - {card1} takes {card2.combat_attack} damage')
            print(f'{self.hand2.name}: Card 2 - {card2} takes {card1.combat_attack} damage')
            if card1.alive is False:
                print(f'FATALITY for {self.hand1.name}: {card1.name}')
            if card2.alive is False:
                print(f'FATALITY for {self.hand2.name}: {card2.name}')

    def get_first_cards(self) -> tuple[Unit]:
        return self.hand1.get_first_card(), self.hand2.get_first_card()

    def set_winner(self) -> None:
        if self.hand1.is_defeated() and self.hand2.is_defeated():
            self.winner = None
        else:
            self.winner = self.hand1 if self.hand2.is_defeated() else self.hand2
