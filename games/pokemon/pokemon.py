import random
from support.tools import display_menu
from support.tools import print_message as pm
from .data import starter_pokemon as starters
from .data import Pokemon
from .pokebattle import Battle
from .entities.player import Player
from .world.kanto import Kanto
import os
import json


class PokemonGame:
    def __init__(self):
        self.name = "Pokemon"
        self.playing = False
        self.game_started = False
        self.player = None
        self.region = Kanto(self)

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
        filename = 'games/pokemon/pokedata/poke_save_data.json'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
        options = []
        menu_options = []
        for item in data:
            option = [data[item]['id'], f"{data[item]["id"]} - {data[item]["name"]}"]
            options.append(option)
            menu_options.append(option[1])
        display_menu(menu_options, "Saved Games", back_option=True)
        chosen_game = int(input("Which game would you like to load?")) - 1
        self.player = Player.load_player_data(filename, options[chosen_game][0])
        self.game_started = True
    

    

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
            self.player.location.main_menu()