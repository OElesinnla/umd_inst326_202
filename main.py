import sys

from game.cards import Card
from game.deck import shuffle_and_deal
from game.players import Player, HumanPlayer, ComputerPlayer
from game.gameplay import Round, GameState

import viewer.view as view
            

def main():
    # Main screen
    #   Mode select
    #   Quit game if q is selected
    mode_input = ''
    while not mode_input in ['1', '2', 'q']:
        view.main_screen()
        mode_input = input().strip()
    if mode_input.lower() == 'q':
        sys.exit()

    # Player creation
    #   Initialize hands and middle cards
    #   Name player if mode 1
    #   Let both players choose a name if mode 2
    p1hand, p2hand, middle = shuffle_and_deal()
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

    # Begin game
    winner: Player              = None
    players: list[Player]       = [p1, p2]
    p_scores: dict[Player, int] = {p1: 0, p2: 0}
    middle_score: int           = 1
    middle_revealed             = []
    view.begin_game_screen(p1.name, p2.name)
    while middle:
        choices: dict[Player, Card] = {p1: None, p2: None}
        for p in players:
            view.player_turn_screen(p.name, p.hand, len(middle), middle_revealed)
            p_choice = p.turn(other_player.hand, middle)
            choices[p] = p_choice
        middle_card = middle.pop(0) # regarding the first index as the leftmost
        middle_revealed.append(middle_card)
        view.reveal_middle_screen(p1.name, p2.name, len(middle), middle_revealed)
        if middle_card > p_choice[p1] and middle_card > p_choice[p2]:
            middle_score += 1
            view.middle_won_screen(middle_score, len(middle), middle_revealed)
        else:
            if p_choice[p1] == p_choice[p2]:
                view.turn_tie_screen()
            else:
                p_scores[p1 if p_choice[p1] > p_choice[p2] else p2] += \
                    middle_score
                middle_score = 1
                view.turn_won_screen(p1.name, p2.name, p_scores[p1], p_scores[p2], len(middle), middle_revealed)
    if p_scores[p1] == p_scores[p2]:
        winner = "Everybody"
        view.winner_screen(p1.name, p2.name, p_scores[p1], p_scores[p2], winner)
    else:
        winner = p1 if p_scores[p1] > p_scores[p2] else p2
        view.winner_screen(p1.name, p2.name, p_scores[p1], p_scores[p2], winner.name)

    print(winner)


if __name__ == '__main__':
    main()