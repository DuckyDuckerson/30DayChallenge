import random

from games.pokemon.pokedata.all_pokemon import ALL_POKEMON


class Pokemon:

    def __init__(self, name, types, xp_type, evols, abilities, moves, xp, initial_level):
        self.name = name
        self.types = types
        self.xp_type = xp_type
        self.evols = evols
        self.abilities = abilities
        self.moves = moves
        self.xp = xp
        self.initial_level = initial_level
        self.metrics = PokeMetrics(self.xp, self.initial_level)
        # PokeMetrics is not subscriptable, so we need to access the stats attribute of the PokeMetrics object to get the stats dictionary


class PokeMetrics:

    def __init__(self, xp, level):
        self.level = level
        self.xp = xp
        self.stats = self.stat_randomizer()

    def level_up(self, xp):
        self.level += 1
        self.xp += xp

    def rand_stat_num(self):
        stat_rand = random.randint(self.level * 2, self.level * 4)
        return stat_rand

    def stat_randomizer(self):

        stats = {
            'hp': self.rand_stat_num(),
            'atk': self.rand_stat_num(),
            'def': self.rand_stat_num(),
            'spatk': self.rand_stat_num(),
            'spdef': self.rand_stat_num(),
            'spd': self.rand_stat_num()
        }
        return stats

starter_pokemon = [
    ALL_POKEMON.get("Bulbasaur")(5),
    ALL_POKEMON.get("Charmander")(5),
    ALL_POKEMON.get("Squirtle")(5)
]
# starter_pokemon = [
#     {
#         'name': 'Bulbasaur',
#         'types': ['grass', 'poison'],
#         'xp_type': 'Medium Slow',
#         'moves': ['Growl', 'Tackle'],
#         'evols': ['Ivysaur'],
#         'xp': 0,
#     },
#     {
#         'name': 'Charmander',
#         'types': ['fire'],
#         'xp_type': 'Medium Slow',
#         'moves': ['Growl'],
#         'evols': ['Charmeleon'],
#         'xp': 0
#     },
#     {
#         'name': 'Squirtle',
#         'types': ['water'],
#         'xp_type': 'Medium Slow',
#         'moves': ['Tail Whip', 'Tackle'],
#         'evols': ['Wartortle'],
#         'xp': 0,
#     }
#     ]

pokemon = []
