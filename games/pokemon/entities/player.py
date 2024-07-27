from support.tools import display_menu
from support.tools import print_message as pm
from typing import Optional
from games.pokemon.world.location import Location
from games.pokemon.mechanics.inventory import Inventory
import os
import json
from games.pokemon.mechanics.pokedex import Pokedex

class Player:
    def __init__(self, name):
        self.name: Optional[str] = name
        self.player_id = self.generate_new_id()
        self.inventory = Inventory()
        self.bike = False
        self.team = []
        self.visited_locations = []
        self.pokedollar = 500
        self.location: Optional[Location] = None
        self.badges = []
        self.pokedex = Pokedex()

    @staticmethod 
    def generate_new_id():
        if os.path.exists('games/pokemon/pokedata/poke_save_data.json'):
            with open('games/pokemon/pokedata/poke_save_data.json', 'r') as file:
                save_data = json.load(file) 
            return len(save_data) + 1 
        else: 
            with open('games/pokemon/pokedata/poke_save_data.json', 'w') as file: 
                json.dump({}, file)
        return 1

    @classmethod
    def load_player_data(cls, file, player_id):
        pass
        #load data from file
        #use it to create an instance of the player class
        #with the location, team, etc from the saved data
        #create player instance
        #return player instance