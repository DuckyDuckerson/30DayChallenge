class Pokemon:
    def __init__(self, name, types, stats, xp_type, evols, abilities, moves, xp):
        self.name = name
        self.types = types
        self.stats = stats
        self.xp_type = xp_type
        self.evols = evols
        self.abilities = abilities
        self.moves = moves
        self.xp = xp
        self.level = 1

starter_pokemon = [
    {
        'name': 'Bulbasaur',
        'types': ['grass', 'poison'],
        'stats': {
            'hp': 45,
            'atk': 49,
            'def': 49,
            'spatk': 65,
            'spdef': 65,
            'spd': 45
        },
        'xp_type': 'Medium Slow',        
        'abilities': ['chlorophyll', 'overgrow'],
        'moves': ['Growl', 'Tackle'],
        'evols': ['Ivysaur'],
        'xp': 0,
    },
    {
        'name': 'Charmander',
        'types': [],
        'stats': {
            'hp': 39,
            'atk': 52,
            'def': 43,
            'spatk': 60,
            'spdef': 50,
            'spd': 65,
            },
        'xp_type': 'Medium Slow',
        'abilities': ['Blaze', 'Solar Power'],
        'moves': ['Growl'],
        'evols': ['Charmeleon'],
        'xp': 0
    },
    {
        'name': 'Squirtle',
        'types': ['Water'],
        'stats': { 
            'hp': 44,
            'atk': 48,
            'def': 65,
            'spatk': 50,
            'spdef': 64,
            'spd': 45
            },
        'xp_type': 'Medium Slow',        
        'abilities': ['Torrent', 'Rain Dish'],
        'moves': ['Tail Whip', 'Tackle'],
        'evols': ['Wartortle'],
        'xp': 0,
    }
    ]

pokemon = []