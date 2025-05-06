import random
from cards import Card
from typing import List, Tuple

def full_deck() -> List[Card]:
    """
    this will build and return the 52 card deck and 4 suits in ranking order.
    """
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10','JACK', 'QUEEN', 'KING', 'ACE']
    suits = ['♠', '♥', '♦', '♣']
    return [Card(rank, suit) for suit in suits for rank in ranks]

def deal_three_suits(
    deck: List[Card]
) -> Tuple[List[Card], List[Card], List[Card]]:
    """
    Split the card deck into three hands, eahc hand will have a suit and shuffle only the middle hand.
    
    Raises if deck isn't  52 Card instances or doesn’t have 13 of each suit.
    """
    if not isinstance(deck, list):
        raise TypeError("deck must be a list")
    if len(deck) != 52:
        raise ValueError("deck must contain exactly 52 cards")
    for c in deck:
        if not isinstance(c, Card):
            raise TypeError("all items in deck must be Card instances")
   
    by_suit = {}
    for c in deck:
        by_suit.setdefault(c.suit, []).append(c)
        
    if set(by_suit.keys()) != {'♠','♥','♦','♣'}:
        raise ValueError("deck must have the four standard suits")
    for suit, cards in by_suit.items():
        if len(cards) != 13:
            raise ValueError(f"suit {suit!r} does not have 13 cards")
        
    suit1, suit2, suit3 = random.sample(list(by_suit), 3)
    hand1 = by_suit[suit1]
    hand2 = by_suit[suit2]
    middle = by_suit[suit3].copy()
    random.shuffle(middle)
    return hand1, hand2, middle

if __name__ == "__main__":
    deck = full_deck()
    p1, p2, mid = deal_three_suits(deck)
   
    print(f"Player 1 hand ({len(p1)} cards, suit {p1[0].suit}): {p1}")
    print(f"Player 2 hand ({len(p2)} cards, suit {p2[0].suit}): {p2}")
    print(f"Middle row ({len(mid)} cards, suit {mid[0].suit}, shuffled): {mid}")