import os

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

def player_init_comp() -> None:
    pclear()
    print("""
Your opponent is Sebastian! 
          
Please enter your name:
""".strip() + ' ', flush=True, end='')