from .location import Location
from support.tools import display_menu

class Town(Location):
    def __init__(self, game, name, description):
        super().__init__(game, name, "Town", description)
