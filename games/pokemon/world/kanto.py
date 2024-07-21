from .town import Town
from .route import Route
from .location import Location
from games.pokemon.pokedata.location_info import kanto_towns, WORLD_SETUP


class Kanto:
    # creating this as like a worldbuilding factory so we dont have to clog up pokemon.py
    # with worldbuilding logic
    # then we'll just add a self.region to the PokemonGame class
    def __init__(self, game):
        self.game = game
        self.name = "Kanto"
        self.locations = {} #format = "{location_name}": {instance of location_class/route_class etc}
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

        
        #this just goes through a list of all the towns and calls the create_location func
        #for stuff that doesn't have any funky things
        #(like accessible set to False) putting them in a list of lists similar to this will work
        #but for others we'll need to do em individually
        for town in kanto_towns:
            self.create_location(town[0], "Town", town[1])


        
        self.connect_locations("Pallet Town", "Route 1")

    def create_location(self, name, location_type, desc, **kwargs):
        if location_type == 'Route':
            terrain = kwargs.get('terrain')
            items = kwargs.get('items')
            loc = Route(self.game, name, desc, terrain, items)
        
        # elif location_type in ["Forest", 'Cave', "Pokemon Center", "Gym"]:
        #     #will expand on each of these once those classes are created
        
        else: #for location types where there are no additional features (like town)
            loc = Location(self.game, name, location_type, desc)

        #then regardless of the location type, we get the wild pokemon and npc data
        #from the WORLD_SETUP dict and update the location
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

