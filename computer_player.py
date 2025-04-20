"""A computer player, we may drop in if we like.
"""

from cards import Card
from random import choice, randint, shuffle
from statistics import fmean


# TODO: factor in accum of points
def choose_next_card(hand_cards: list[Card], 
                     opponent_cards: list[Card], 
                     middle_cards: list[Card], 
                     depth: int, accum: int = 0) -> tuple[Card, float]:
    """From Cards in hand, choose a Card which is most likely to lead to future
    profits.

    Args:
        hand_cards (list):      The Cards in the hand to choose from.
        opponent_cards (list):  The cards opponent has laid so far.
        middle_cards (list):    The cards revealed in the middle so far.
        depth (int):            How many moves to predict into the future.
    Returns:
        Card: The identity of the card to play.
    """
    opp_permutes: list[tuple[Card, Card]] = \
        [(o, m) for o in opponent_cards for m in middle_cards]
    card_probs: dict[Card, float] = dict()
    for card in hand_cards:
        successes = 0
        branch_probs: list[float] = list()
        for permute in opp_permutes:
            opp_card, middle_card = permute
            if card > opp_card and card > middle_card:
                successes += 1
            elif middle_card > card and middle_card > opp_card:
                accum += 1
            if not len(hand_cards) == 1:
                branch_probs.append(
                    choose_next_card(
                        [c for c in hand_cards if not c == card],
                        [c for c in opponent_cards if not c == opp_card],
                        [c for c in middle_cards if not c == middle_card],
                        depth - 1,
                        accum
                    )[-1]
                )
        branch_prob = fmean(branch_probs)
        immediate_prob = successes / len(opp_permutes)
        card_probs[card] = branch_prob * immediate_prob / 2
        if len(hand_cards) == 3:
            print(f"{card.alias}: {card_probs[card]}")
    good_cards = \
        [c for c, p in card_probs.items() if p >= max(card_probs.values())]
    pick = choice(good_cards)
    return (pick, card_probs[pick])

if __name__ == '__main__':
    p1 = [Card(i) for i in range(13)]
    shuffle(p1)
    p2 = [Card(i) for i in range(13)]
    shuffle(p2)
    middle = [Card(i) for i in range(13)]
    shuffle(middle)
    print(f"p1 cards: {[c.alias for c in p1]}")
    print(f"p2 cards: {[c.alias for c in p2]}")
    print(f"Middle cards: {[c.alias for c in middle]}")
    pick = choose_next_card(p1[-3:], p2[-3:], middle[-3:], 10)
    print(f">> Pick: {pick}")