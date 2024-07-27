from .npc import NPC

class Trainer(NPC):
    def __init__(self, name, speech_options, team, challenge_rating):
        super().__init__(name, [], speech_options)
        self.team = team
        self.challenge_rating = challenge_rating
