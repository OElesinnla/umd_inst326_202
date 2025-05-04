import random

from .cards import Card

# TODO
# Could this function just return a tuple of lists of cards, shuffled & of the 
# same suit? so the header would look like this
# shuffle_and_deal() -> tuple[list[Card]]
# and we could use it like this
# p1_hand, p2_hand, middle = shuffle_and_deal() 
def shuffle_and_deal(deck: list[tuple], num_cards: int = 13) -> tuple[list[tuple], list[tuple]]:
    """
    Shuffle deck and deal off num_cards.

    Args:
        deck = your deck of cards 
        num_cards = how many cards will be dealt which is 13 cards

    Returns:
        hand: the cards that the player get after the cards are dealt
        remainder: the rest of the deck after the cards are dealt 
    """
    if not isinstance(deck, list):
        raise TypeError("deck must be a list")
    if not isinstance(num_cards, int):
        raise TypeError("num_cards must be an integer")
    if num_cards < 0 or num_cards > len(deck):
        raise ValueError("num_cards must be between 0 and len(deck)")

    d = deck[:]
    random.shuffle(d)
    hand = [d.pop(0) for _ in range(num_cards)]
    remainder = d

    return hand, remainder

ranks = ['ACE','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING']
suits = ['♠','♥','♦','♣']
full_deck = [r+s for s in suits for r in ranks]

player_hand, rest_of_cards = shuffle_and_deal(full_deck, 13)
print(f"Dealt {len(player_hand)} cards, {len(rest_of_cards)} remain.")