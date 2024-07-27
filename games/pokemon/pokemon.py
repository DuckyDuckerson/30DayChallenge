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
            for item in data.keys():
                option = [data[item]['id'],
                          f"{data[item]["name"]} - {data[item]["location"] {len(data[item]['pokedex']['seen'])}/151 Seen, {len(data[item]['pokedex']['caught'])}/151 Caught"]
                options.append(option)
                menu_options.append(option[1])
            display_menu(menu_options, "Saved Games", back_option=True)
            chosen_game = int(input("Which game would you like to load?")) - 1
            self.player = Player.load_player_data(filename, options[chosen_game][0])
            self.game_started = True
        else:
            #TODO need to update at some point
            print("No saved data found")

    def create_character(self):
        #pm("Hello there! Welcome to the world of Pokemon!", 2, 1)
        #pm("My name is Oak! People call me the Pokemon Professor.", 2, 1)
        #pm("This world is inhabited by creatures called Pokemon!", 2, 1)
        #pm("For some people, Pokemon are pets. Others use them for battles.", 2, 1)
        #pm("As for myself... I study Pokemon as a profession.", 2, 1)
        player_name = input("First, what is your name? ")
        self.player = Player(player_name)
        self.player.location = self.region.starting_location
        #pm(f"Right! So your name is {self.player.name}!", 2, 1)
        #pm("Your very own Pokemon legend is about to unfold.", 2, 1)
        #pm("A world of dreams and adventures with Pokemon awaits! Let's go!", 2, 1)
        self.game_started = True
        self.select_pokemon()

    def select_pokemon(self):
        if self.player is not None and self.player.location is not None:
            pm(f"{self.player.name}, it is time for you to choose your first Pokemon.", 2, 1)
            poke_options = [starter.name for starter in starters]
            display_menu(poke_options, "Starter Pokemon")
            chosen_pokemon  = int(input("Selected Pokemon: ")) - 1
        
            starting_pokemon = starters[chosen_pokemon]
            self.player.team.append(starting_pokemon)
            pm(f"You've chosen {starting_pokemon.name}!", 2, 1)
            pm(f"With {starting_pokemon.name} at your side, you are ready to begin your adventure! You may explore Pallet Town more, or set off to see the world.", 2, 1)
            
    
    def game_loop(self):
        if not self.game_started:
            self.start_menu()
        else:
            if self.player is not None and self.player.location is not None:
                self.player.location.main_menu()