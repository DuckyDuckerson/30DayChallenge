from .location import Location
from support.tools import display_menu

class PokemonCenter(Location):
    def __init__(self, game, name, description, items):
        super().__init__(game, name, "Pokemon Center", description)
        self.menu_options.extend(["Shop", "Heal", "Manage Storage"])
        if self.game.player.bike:
            self.menu_options.append("Fast Travel")
        self.items = items

    def main_menu(self):
        display_menu(self.menu_options)
        action = int(input("What would you like to do?")) - 1
        if action < 6:
            match action:
                case 0:
                    self.travel()
                case 1:
                    self.view_description()
                case 2:
                    self.view_npcs()
                case 3:
                    self.shop()
                case 4:
                    self.heal()
                case 5:
                    self.storage()
        else:
            if self.game.player.bike:
                self.fast_travel()

    def shop(self):
        pass

    def heal(self):
        pass

    def storage(self):
        pass

    def fast_travel(self):
        options = self.game.player.visited_locations

    def buy(self):
        pass

    def sell(self):
        pass