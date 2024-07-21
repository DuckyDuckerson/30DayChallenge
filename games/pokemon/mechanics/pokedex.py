class Pokedex:

    def __init__(self):
        self.total_pokemon = 151
        self.entries = {}
        self.seen = {}
        self.caught = {}

    def location_stats(self, location):
        pass
        #will return info specific to your current location

    #need to make other functions to return info, how many are caught/uncaught, seen/unseen, etc


class PokedexEntry:

    def __init__(self, pokemon):
        self.id = pokemon.id
        self.name = pokemon.name
        self.type = pokemon.type
        self.description = pokemon.description

    def get_info(self):
        return f"#{self.id} {self.name}\nType(s): {self.type}\nDescription: {self.description}"
