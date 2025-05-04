import os


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
    pclear()
    print("""
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

BASTION'S BREACH
          
    1 - Begin game with you & a computer player
    2 - Begin game with two players taking turns
    q - Quit
          
    Select game mode:
""".strip() + ' ', flush=True, end='')

def player_init_1() -> None:
    pclear()
    print("""
Your opponent is Sebastian! 
          
Please enter your name:
""".strip() + ' ', flush=True, end='')
    
def player_init_2(player: int) -> None:
    pclear()
    print(f"""
Player {player}
          
Please enter your name:
""".strip() + ' ', flush=True, end='')