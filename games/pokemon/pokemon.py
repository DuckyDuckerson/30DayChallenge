import random
from support.tools import display_menu
from support.tools import print_message as pm
from .data import starter_pokemon as starters
from .data import Pokemon
from .pokebattle import Battle
from .entities.player import Player
from .world.kanto import Kanto



class PokemonGame:
    def __init__(self):
        self.name = "Pokemon"
        self.playing = False
        self.game_started = False
        self.player = None
        self.region = Kanto(self)


    # I think we should do instead of this main_game menu here, a "main_menu" method on each of the locations, that lists the available options for that location
    #then in game_loop we'll call self.player.current_location.main_menu()
    #that way we can have different options depending on where you are and we can kinda separate the code out a little bit.
    #so i'm gonna do the pokemon center class with that structure in mind, and then if/when i finish that I'll work on restructuring this file if that sounds cool with yall
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

        player_pokemon = self.player.team[0] #can ignore this warning, it just doesn't like that I init player as None cuz None has no team
        # but by the time this function is called, a player will have been created

        self.battle(enemy, player_pokemon)

    def battle(self, enemy, player_pokemon):
        battle = Battle(enemy, player_pokemon)
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
            self.create_character()            
        elif choice == 1:
            self.load_game()
        else:
            self.playing = False

    def load_game(self):
        pass
        #write code to read data from json file and list games by "player name, location, and date and time of last save"
        # use saved data to create self.player as an instance of the Player class with the loaded info
        # set self.game_started = True

    def create_character(self):
        player_name = input("Enter Your Player Name: ")
        self.player = Player(player_name)
        self.player.location = self.region.starting_location
        self.game_started = True
        self.select_pokemon()

    def select_pokemon(self):
        pm(f"Welcome {self.player.name}! Which pokemon would you like to select?", 2, 1)
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
        self.player.team.append(starting_pokemon) #same warning as above
        pm(f"Welcome to {self.player.location.name}!", 2, 1)

    def game_loop(self):
        if not self.game_started:
            self.start_menu()
        else:
            #self.main_game()
            self.player.location.main_menu() #can ignore these warnings. its yelling cuz the location is set to none initially, but by the time this code is ran, it will have been set