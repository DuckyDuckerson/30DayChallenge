from .location import Location

class PokemonCenter(Location):
    def __init__(self, game, name, description, items):
        super().__init__(game, name, "Pokemon Center", description)
        self.menu_options.extend(["Shop", "Heal", "Manage Storage", "Fast Travel"])
        self.items = items

    # need to add functions and blah blah