from players import HumanPlayer
from cards import Card
def test_validate_input():
    player1 = HumanPlayer("P", set([Card(2), Card(1)]))
    assert player1.validate_input("Ace") == Card(1)
    assert player1.validate_input("2") == Card(2)