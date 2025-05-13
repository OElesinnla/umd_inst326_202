# CLI Game: Bastion's Breach
By Team 202 INST 326: 
Marshal Carr, Dayonte Mcintosh, Diego Fonseca, Oluwanifemi Elesinnla

# Overview
Our recreation of Bastion's Breach in Python features the game's full mechanics,
a command-line interface, and a complete gameplay loop.


# An explanation of the purpose of each file in your repository.
All of the program files in our repository and their use.
| File               | Explanation
| ------------------ | --------------------------------------------------------
|cards.py            | Creation of Card class and assigning values to cards
|computerlogic.py    | Defines the computer player's behavior
|deck.py             | Designs the distrubtion of the cardsto the player and the middle deck
|gameplay.py         | Takes care of each round of the game the scoring logic and the game information to display.
|players.py          | Takes care of getting input of players' choices, whether they are a human player or a computer.
|main.py             | Takes care of the entire logic of the game and how the game actually runs from beginning to end
|test_players.py     | Test file for the validate input method and magic methods
|test_screens.py     | Test file for the display screens 


# Clear instructions on how to run your program from the command line. 
On Windows, type the following into your terminal:
```python main.py```

# Clear instructions on how to use your program and/or interpret its output
 1. Select game mode (`1`-Begin game with you & a computer player
                      `2`-Begin game with two players taking turns
                      `q`- Quit)
2. Enter your name 
3. The middle card is displayed and your cards are also displayed 
4. When you see this >> << around a card in the middle deck it means that
    is the current card you have to beat
3. Type in the value of whatever card you want to play
4. This repeats for the other player, or the computer player makes a move.
5. The turn's winner is displayed
6. If no one wins a round the score is accumulated for the next round
7. After 13 rounds the winner is displayed  


# An annotated bibliography of all sources you used to develop your project
HipsterDashie. (2021, May 28). 
*I typed up a player's guide for Bastion's Breach - here's the doc!*. 
[Online forum post]. Reddit. https://www.reddit.com/r/AngelsWithScalyWings/commentsnn9u91i_typed_up_a_players_guide_for_bastions_breach/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

# Functions written, skills demonstrated
What function each group member wrote, and the skill they claim.
| Function                              | Author         | Skill demonstrated
| -----------------------------------   | -------------- | ---------------------
| computerlogic.`choose_next_card`      | M. Carr        | Default, keyword arguments
| players.HumanPlayer.`turn`            | M. Carr        | Set operations (difference)
| gameplay.Round.`determine_winner`     | D. Fonseca     | Key function (max)
| gameplay.Round.`turns`                | D. Fonseca     | f-strings 
| players.HumanPlayer.`validate_input`  | O. Elesinnla   | Conditional expressions
| players.ComputerPlayer.`__str__`      | O. Elesinnla   | Magic method 
| deck.`deal_three_suits `              | D. Mcintosh    | Sequence unpacking
| deck.`full_deck`                      | D. Mcintosh    | List comprehension