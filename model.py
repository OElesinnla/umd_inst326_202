from cards import Card


FULL_SUIT: set[Card] = {Card(i) for i in range(13)}

    
def validate_input(player_input, hand_cards):
    if player_input.isalpha == False:
        raise ValueError ("Invalid input")
    if not isinstance (player_input, card.alias):
        raise ValueError
    if player_input not in hand_cards:
        raise ValueError ("Not in your deck")
    else:
        return player_input 
    
    