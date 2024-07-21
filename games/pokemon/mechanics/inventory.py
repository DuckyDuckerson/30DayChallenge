class Inventory:
    def __init__(self):
        self.on_hand = {}
        self.storage_items = {}
        self.storage_pokemon = {}

    def use_item(self, item, target=None):
        item.use(target)
        self.on_hand[item.name]['amount'] -= 1