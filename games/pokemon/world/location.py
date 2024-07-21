from os import access
from support.tools import display_menu, print_message

class Location:
    def __init__(self, game, name, location_type, description):
        self.game = game
        self.name = name
        self.location_type = location_type
        self.description = description
        self.connected_locations = []
        self.accessible = True
        self.npcs = []
        self.wild_pokemon = []
        self.menu_options = ["Travel", "Where Am I?", "Who Is That?"]
        self.events = []

    def main_menu(self):
        display_menu(self.menu_options)
        action = int(input("What would you like to do?")) - 1
        match action:
            case 0:
                self.travel()
            case 1:
                self.view_description()
            case 2:
                self.view_npcs()

    def view_description(self):
        print_message(f"You are in {self.name}.", 2, 1)
        if self.description != "":
            print_message(self.description, 2, 1)

    def travel(self):
        accessible_locations = []
        location_names = []
        for location in self.connected_locations:
            if location.accessible:
                accessible_locations.append(location)
        for location in accessible_locations:
            location_names.append(location.name)
        display_menu(location_names, "Connected Locations", back_option=True)
        action = int(input("Where would you like to go?")) - 1
        if action == len(location_names) - 1:
            return
        else:
            if accessible_locations[action].location_type == 'Pokemon Center' and accessible_locations[action].name not in self.game.player.visited_locations:
                self.game.player.visited_locations.append(accessible_locations[action].name)
            print_message(f"Welcome to {accessible_locations[action].name}", 2, 1)            
            self.travel_to(accessible_locations[action])

    def travel_to(self, location):
        self.game.player.location = location

    def view_npcs(self):
        names = []
        for npc in self.npcs:
            names.append(f"{npc.name} - {npc.description}")
        if names == []:
            print_message("There is no one here.", 2, 1)
        else:
            display_menu(names, "There Are Some People Here", back_option=True)
            action = int(input("Who would you like to talk to? ")) - 1
            if action == len(names) - 1:
                return
            else:
                self.npcs[action].chat()
            #can make the chat function more complex if we wnt. like include a response option and stuff