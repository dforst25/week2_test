from core.deck import *
from core.game_logic import *

if __name__ == "__main__":
    deck = shuffle_by_suit(build_standard_deck())
    player = {"hand": []}
    dealer = {"hand": []}
    run_full_game(deck, player, dealer)
