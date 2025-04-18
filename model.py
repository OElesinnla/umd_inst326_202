from cards import Card


FULL_SUIT: set[Card] = {Card(i) for i in range(13)}


def choose_next_card(hand_cards: list[Card], 
                     opponent_cards: list[Card], 
                     middle_cards: list[Card], depth: int) -> Card:
    """From Cards in hand, choose a Card which is most likely to lead to future
    profits.

    Args:
        hand_cards (list):      The Cards in the hand to choose from.
        opponent_cards (list):  The cards opponent has laid so far.
        middle_cards (list):    The cards revealed in the middle so far.
        depth (int):            How many moves to predict into the future.
    Returns:
        Card: The identity of the card to play.
    """
    # 1- get all the possible cards we could play, iterate thru them
    # 2- for each card we could play, what moves could opponent make, what
    #    cards could middle reveal?
    # 3- for each possible card opponent could play x each card middle could
    #    reveal, again pick a card that we could play.... i.e. recursion
    # 4- this can get extremely computationally heavy so figure out some edge
    #    cases or strategies to "trim the branches"
    # 5- return when there's only one card in hand left, or when depth is 0
    # (you could ignore depth if you felt like it)
    
def validate_input(card):
    if player_input !=:
        raise ValueError
    elif player_input not in hand_cards:
        raise ValueError
    else:
        return player_input 
   
     
    # if player_input is a integer/ letter
    # if player_input is in player's deck 
    
        