from .cards import Card, to_card_value
from .computerlogic import choose_next_card


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

    def turn(self, *args) -> None | Card:
        """The human player will chose a card they have. If it's valid, it will 
        be removed from their hand and given to the game's logic handler.

        Returns:
            Card: The card corresponding to the input the player chose, given 
                they had it. It will no longer be accessible to them.
                This will be None if the input wasn't valid, and must be tried
                again.
        """
        # TODO: do error checking here: enclose this in a while loop
        # p_in = input().strip() # Text prompt will be handled by the viewer
        # if not (card := self.validate_input(p_in)):
        #     return None
        # else:
        #     self.hand -= card
        #     return card

    def validate_input(self, player_input: str) -> None | Card:
        """Validates the player's input 

        Args:
            player_input (str): The user's input 

        Returns:
            None | Card: Returns a card representing the user's input if the 
            input is valid and returns None if a user's input is invalid. 
        """
        player_input = player_input.strip()
        if not player_input in \
            ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
            'Jack', 'Queen', 'King'):
            return None
        elif to_card_value(player_input) not in self.hand:
            return None
        else:
            return to_card_value(player_input)
        
    def __repr__(self):
        return f"HumanPlayer(name=\"{self.name}\", hand={self.hand})"
        
    def __str__(self):
        return f"HumanPlayer\"{self.name}\" has "  + \
            ', '.join([str(c) for c in self.hand])
        
class ComputerPlayer(Player):
    """A computer player who will make moves like a player. They will also
    submit specialized information about their internal state.
    
    Attributes:
        name (str): The computer's title.
        hand (set): Cards in the comp's hand.
    """
    def __init__(self, name: str, hand: set[Card]):
        super().__init__(name, hand)

    def turn(self, opponent_hand, middle_hidden) -> Card:
        """Chose a Card given the GameState.

        Args:
            opponent_hand (set): What Cards the opponent still has in their
                hand.
            middle_hidden (set): What Cards the middle has yet to reveal.
        Returns:
            Card: The Card chosen, now removed from the comp's hand.
        """
        computer_card = choose_next_card(self.hand_cards, opponent_hand,
                                         middle_hidden)
        self.hand_cards.remove(computer_card)
        return computer_card
    
    def __repr__(self):
        return f"ComputerPlayer(name=\"{self.name}\", hand={self.hand})"
        
    def __str__(self):
        return f"ComputerPlayer \"{self.name}\" has " + \
            ', '.join([str(c) for c in self.hand])