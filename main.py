import sys

from game.cards import Card
from game.deck import full_deck, deal_three_suits
from game.players import Player, HumanPlayer, ComputerPlayer
from game.gameplay import Round, GameState

import graphics.view as view


def main():
    # Main screen
    #   Mode select
    #   Quit game if q is selected
    mode_input = ''
    while not mode_input in ['1', '2', '3', 'q']:
        view.main_screen()
        mode_input = input().strip()
    if mode_input.lower() == 'q':
        sys.exit()

    # Player creation
    #   Initialize hands and middle cards
    #   Name player if mode 1
    #   Let both players choose a name if mode 2
    deck = full_deck()
    p1hand, p2hand, middle = deal_three_suits(deck)
    p1 = None
    p2 = None
    if mode_input == '1':                           # 1 player mode
        player_name_input = ''
        while not player_name_input:
            view.player_init_1()
            player_name_input = input().strip()
        p1 = HumanPlayer(player_name_input, p1hand)
        p2 = ComputerPlayer("Sebastian", p2hand)
    if mode_input == '2':                           # 2 player mode
        player_name_input = ''
        while not player_name_input:
            view.player_init_2(1)
            player_name_input = input().strip()
        p1 = HumanPlayer(player_name_input, p1hand)
        player_name_input = ''
        while not player_name_input:
            view.player_init_2(2)
            player_name_input = input().strip()
        p2 = HumanPlayer(player_name_input, p2hand)
    if mode_input == '3':                           # Secret 3rd mode!
        p1 = ComputerPlayer("Sebastian1", p1hand)
        p2 = ComputerPlayer("Sebastian2", p2hand)

    # Begin game
    winner: Player              = None
    players: list[Player]       = [p1, p2]
    p_scores: dict[Player, int] = {p1: 0, p2: 0}
    middle_score: int           = 1
    middle_revealed             = []
    view.begin_game_screen(p1.name, p2.name)
    while middle:
        choices: dict[Player, Card] = {p1: None, p2: None}
        # player 1 turn
        if isinstance(p1, HumanPlayer):
            while not choices[p1]:
                view.player_turn_screen(p1.name, p1.hand, len(middle), middle_revealed)
                choices[p1] = p1.turn()
        else:
            choices[p1] = p1.turn(p2.hand, middle)
        # player 2/computer turn
        if isinstance(p2, HumanPlayer):
            while not choices[p2]:
                view.player_turn_screen(p2.name, p2.hand, len(middle), middle_revealed)
                choices[p2] = p2.turn()
        else:
            choices[p2] = p2.turn(p1.hand, middle)
        middle_card = middle.pop(0) # regarding the first index as the leftmost
        middle_revealed.append(middle_card)
        view.reveal_middle_screen(p1.name, p2.name, choices[p1], choices[p2], len(middle), middle_revealed)
        if middle_card > choices[p1] and middle_card > choices[p2]:
            middle_score += 1
            view.middle_won_screen(middle_score, len(middle), middle_revealed)
        else:
            if choices[p1] == choices[p2]:
                view.turn_tie_screen()
            else:
                turn_winner = p1 if choices[p1] > choices[p2] else p2
                p_scores[turn_winner] += \
                    middle_score
                middle_score = 1
                view.turn_won_screen(p1.name, p2.name, p_scores[p1], p_scores[p2], turn_winner.name, len(middle), middle_revealed)
    if p_scores[p1] == p_scores[p2]:
        winner = "Everybody"
        view.winner_screen(p1.name, p2.name, p_scores[p1], p_scores[p2], winner)
    else:
        winner = p1 if p_scores[p1] > p_scores[p2] else p2
        view.winner_screen(p1.name, p2.name, p_scores[p1], p_scores[p2], winner.name)

    print("GAME END")


if __name__ == '__main__':
    main()