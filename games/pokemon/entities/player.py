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
        self.pokedollar = 100
        self.storage = []
        self.location = None
        self.badges = []
        self.pokedex = Pokedex()

    @staticmethod #this is a decorator. I don't know exactly how they work but 
    # you can use decorators on functions to like, modify the function behavior.
    #in this case, we're setting it as a static method, meaning it can be called on either
    # the class itself or an instance of the class, but it's not able to modify the class or instance directly
    #it doesnt take "self" as an argument, because it doesnt rely on an instance of the class
    #the @classmethod decorator is similar but it takes "cls" (for class) as the first argument instead of self
    # it *can* modify the class, and must be called on the class itself instead of on an instance of the class
    #gonna make a class method later on for loading the data from the json file, to create an instance of the player that has all that players saved info
    #but i gotta figure out how itll be structured first lol we're a ways away from that
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