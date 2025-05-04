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
    while middle:
        choices: dict[Player, Card] = {p1: None, p2: None}
        for p in players:
            p_choice = p.turn(players.remove(p)[0].hand, middle)
            choices[p] = p_choice
        middle_card = middle.pop(0) # regarding the first index as the leftmost
        if middle_card > p_choice[p1] and middle_card > p_choice[p2]:
            middle_score += 1
        else:
            p_scores[p1 if p_choice[p1] > p_choice[p2] else p2] += middle_score
            middle_score = 1
    if p_scores[p1] == p_scores[p2]:
        winner = "Everybody!"
    else:
        winner = p1 if p_scores[p1] > p_scores[p2] else p2

    print(winner)


if __name__ == '__main__':
    main()