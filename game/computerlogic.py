"""A computer player's logic which we may drop in if we like.
"""

from .cards import Card
from random import choice, shuffle


def choose_next_card(hand_cards: list[Card], 
                     opponent_cards: list[Card], 
                     middle_cards: list[Card], 
                     depth: int, accum: int = 0) -> tuple[Card, int]:
    """From Cards in hand, choose a Card which is most likely to lead to future
    profits.

    Args:
        hand_cards (list):      The cards in the hand to choose from.
        opponent_cards (list):  The cards the opponent can lay.
        middle_cards (list):    The cards the middle can still reveal.
        depth (int):            How many moves to predict into the future.
    Returns:
        Card: The identity of the card to play.
    """
    # Basic pruning conditions
    if len(hand_cards) > 10:
        hand_cards = [c for c in hand_cards if c.number not in (0, 11, 12)]
    if sum(hand_cards, Card(0)) > sum(middle_cards, Card(0)):
        return max(hand_cards), depth
    # if sum(opponent_cards, Card(0)) > sum(hand_cards, Card(0)):
    #     return min(hand_cards), depth - 1
    
    # All permutations from here
    opp_permutes: list[tuple[Card, Card]] = \
        [(o, m) for o in opponent_cards for m in middle_cards]
    card_outcomes: dict[Card, int] = dict()
    for card in hand_cards:
        score = 0
        branch_scores = [0]
        for permute in opp_permutes:
            score = 0
            branch_scores = [0]
            opp_card, middle_card = permute
            if card > opp_card and card > middle_card:
                score += 1 + accum
            # Look ahead if there is scope to do so
            if depth > 0 and not len(hand_cards) == 1:
                branch_scores.append(
                    choose_next_card(
                        [c for c in hand_cards if not c == card],
                        [c for c in opponent_cards if not c == opp_card],
                        [c for c in middle_cards if not c == middle_card],
                        depth - 1,
                        accum + 1 \
                            if middle_card > opp_card and middle_card > card \
                            else 0
                    )[-1]
                )
        # Best forseen outcome after choosing this card
        card_outcomes[card] = score + max(branch_scores)
    # List the best choices, which may have the same expected vals
    choices = \
        [(c, e) for c, e in card_outcomes.items() \
         if e == max(card_outcomes.values())]
    return choice(choices)