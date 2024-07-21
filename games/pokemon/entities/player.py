from support.tools import display_menu
from support.tools import print_message as pm
import os
import json
from games.pokemon.mechanics.pokedex import Pokedex

class Player:
    def __init__(self, name):
        self.name = name
        self.player_id = self.generate_new_id()
        self.inventory = []
        self.bike = False
        self.team = []
        self.visited_locations = []
        self.pokedollar = 100
        self.storage = []
        self.location = None
        self.badges = []
        self.pokedex = Pokedex()

    @staticmethod 
    def generate_new_id():
        if os.path.exists('poke_save_data.json'): #not sure if yall know about reading/writing to files in python
            # but this is how its done. can explain more when we meet tn
            with open('poke_save_data.json', 'r') as file: #opens the file in readonly mode, as 'file'
                save_data = json.load(file) #converts the json to a python object (in this case a list)
            return len(save_data) + 1 
        else: #or if the file doesnt exist
            with open('poke_save_data.json', 'w') as file: 
                json.dump([], file) #this will create it, and insert just an empty list into the file
        return 1

    @classmethod
    def load_player_data(cls, file, player_id):
        pass
        #load data from file
        #use it to create an instance of the player class
        #with the location, team, etc from the saved data
        #create player instance
        #return player instance