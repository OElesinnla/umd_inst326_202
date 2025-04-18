import model, view

def game_turns(p1hand: list, p2hand: list, middle: list) -> str:
    ...
    # while True OR while middle
    # p_in = input()
    # if move_algorithm.validate_input(p_in, p1hand)
    # determine_winner()

def main():
    p1 = model.pick_cards()
    p2 = model.pick_cards()
    middle = model.pick_cards()
    middle = middle.shuffle()

    winner = game_turns(p1, p2, middle)

if __name__ == '__main__':
    main()