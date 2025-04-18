import model, view

def game_turns(p1hand: list, p2hand: list, middle: list) -> str:
    ...
    # while True OR while middle
    # p_in = input()
    # if move_algorithm.validate_input(p_in, p1hand)
    # determine_winner()
    turn = 1
    p1score, p2score, middlescore = 0, 0, 0
    middle_pile = []
    while middle:
        print(f"Player 1: {p1hand}")
        print(f"Player 2: {p2hand}")
        
        if turn == 1:
            player_name, player_hand = "Player 1", p1hand
        else:
              player_name, player_hand = "Player 2", p2hand
        move = input(f"[player_name], play a card: ")
        
        if validate_input(move, player_hand):
            player_hand.remove(move)
            middle_pile.append(move)
            print(f"{player_name} plays {move}")
            
            if len(middle_pile) == 2:
                player1 = middle_pile[0]
                player2 = middle_pile[1]

                if middle.pop() > player1 and player2:
                    middlescore += 1
                if player1 > player2:
                    p1score += 1 + middlescore
                if player2 > player1:
                    p2score += 1 + middlescore
                
                middle_pile = []
                
            turn == 2 if turn == 1 else 1
            
        
        result = determine_winner(p1hand,p2hand,middle)
        return(f"The winner is {result}")
            
            
      
def main():
    p1 = model.pick_cards()
    p2 = model.pick_cards()
    middle = model.pick_cards()
    middle = middle.shuffle()

    winner = game_turns(p1, p2, middle)

if __name__ == '__main__':
    main()