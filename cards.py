from dataclasses import dataclass, field

@dataclass
class Card:
    """A card in the 52-card deck. In Bastion Breach, the suit is irrelevant to
    value.

    Attributes:
        number (int): The Card's numeric value, from Ace to King, 
            beginning at 0.
        alias (str): The name of the card's value.
        suit (str): The suit of the card.
    """
    number: int
    alias: str = field(init=False)
    suit: str = 'generic'

    def __post_init__(self):
        match self.number:
            case 0:
                self.alias = 'Ace'
            case 10:
                self.alias = 'Jack'
            case 11:
                self.alias = 'Queen'
            case 12:
                self.alias = 'King'
            case _:
                self.alias = str(self.number + 1)

    def __eq__(self, other: 'Card'):
        return self.number == other.number
    
    def __hash__(self):
        return self.number