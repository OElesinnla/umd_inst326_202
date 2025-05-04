from dataclasses import dataclass, field

@dataclass
class Card:
    """A card in the 52-card deck.
    In Bastion Breach, the suit is irrelevant to a card's value.

    Attributes:
        number (int): The Card's numeric value, from Ace to King, 
            beginning at 0.
        alias (str): The name of the card's value.
        suit (str): The suit of the card, as a utf-8 character.
    """
    number: int
    alias: str = field(init=False)
    suit: str = ''

    def __post_init__(self):
        match self.number:
            case 1:
                self.alias = 'ace'
            case 11:
                self.alias = 'jack'
            case 12:
                self.alias = 'queen'
            case 13:
                self.alias = 'king'
            case _:
                self.alias = str(self.number)

    def __eq__(self, other: 'Card'):
        return self.number == other.number
    def __lt__(self, other: 'Card'):
        return other.number < 11 if self.number == 1 \
            else self.number < other.number
    def __gt__(self, other: 'Card'):
        return other.number >= 10 if self.number == 1 \
            else self.number > other.number
    
    def __add__(self, other: 'Card'):
        return Card(self.number + other.number)
    
    def __hash__(self):
        return self.number
    
    def __repr__(self):
        return f"Card(number={self.number})" \
            if not self.suit \
            else f"Card(number={self.number}, suit={self.suit})"
    
    def __str__(self):
        return f"{self.alias}" \
            if not self.suit \
            else f"{self.alias} of {self.suit}"
    
def to_card_value(alias: str) -> Card:
    """Convert a card alias to a Card with its respective value.
    
    Args:
        alias (str): semantic card name. th resultant Card will have an alias
            which is this.
    Returns:
        Card: has the same alias as the arg alias, provided it is valid.
    """
    alias = alias.lower()
    match alias:
        case 'ace':
            return Card(1)
        case 'jack':
            return Card(11)
        case 'queen':
            return Card(12)
        case 'king':
            return Card(13)
        case _:
            return Card(int(alias))
        
