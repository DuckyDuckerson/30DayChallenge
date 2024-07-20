import random
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
        self.game_started = False
        self.player = None


    def main_game(self):
        options = ["Explore", "Pokemon Center", "Gym", "Pokedex"]
        display_menu(options, "What would you like to do next?")
        choice = int(input("Enter your selection: ")) - 1
        if choice == 0:
            self.explore()
        elif choice == 1:
            self.center()
        elif choice == 2:
            self.gym()
        else:
            self.pokedex()

    def explore(self):
        time_passed = random.randint(2, 7)
        for i in range(time_passed):
            pm(".....", 1, 1)
        pm("You encountered a wild pokemon!", 2, 1)
        enemy  = Pokemon("Charmander", ["fire"], "Medium Slow",
                         ['Charmeleon'], ['Blaze', 'Solar Power'],
                         ['Growl'], 123, 2)
        
        self.battle(enemy)

    def battle(self, enemy):
        battle = Battle(enemy)
        battle.battle()

    
    def center(self):
        pass

    def gym(self):
        pass

    def pokedex(self):
        pass
                
        
    def start_menu(self):
        options = ["Start Game", "Load Game", "Exit",]
        menu_title = "Pokemon"
        display_menu(options, menu_title)
        choice = int(input("Enter Your Choice: ")) - 1

        if choice == 0:
            self.game_started = True
            self.select_pokemon()
            
    def select_pokemon(self):
        pm("Which pokemon would you like to select?", 2, 1)
        poke_options = [opt.get("name") for opt in starters]
        display_menu(poke_options, "Starter Pokemon")
        chosen_pokemon  = int(input("Selected Pokemon: ")) - 1

        starting_pokemon = None
        for option in starters:
            if option.get("name") == poke_options[chosen_pokemon]:
                starting_pokemon = Pokemon(option.get("name"),
                                           option.get("types"),
                                           option.get("xp_type"),
                                           option.get("evols"),
                                           option.get("abilities"),
                                           option.get("moves"),
                                           option.get("xp"),
                                           1)
        self.team.append(starting_pokemon)
    
    def game_loop(self):
        if not self.game_started:
            self.start_menu()
        else:
            self.main_game()

class Battle:
    def __init__(self, enemy):
        pass

    def battle(self):
        pass