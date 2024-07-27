from support.tools import print_message
import random

class NPC:
    def __init__(self, name, items, speech_options):
        self.name = name
        self.items = items
        self.speech_options = speech_options

    def chat(self):
        message = random.choice(self.speech_options)
        print_message(message, 2, 1)