import random
from typing import Type

from objects.cards.card import Card
from objects.cards.unit import Unit
from objects.cards.units.cat import Cat
from objects.cards.units.dog import Dog
from objects.cards.units.fish import Fish
from objects.hand import Hand, CombatHand, RunHand
from settings import HAND_SIZE


def card_is_specific_unit(hand: Hand, index: int, card: Card):
    return isinstance(hand.get_hand()[index], card)


def card_is_any_unit(hand: Hand, index: int):
    return hand.get_hand()[index] is Unit


def card_is_empty(hand: Hand, index: int):
    return hand.get_hand()[index] is None


def add_hand_of_units(name: str, unit: Type[Unit]) -> CombatHand:
    run_hand = RunHand(name)
    combat_hand = CombatHand(run_hand)
    for i in range(HAND_SIZE):
        combat_hand.add_card(unit, i)
    return combat_hand


def add_hand_of_random_units(name: str) -> CombatHand:
    run_hand = RunHand(name)
    unit_pool = [Cat, Fish, Dog]
    cards = random.choices(unit_pool, k=HAND_SIZE)
    for i, card in enumerate(cards):
        run_hand.add_card(card, i)
    return CombatHand(run_hand)
