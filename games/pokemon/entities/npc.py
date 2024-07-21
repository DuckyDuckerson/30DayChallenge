from support.tools import print_message
import random

class NPC: # base NPC in case we want to add NPCs that you can just talk to, maybe get items from, etc
    #prolly just have the trainer class inherit from this class
    #this is basically pseudo code. i mean i guess its not lol but its not like definintely what we have to use
    #just throwing shit out there so I can have an idea of structure and stuff
    # realized I needed to add a bunch of stuff in order to actually create the pokemon center so i just been working on that lol
    def __init__(self, name, items, speech_options):
        self.name = name
        self.items = items
        self.speech_options = speech_options

    def chat(self):
        message = random.choice(self.speech_options)
        print_message(message, 2, 1)