class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def use(self, target=None):
        pass
        #need to figure out how to implement this
        #like based on the item name, maybe a switch statement or whatever
        #and then also figure out how to apply it to the target if there is one
        #Oh! we could do like subclasses for certain items, like HMs and TMs maybe
        #and then those have use methods that overwrite this one. idk we'll see