from cards import Card, to_card_value


class Player:
    """A player of the game, who participates in turns and has a hand of cards.

    Attributes:
        name (str): The player's title.
        hand (set): Cards in the player's hand.
    """
    def __init__(self, name: str, hand: set[Card]):
        self.name = name
        self.hand = hand

    def turn(self) -> Card:
        raise NotImplementedError

class HumanPlayer(Player):
    """A player of the game who is using the terminal interface.
    """
    def __init__(self):
        super().__init__()

    def turn(self) -> Card:
        p_in = input() # Text prompt will be handled by the viewer
        if not validate_input(p_in, self.hand):
            return None
        ...


def validate_input(player_input: str, hand_cards: list[Card]) -> bool:
    player_input = player_input.strip()
    if player_input.isalpha() == False:
        return False
    elif not player_input in \
        ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
         'Jack', 'Queen', 'King'):
        return False
    elif to_card_value(player_input) not in hand_cards:
        return False
    else:
        return True