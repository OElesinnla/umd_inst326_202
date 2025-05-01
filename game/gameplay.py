from cards import Card
from players import Player, HumanPlayer


class Round:
    """A round of Bastion's Breach, where players will take turns placing cards
    and scoring points.

    Attributes:
        players (tuple): The two players participating in the game.
        scores (dict): The scores of each player.
        middle (list): The middle cards left to reveal.
        middle_streak (int): Points to add to the next turn a player scores,
            given the middle has won however many times.
    """
    def __init__(self, players: tuple[Player], middle: list[Card]):
        self.players: tuple[Player]     = players
        self.scores: dict[Player, int]  = {(p, 0) for p in players}
        self.p_choices: dict[Player, Card]  = {(p, None) for p in players}
        self.middle: list[Card]         = middle
        self.middle_streak: int         = 0

    def turns(self) -> list[Player]:
        """Get the necessary input from both players, and determine who won this
        time.

        Returns:
            list: The players who won. More than 1 player indicates a tie. 
        """
        while self.middle:
            middle_card = self.middle.pop()
            for player in self.players:
                self.p_choices[player] = player.turn()
                if not self.p_choices[player]:
                    ...

    def winner(self) -> list[Player]:
        """Determine from our score which player is the ultimate winner.

        Returns:
            list: The players who won. More than 1 player indicates a tie.
        """
        return [p for p, s in self.scores if s == max(self.scores)]


class GameState:
    """A representation of relevant game information for displaying in the view.
    """
    def __init__(self, players, player,
                 middle_revealed, middle_hidden,
                 scores,
                 streak: int):
        self.players = players
        self.player_turn = player
        self.middle_revealed = middle_revealed
        self.middle_hidden = middle_hidden
        self.scores = scores
        self.streak = streak