import os
import time

class ScreenElement:
    """A text sprite to display on the Screen.
    """
    def __init__(self, sprite: str, vpos: int, hpos: int, layer: int = 0):
        self.sprite = sprite
        self.vpos = vpos
        self.hpos = hpos
        lines = sprite.split("\n")
        self.width = len(lines[0])
        self.height = len(lines)
        self.layer = layer

    def __call__(self, *args, **kwds):
        ...

    def __le__(self, other: 'ScreenElement'):
        """Determine if self or other is higher-priority in the draw order.
        """
        return self.layer <= other.layer

class Screen:
    """A screen which displays graphical elements. User input will always
    terminate on the bottom-rightmost line. 
    """
    def __init__(self):
        self.elements = []
        self.vertical_resolution = 40
        self.horizontal_resolution = 80

    def render(self):
        os.system('cls')
        screen = ''
        for vp in range(self.vertical_resolution):
            for hp in range(self.horizontal_resolution):
                for e in self.elements:
                    if (vp - e.vpos >= 0 and e.height + e.vpos <= vp) \
                            and \
                            (hp - e.hpos > 0 and e.width + e.hpos <= hp):
                        char = e(vp - e.vpos, hp - e.hpos)
                screen += char
            screen += "\n"
        print(screen) # TODO: account for whitespace buffer

    def append(self, element: ScreenElement) -> None:
        self.elements.append(element)
        self.elements.sort()


def pclear():
    os.system('cls')
    # DEBUG: 80col ruler
    print('0123456789' * 8)

def main_screen() -> None:
    """Displays the main menu screen for the game.
    """
    pclear()
    print("""
================================================================================
 _______  _______  _______  _______  ___   _______  __    _  __   _______   
|  _    ||   _   ||       ||       ||   | |       ||  |  | ||  | |       |  
| |_|   ||  |_|  ||  _____||_     _||   | |   _   ||   |_| ||__| |  _____|  
|       ||       || |_____   |   |  |   | |  | |  ||       |     | |_____   
|  _   | |       ||_____  |  |   |  |   | |  |_|  ||  _    |     |_____  |  
| |_|   ||   _   | _____| |  |   |  |   | |       || | |   |      _____| |  
|_______||__| |__||_______|  |___|  |___| |_______||_|  |__|     |_______|  
 _______  ______    _______  _______  _______  __   __                      
|  _    ||    _ |  |       ||   _   ||       ||  | |  |                     
| |_|   ||   | ||  |    ___||  |_|  ||       ||  |_|  |                     
|       ||   |_||_ |   |___ |       ||       ||       |                     
|  _   | |    __  ||    ___||       ||      _||       |                     
| |_|   ||   |  | ||   |___ |   _   ||     |_ |   _   |                     
|_______||___|  |_||_______||__| |__||_______||__| |__|
                  
================================================================================
BASTION'S BREACH
          
    1 - Begin game with you & a computer player
    2 - Begin game with two players taking turns
    q - Quit
          
    Select game mode:
""".strip() + ' ', flush=True, end='')

def player_init_1() -> None:
    """Sets up the player by prompting the user for their name.
    The opponent is the computer player, so only 1 player enters their name.
    """
    pclear()
    print("""
Your opponent is Sebastian! 
          
Please enter your name:
""".strip() + ' ', flush=True, end='')
    
def player_init_2(player: int) -> None:
    """Sets up the player by prompting the user for their name.
    Both players will have to enter their names.
    """
    pclear()
    print(f"""
Player {player}
          
Please enter your name:
""".strip() + ' ', flush=True, end='')
    
def begin_game_screen(p1name: str, p2name: str):
    """Says who's versus who.
    """
    pclear()
    print(f"""
====BEGIN=======================================================================
    
          {p1name} vs. {p2name}
""".strip())
    time.sleep(5.0)

def player_turn_screen(pname, hand: str, middle_hidden: int, middle_revealed: list, opp_plays = None):
    """Shows the middle's revealed & yet-to-be-revealed cards, the player's 
    hand cards, and prompts for their input.
    """
    # TODO: show opponent's plays as well
    pclear()
    middle_graphic_bar = ''
    for c in middle_revealed:
        if c == middle_revealed[-1]:
            middle_graphic_bar += f"|    {c}    |"
        else:
            middle_graphic_bar += f"| {c}"
    middle_graphic_bar += '|' * middle_hidden
    print(f"""
{middle_graphic_bar}

{pname}'s hand:
{hand}

What's your move?
Type the card's name:
""".strip() + ' ', end='')
    
def reveal_middle_screen(p1name, p2name, middle_hidden: int, middle_revealed: list):
    """Shows what the middle card was.
    """
    pclear()
    print(f"""
{p1name}

Middle was: {middle_revealed[-1]}

{p2name}
""".strip())
    time.sleep(5.0)

    
def middle_won_screen(middle_score, middle_hidden: int, middle_revealed: list):
    """Shows what the middle's accumulation score is given it won the turn.
    """
    pclear()
    print(f"""
Status

{', '.join(middle_revealed)}
{middle_hidden} turns remaining

Next score is now worth {middle_score}!
""".strip())
    time.sleep(8.0)
    
def turn_tie_screen():
    """Shows if the middle didn't win, but both players tied.
    """
    pclear()
    print("""
Shit, it was a tie!
""")
    time.sleep(8.0)
    
def turn_won_screen(p1name, p2name, p1score, p2score, middle_hidden: int, middle_revealed: list):
    """Shows which player won, and the players' scores at this stage. Also gives
    stats on what the middle is like.
    """
    pclear()
    print(f"""
====STATUS======================================================================

{', '.join(middle_revealed)}
{middle_hidden} turns remaining

{p1name if p1score > p2score else p2name} won this time!
{p1name}'s score: {p1score}
{p2name}'s score: {p2score}
""".strip())
    time.sleep(8.0)

def winner_screen(p1name, p2name, p1score, p2score, winner: str):
    """Displays the final scores & who won.
    """
    pclear()
    print(f"""
====RESULTS=====================================================================

{p1name}'s final score: {p1score}
{p2name}'s final score: {p2score}

{winner} is the winner! Congrats you lucky bastard!
""".strip())
    time.sleep(8.0)