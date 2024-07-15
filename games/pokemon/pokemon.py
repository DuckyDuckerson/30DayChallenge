import curses
from support.tools import display_menu
from support.tools import print_message as pm
from .data import starter_pokemon as starters
from .data import Pokemon

class PokemonGame:
    def __init__(self):
        self.name = "Pokemon"
        self.playing = False
        self.team = []
        self.inventory = []


    def start_game(self, starter):
        starting_pokemon = None
        for option in starters:
            if option.get("name") == starter:
                starting_pokemon = Pokemon(option.get("name"),
                                           option.get("types"),
                                           option.get("xp_type"),
                                           option.get("evols"),
                                           option.get("abilities"),
                                           option.get("moves"),
                                           option.get("xp"),
                                           option.get("level"))
        self.team.append(starting_pokemon)

        options = ["Explore", "Pokemon Center", "Gym", "Pokedex"]
        display_menu(options, "What would you like to do next?")
        choice = input("Enter your selection: ")
        if choice == 0:
            self.explore()
        elif choice == 1:
            self.center()
        elif choice == 2:
            self.gym()
        else:
            self.pokedex()

    def explore(self):
        pass

    def center(self):
        pass

    def gym(self):
        pass

    def pokedex(self):
        pass
                
        
    def game_loop(self):
        options = ["Start Game", "Load Game", "Exit",]
        menu_title = "Pokemon"
        display_menu(options, menu_title)
        choice = int(input("Enter Your Choice: ")) - 1

        if choice == 0:
            pm("Which pokemon would you like to select?", 2, 1)
            poke_options = [opt.get("name") for opt in starters]
            display_menu(poke_options, "Starter Pokemon")
            chosen_pokemon  = int(input("Selected Pokemon: ")) - 1
            self.start_game(poke_options[chosen_pokemon])
        