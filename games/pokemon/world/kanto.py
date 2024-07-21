from .town import Town
from .route import Route
from .location import Location
from games.pokemon.pokedata.location_info import kanto_towns, WORLD_SETUP
from .center import PokemonCenter

class Kanto:
    def __init__(self, game):
        self.game = game
        self.name = "Kanto"
        self.locations = {}
        self.starting_location = None
        self.build_kanto()

    #Anytime we create a new location, we need to make sure to add its data to the
    #WORLD_SETUP dict in data.location_info
    #and then create it within this build world function
    #and then call connect_locations for all of its connections at the end of the build world function
    def build_kanto(self):        
        self.starting_location = Location(self.game,
                                      "Pallet Town",
                                      "Town",
                                      "A small, quiet town. Home to Professor Oak's laboratory.")
        self.locations[self.starting_location.name] = self.starting_location

        self.create_location("Route 1",
                        "Route",
                        "A short, grassy path connecting Pallet Town to Viridian City.",
                        terrain="Grassy", items=[])
        
        self.create_location('Viridian City - Pokemon Center', 'Pokemon Center', "The Pokemon Center within Viridian City", items=WORLD_SETUP['Viridian City - Pokemon Center']['items'])

       
        for town in kanto_towns:
            self.create_location(town[0], "Town", town[1])


        
        self.connect_locations("Pallet Town", "Route 1")
        self.connect_locations("Viridian City", "Route 1")
        self.connect_locations("Viridian City - Pokemon Center", "Viridian City")

    def create_location(self, name, location_type, desc, **kwargs):
        if location_type == 'Route':
            terrain = kwargs.get('terrain')
            items = kwargs.get('items')
            loc = Route(self.game, name, desc, terrain, items)
        elif location_type == 'Pokemon Center':
            items = kwargs.get('items')
            loc = PokemonCenter(self.game, name, desc, items)
        # elif location_type in ["Forest", 'Cave', "Pokemon Center", "Gym"]:
        #     #will expand on each of these once those classes are created
        
        else: 
            loc = Location(self.game, name, location_type, desc)

        loc.wild_pokemon.extend(WORLD_SETUP[loc.name]['wild pokemon'])
        loc.npcs.extend(WORLD_SETUP[loc.name]['npcs'])
        #and finally, add the location to our self.locations dictionary
        self.locations[loc.name] = loc

    def connect_locations(self, location1_name, location2_name):
        #get locations from dictionary
        loc1 = self.locations[location1_name]
        loc2 = self.locations[location2_name]
        #add connections for the locations
        loc1.connected_locations.append(loc2)
        loc2.connected_locations.append(loc1)

