import sys

from game.deck import shuffle_and_deal
from game.players import HumanPlayer, ComputerPlayer
from game.gameplay import Round, GameState

import viewer.view as view

# def game_turns(p1hand: list, p2hand: list, middle: list) -> str:
#     turn = 1
#     p1score, p2score, middlescore = 0, 0, 0
#     middle_pile = []
#     while middle:
#         print(f"Player 1: {p1hand}")
#         print(f"Player 2: {p2hand}")
        
#         if turn == 1:
#             player_name, player_hand = "Player 1", p1hand
#         else:
#               player_name, player_hand = "Player 2", p2hand
#         move = input(f"[player_name], play a card: ")
        
#         if model.validate_input(move, player_hand):
#             player_hand.remove(move)
#             middle_pile.append(move)
#             print(f"{player_name} plays {move}")
            
#             if len(middle_pile) == 2:
#                 player1 = middle_pile[0]
#                 player2 = middle_pile[1]

#                 if middle.pop() > player1 and player2:
#                     middlescore += 1
#                 if player1 > player2:
#                     p1score += 1 + middlescore
#                 if player2 > player1:
#                     p2score += 1 + middlescore
                
#                 middle_pile = []
                
#             turn == 2 if turn == 1 else 1
             
#         result = model.determine_winner(p1hand,p2hand,middle)
#     return(f"The winner is {result}")
            

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
    round = Round((p1, p2), middle)
    winner = None
    turn_winner = None
    while not winner:
        while not turn_winner:
            gamestate = Round.turn()

    ...

if __name__ == '__main__':
    main()