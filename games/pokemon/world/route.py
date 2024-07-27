from support.tools import display_menu, print_message as pm
from .location import Location
import random
from games.pokemon.data import Pokemon
from games.pokemon.pokebattle import Battle

class Route(Location):
    def __init__(self, game, name, description, terrain, items):
        super().__init__(game, name, "Route", description)
        self.terrain = terrain
        self.items = items
        self.menu_options.append("Explore")

    def main_menu(self):
        display_menu(self.menu_options)
        action = int(input("What would you like to do?")) - 1

        if action < len(self.menu_options) - 1:
            match action:
                case 0:
                    self.travel()
                case 1:
                    self.view_description()
                case 2:
                    self.view_npcs()
                case 3:
                    self.save_game()
        else:
            self.explore()

    def view_description(self):
        pm(f"You are on {self.name}.", 2, 1)
        if self.description != "":
            pm(self.description, 2, 1)

    def random_encounter(self):
        for pokemon in self.wild_pokemon:
            pass
            # self.wild_pokemon is a list of dictionaries with the structure:
                # {
                 #'name': pokemon name
                 # 'range': [2, 5] for example. just a list of two items for the level range
                 # 'rate': 50 (for example. just a percentage num for the chance it appears compared to the other ones in the list)
                #}
            #can use the encounter rate to determine what pokemon appears and range to determine what level it is
            # then return that pokemon and call this function in the explore function below before the battle    

    def explore(self):
        time_passed = random.randint(2, 7)
        for i in range(time_passed):
            pm(".....", 1, 1)
        #have a chance to have an encounter, a chance nothing happens and maybe a small chance to find an item
        #if self.items != []
        pm("You encountered a wild pokemon!", 2, 1)
        enemy  = Pokemon("Charmander", ["fire"], "Medium Slow",
                         ['Charmeleon'], ['Blaze', 'Solar Power'],
                         ['Growl'], 123, 2)

        player_pokemon = self.game.player.team[0]
    
        self.battle(enemy, player_pokemon)
    
    def battle(self, enemy, player_pokemon):
        battle = Battle(enemy, player_pokemon)
        battle.battle()