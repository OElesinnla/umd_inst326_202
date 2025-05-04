import random
from cards import Card

RANKS = ['ACE','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING']
SUITS = ['♠','♥','♦','♣']

def shuffle_and_deal() -> tuple[list[Card], list[Card], list[Card]]:
    """
    Builds a 52 card deck, shuffle it, and deal 13 cards to
    two players plus 13 cards as the middle row

    Returns:
        tuple of three lists of Card:
          - player1_hand: 13 cards
          - player2_hand: 13 cards
          - middle_row:   13 cards
    """
    deck: list[Card] = [Card(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)

    player1_hand = [deck.pop() for _ in range(13)]
    player2_hand = [deck.pop() for _ in range(13)]
    middle_row   = [deck.pop() for _ in range(13)]

    return player1_hand, player2_hand, middle_row

p1, p2, middle = shuffle_and_deal()
print(f"Player 1 got {len(p1)} cards, Player 2 got {len(p2)} cards, "
      f"middle row has {len(middle)} cards.")