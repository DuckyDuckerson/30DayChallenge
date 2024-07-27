from .location import Location
from support.tools import display_menu

class PokemonCenter(Location):
    def __init__(self, game, name, description, items):
        super().__init__(game, name, "Pokemon Center", description)
        self.menu_options.extend(["Shop", "Heal", "Manage Storage"])
        if self.game.player:
            if self.game.player.bike:
                self.menu_options.append("Fast Travel")
        self.items = items
        self.buying = False
        self.selling = False
    #TODO - fix bugs in the buy and sell functions
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
                    self.save_game()
                case 4:
                    self.shop()
                case 5:
                    self.heal()
                case 6:
                    self.storage()
        else:
            if self.game.player.bike:
                self.fast_travel()

    def shop(self):
        options = ["Buy", "Sell"]
        display_menu(options, "Welcome To Pokemart!", back_option=True)
        choice = int(input("How can I help you? ")) - 1
        if choice == 0:
            available_items = []
            for item in self.items:
                available_items.append(f"{item.name} - {item.price}")
            display_menu(available_items, "Here's what we have for sale")
            purchase = int(input(f"You have ${self.game.player.pokedollar}. What would you like to buy? ")) - 1
            amount = int(input("How many are you purchasing?"))
            self.buy(self.items[purchase], amount)
        elif choice == 1:
            available_items = []
            for item in self.game.player.inventory.on_hand:
                #### FIX LINE BELOW ####
                available_items.append(f"{item['amount']} {item['item']} - ${item.price / 2}")
            display_menu(available_items, "Here's what is in your inventory")
            purchase = int(input("What would you like to sell? ")) - 1
            self.sell(self.items[purchase])
        else:
            return

    def heal(self):
        pass

    def storage(self):
        pass

    def fast_travel(self):
        options = self.game.player.visited_locations
        menu_options = []
        for option in options:
            menu_options.append(option.name)
        display_menu(menu_options, "Fast Travel Locations", back_option=True)
        choice = int(input("Where would you like to go? ")) - 1
        self.travel_to(options[choice])

    #TODO handle when player doesnt have enough money
    #TODO handle when inventory on_hand is full (option to buy anyway and send to storage?)
    def buy(self, item, amount):
        total_cost = item.price * amount
        if self.game.player.inventory.on_hand.get(item.name):
            self.game.player.inventory.on_hand[item.name]['amount'] += amount
        else:
            self.game.player.inventory.on_hand[item.name] = {'item': item,
                                                     'amount': amount}
        self.game.player.pokedollar -= total_cost
        print(f"You have {self.game.player.pokedollar}")
        print(f"You have the following in your inventory:")
        for key, value in self.game.player.inventory.on_hand.items():
            print(f"{key}: {value}")
            
        self.shop()

    def sell(self, item):
        self.game.player.inventory.on_hand[item.name]['amount'] -= 1
        self.game.player.pokedollar += item.price / 2
        print(f"You have {self.game.player.pokedollar}")
        print(f"Your inventory contains the following: {self.game.player.inventory.on_hand}")
        self.shop()