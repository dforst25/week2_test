from random import randrange

__all__ = ["build_standard_deck", "shuffle_by_suit"]

VALUE_OF_RANK = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                 '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
# A global dictionary where the keys are the suite and the value is the division number
SUITES_LIST = {'H': 5, 'C': 3, 'D': 2, 'S': 7}


def create_card(rank: str, suite: str) -> dict:
    if rank not in VALUE_OF_RANK:
        raise Exception("Invalid rank!!!")
    if suite not in SUITES_LIST:
        raise Exception("Invalid suite!!!")
    return {"rank": rank, "suite": suite, "value": VALUE_OF_RANK[rank]}


def build_standard_deck() -> list[dict]:
    return [create_card(rank, suite) for suite in SUITES_LIST for rank in VALUE_OF_RANK]


def is_valid_rand(deck: list[dict], i: int, j: int) -> bool:
    div_num = SUITES_LIST[deck[i]["suite"]]
    return i != j and j % div_num == 0


def get_twe_rand(deck: list[dict]) -> tuple[int, int]:
    size = len(deck)
    i = randrange(size)
    while True:
        j = randrange(size)
        if is_valid_rand(deck, i, j):
            break
    return i, j


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range(5000):
        i, j = get_twe_rand(deck)
        deck[i], deck[j] = deck[j], deck[i]
    return deck


print(shuffle_by_suit(build_standard_deck()))
