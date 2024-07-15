import curses
from support.tools import display_menu
from .data import starter_pokemon as starters

class Pokemon:
    def __init__(self):
        self.name = "Pokemon"
        self.playing = False
    

    def poke_home(self, stdscr):
        curses.curs_set(0)
    
        options = ["Start Game", "Load Game", "Exit",]
        menu_title = "Pokemon"
    
        selected_option = display_menu(stdscr, options, menu_title)
    
        if selected_option == "Exit":
            self.playing = False
        elif selected_option == "Load Game":
            pass
        else:
            self.start_game(stdscr)

    def start_game(self, stdscr):
        curses.curs_set(0)
        title = "Choose A Starter Pokemon"

        options = [opt.get("name") for opt in starters]
        display_menu(stdscr, options, title)
        
    def game_loop(self):
        curses.wrapper(self.poke_home)