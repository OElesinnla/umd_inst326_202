from game.players import HumanPlayer, ComputerPlayer
from game.cards import Card


def test_validate_input():
    player1 = HumanPlayer("P", set([Card(2), Card(1)]))
    assert player1.validate_input("Ace") == Card(1)
    assert player1.validate_input("2") == Card(2)


def test_player_repr_str():
    hp1 = HumanPlayer(name="Dondon", hand={Card(number=1), Card(number=2)})
    hp2 = HumanPlayer("Dondon2", set())
    comp = ComputerPlayer("Compy", {Card(11), Card(12)})

    # print(repr(hp1))
    # print(hp1)
    # print(repr(hp2))
    # print(hp2)
    # print(comp)

    assert repr(hp1) == \
        "HumanPlayer(name=\"Dondon\", hand={Card(number=1), Card(number=2)})"
    assert repr(hp2) == \
        "HumanPlayer(name=\"Dondon2\", hand=set())"
    assert repr(comp) == \
        "ComputerPlayer(name=\"Compy\", " \
            "hand={Card(number=11), Card(number=12)})"
     
    assert str(hp1) == "HumanPlayer \"Dondon\" has ace, 2"
    assert str(comp) == "ComputerPlayer \"Compy\" has jack, queen"