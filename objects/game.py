import settings
from objects.combat import Combat
from objects.hand import RunHand, CombatHand
from objects.shop import Shop


class Game:
    """
    One run of the game. Keeps track of meta information such as health
    """
    current_round: int
    run_hand: RunHand
    wins: int
    lives: int
    coins: int
    shop: Shop
    game_over: bool

    def __init__(self):
        self.game_over = False
        self.current_round = 0
        self.run_hand = RunHand()
        self.shop = Shop()
        self.lives = settings.PLAYER_INITIAL_HEALTH
        self.coins = settings.PLAYER_INITIAL_COINS

    def new_round(self):
        if self.lives <= 0:
            self.game_over = True
        self.current_round += 1
        self.coins = settings.COINS_PER_ROUND
        self.shop.roll_shop_hand(self.current_round)

    def do_combat(self, adversary_combat_hand: CombatHand):
        combat_hand = self.run_hand.to_combat_hand()
        combat = Combat(combat_hand, adversary_combat_hand)
        combat.perform_combat()
        if combat.winner is combat_hand:
            self.wins += 1
        if combat.winner is adversary_combat_hand:
            self.lives -= 1

        self.new_round()



