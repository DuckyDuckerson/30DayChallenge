import random


class Pokemon:
    def __init__(self, name, types, xp_type, evols, abilities, moves, xp, level):
        self.name = name
        self.types = types
        self.xp_type = xp_type
        self.evols = evols
        self.abilities = abilities
        self.moves = moves
        self.xp = xp
        self.level = level
        self.stats = self.stat_randomizer(self.level)


    def stat_randomizer(self, level):
        stat_rand = random.randint(level * 2, level * 4)
        
        stats = {
            'hp': stat_rand,
            'atk': stat_rand,
            'def': stat_rand,
            'spatk': stat_rand,
            'spdef': stat_rand,
            'spd': stat_rand
        }
        return stats


starter_pokemon = [
    {
        'name': 'Bulbasaur',
        'types': ['grass', 'poison'],
        'xp_type': 'Medium Slow',        
        'abilities': ['chlorophyll', 'overgrow'],
        'moves': ['Growl', 'Tackle'],
        'evols': ['Ivysaur'],
        'xp': 0,
    },
    {
        'name': 'Charmander',
        'types': ['fire'],
        'xp_type': 'Medium Slow',
        'abilities': ['Blaze', 'Solar Power'],
        'moves': ['Growl'],
        'evols': ['Charmeleon'],
        'xp': 0
    },
    {
        'name': 'Squirtle',
        'types': ['water'],
        'xp_type': 'Medium Slow',        
        'abilities': ['Torrent', 'Rain Dish'],
        'moves': ['Tail Whip', 'Tackle'],
        'evols': ['Wartortle'],
        'xp': 0,
    }
    ]

pokemon = []