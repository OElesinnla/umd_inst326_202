# CLI Game: Bastion's Breach
By Team 202 INST 326: 
Dayonte Mcintosh, Oluwanifemi Elesinnla, Diego Fonseca, Marshal Carr

# Overview
Our recreation of Bastion's Breach in Python features the game's full mechanics,
a command-line interface, and a complete gameplay loop.


# An explanation of the purpose of each file in your repository.
cards.py             | Creation of Card class and assigning values to cards
computerlogic.py     | Designs how the computer player operates
deck.py              | Designs the distrubtion of the cards to the player
                        and the middle deck
gameplay.py          | Takes care of each round of the game, the scoring
                         logic and the display of the game to the terminal
players.py           | Takes care of the display of players' choices 
main.py              | Takes care of the entire logic of the game and how the
                         game actually runs from beginning to end
test_players.py      | Test file for the validate input method and magic methods
test_screens.py      | Test file for the display screens 


# Clear instructions on how to run your program from the command line. 
1. python main.py 

# Clear instructions on how to use your program and/or interpret the output of 
 the program. 
 1. Select game mode (1-Begin game with you & a computer player
                      2-Begin game with two players taking turns
                      q- Quit)
2. Enter your name 
3. The middle card is displayed and your cards are also displayed 
4. When you see this >> << around a card in the middle deck it means that
    is the current card you have to beat
3. Type in the value of whatever card you want to play
4. The computer player's card is displayed
5. Then your current score and the computer player's current score
6. Your can only enter a card that is currently in your deck
7. If no one wins a round the score is accumulated for the next round
8. After 13 rounds the winner is displayed  


# An annotated bibliography of all sources you used to develop your project


# Functions written, skills demonstrated
What function each group member wrote, and the skill they claim.
| Function/ Method     | Primary author         |  Techniques demonstrated                  
| ------------         | ---------------------- | -----------------------------
|                      | M. Carr                |
|                      | M. Carr                |
| validate_input       | O. Elesinnla           | Conditional Expressions 
| turn method          | O. Elesinnla           | Composition of two custom 
                                                    classes
|                      | D. Fonseca             |
|                      | D. Fonseca             |
| shuffle_and_deal()   | D. Mcintosh            | List comprehensions
|                      | D. Mcintosh            |

