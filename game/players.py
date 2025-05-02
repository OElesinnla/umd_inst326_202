from .cards import Card, to_card_value


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
        """A turn for this player in which they will chose their Card from their
        hand.
        """
        raise NotImplementedError
    
    def __hash__(self):
        """Hash from player's name and their suit.
        """
        return hash(f"{self.name}{self.hand[0].suit}")

class HumanPlayer(Player):
    """A player of the game who is using the terminal interface.

    Attributes:
        name (str): The player's title.
        hand (set): Cards in the player's hand.
    """
    def __init__(self, name: str, hand: set[Card]):
        super().__init__(name, hand)

    def turn(self) -> Card:
        p_in = input().strip() # Text prompt will be handled by the viewer
        if not (card := self.validate_input(p_in)):
            return None
        else:
            self.hand -= card
            return card

    def validate_input(self, player_input: str) -> bool:
        player_input = player_input.strip()
        if not player_input in \
            ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
            'Jack', 'Queen', 'King'):
            return None
        elif to_card_value(player_input) not in self.hand:
            return None
        else:
            return to_card_value(player_input)
        
class ComputerPlayer(Player):
    """A computer player who will make moves like a player. They will also
    submit specialized information about their internal state.
    
    Attributes:
        name (str): The computer's title.
        hand (set): Cards in the comp's hand.
    """
    def __init__(self, name, hand):
        super().__init__(name, hand)
