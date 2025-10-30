def is_valid_input(inp: str) -> bool:
    return inp in {'S', 'H'}


def ask_player_action() -> str:
    choice = ''
    while not is_valid_input(choice):
        choice = input("Enter your choice: 'H' or 'S'\nH = HIT, continue drawing\nS = STAND, stopping: ").upper()
    return choice
