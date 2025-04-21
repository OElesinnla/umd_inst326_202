from cards import Card, to_card_value


# FULL_SUIT: set[Card] = {Card(i) for i in range(13)}

    
def validate_input(player_input: str, hand_cards: list[Card]):
    player_input = player_input.strip()
    if player_input.isalpha() == False:
        raise ValueError("Invalid input")
    elif not player_input in \
        ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
         'Jack', 'Queen', 'King'):
        raise ValueError("Not a possible card")
    elif to_card_value(player_input) not in hand_cards:
        raise ValueError("Not in your deck")
    else:
        return player_input