from .npc import NPC

class Trainer(NPC):
    def __init__(self, name, speech_options, team, challenge_rating):
        super().__init__(name, [], speech_options)
        self.team = team
        self.challenge_rating = challenge_rating

    #im assuming trainers wont have items so in this class, tht inherits from NPC, when we init it we dont
    #have to pass in an items thing
    #then on line 5 where we init the parent class (thats what super does. its *nearly* the same as doing NPC.__init__ but has slight differences i can go over tn if yall want)
    #but when we init the parent class, we pass in an empty list, so the default value for items will that
    #if we passed in items to the init method of Trainer, then we could put items in teh super init method
    #but since we've omitted it, but the NPC class still requires it, we have to pass a default value there basically