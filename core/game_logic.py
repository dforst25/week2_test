from core.deck import VALUE_OF_RANK
from core.player_io import *


def calc_as_value(calc_sum: int, as_count: int) -> int:
    if as_count == 0 or calc_sum + as_count + 10 > 21:
        return 0
    else:
        return 10

def calculate_hand_value(hand: list[dict]) -> int:
    as_count = len(list(filter(lambda x: x["rank"] == "A", hand)))
    print(hand)
    calc_sum = sum(map(lambda x: VALUE_OF_RANK[x["rank"]], hand))
    if calc_sum >= 21:
        return calc_sum
    else:
        return calc_sum + calc_as_value(calc_sum-as_count, as_count)



def card_draw(deck: list[dict], player: dict) -> bool:
    if len(deck) == 0:
        raise Exception("you can't draw the card The deck is empty!!!")
    player['hand'].append(deck.pop())


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    card_draw(deck, player)
    card_draw(deck, player)
    card_draw(deck, dealer)
    card_draw(deck, dealer)
    print(f"The player's value hand is {calculate_hand_value(player['hand'])}")
    print(f"The dealer's value hand is {calculate_hand_value(dealer['hand'])}")


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer['hand']) < 17:
        card_draw(deck, dealer)
    if calculate_hand_value(dealer['hand']) > 21:
        print("The dealer got more then 21.")
        return False
    else:
        return True


def print_winner(player: dict, dealer: dict) -> None:
    points_player = calculate_hand_value(player['hand'])
    points_dealer = calculate_hand_value(dealer['hand'])
    if points_player > points_dealer:
        print("You won!!!")
    elif points_player < points_dealer:
        print("You lost!!!")
    else:
        print("Draw")


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    while ask_player_action() == 'H':
        card_draw(deck, player)
        if calculate_hand_value(player['hand']) > 21:
            print("Game Over!!!\nYou got more then 21.")
            break
        print(f"you have in your hand {calculate_hand_value(player['hand'])} points!!!")
    else:
        if dealer_play(deck, dealer):
            print_winner(player, dealer)
        else:
            print("You won!!!")
    print(f"{'='*50}\nyour points in your hand is: {calculate_hand_value(player['hand'])}\n"
          f"the dealer's points in his hand is: {calculate_hand_value(dealer['hand'])}\n{'='*50}")