import random
import math
from games.pokemon.mechanics.moves import ALL_MOVES

class Pokemon:
    def __init__(self, initial_level, name, types, evols, male_percent, catch_rate, xp_data, base_stats, legendary, default, moves, locations, nickname=None):
        self.name = name
        self.types = types
        self.gender = self.calculate_gender(male_percent)
        self.evols = evols
        self.legendary = legendary
        self.default = default
        self.locations = locations
        self.catch_rate = catch_rate
        self.moves = moves
        self.metrics = PokeMetrics(int(initial_level), base_stats, xp_data)
        self.nickname = nickname
        self.create_moves()
        self.moveset = moves["starter_moves"]
        #battle multiplier stats that will reset to 0 after each battle
        self.battle_mult = {
            'hp': 0,
            'atk': 0,
            'def': 0,
            'spec': 0,
            'spd': 0,
            'acc': 0,
            'evas': 0
        }

    # For wild pokemon at later levels, generate a random moveset from their available moves
    def generate_moveset(self):
        possible_moves = []
        for move, details in self.moves["all_moves"].items():
            if details["learn_method"] == "level-up" and details["level_learned"] <= self.metrics.level:
                possible_moves.append(move)
        for i in range(4):
            self.moveset.append(random.choice(possible_moves))

    # calculate the gender based on the percentage chance
    def calculate_gender(self, male_percent):
        if random.uniform(0, 100) <= male_percent:
            return 'm'
        else:
            return 'f'

    def evolve(self, item=None):
        #self.evols["evol_trigger"] is the trigger for evolution
        #self.evols["evol_req"] is the requirement for evolution
        #self.evols["evolves_to"] is the pokemon it evolves to
        #evee nidoran-f and nidoran-m have evolve funcs that overwrite this
        pass

    #calls a funtion in the PokemonMetrics class to update the stats after leveling
    #see below
    def level_up(self):
        self.metrics.level += 1
        self.metrics.calculate_stats()


    def create_moves(self):
        move_classes = {
            "all_moves": {},
            "starter_moves": []
        }
        for move, details in self.moves["all_moves"].items():
            move_classes["all_moves"][move] = {
                "move": ALL_MOVES[move],
                "learn_method": self.moves["all_moves"][move]["learn_method"],
                "level_learned": self.moves["all_moves"][move]["level_learned"]
            }
        for move in self.moves["starter_moves"]:
            move_classes["starter_moves"].append(ALL_MOVES[move])

        self.moves = move_classes


class PokeMetrics:
    #added base stats from pokemon data, and dmg_taken info (both dictionaries)
    #updated xp to be a dict containing current_xp, base_xp, and an xp_level dict
    #the base_xp is used to calculate how much xp a pokemon gives when defeated
    #the xp_level dict contains the xp req to reach each level
    def __init__(self, level, base_stats, xp_data):
        self.level = level
        self.xp_data = xp_data

        #in pokemon gen1, a formula was used to calculate the stats based on
        #the base stats, the ivs and evs, and the level
        #i was thinking we could use the base stats from the pokemon data
        # and then update the the stat randomizer to add a modifier to them for some variation
        self.base_stats = self.stat_randomizer()
        self.ev = {stat: 0 for stat in base_stats} # always starts at 0
        self.iv = self.generate_iv() #see function below
        #then we set the stats equal to the self.base_stats (which will be modified by stat_randomizer)
        #and update them upon leveling up
        self.stats = self.base_stats


    #IVs in gen 1 were a random # between 0 and 31
    #this function calculates an iv for each stat, but adds a level_influence
    #so for higher level pokemon the ivs will be higher
    def generate_iv(self):
        level_influence = min(self.level // 10, 5)
        iv_stats = {
            'hp': min(random.randint(0, 31) + level_influence, 31),
            'atk': min(random.randint(0, 31) + level_influence, 31),
            'def': min(random.randint(0, 31) + level_influence, 31),
            'spec': min(random.randint(0, 31) + level_influence, 31),
            'spd': min(random.randint(0, 31) + level_influence, 31)}
        return iv_stats

    #used the formula for exp gained
    #for wild pokemon battles, the opponent is the wild pokemon
    #for trainer battles, the opponent is the trainer
    def regular_battle_xp(self, opponent, trainer_battle=False):
        if trainer_battle == False:
            self.xp_data["current_xp"] += (opponent.metrics.xp_data['base_xp]'] * opponent.metrics.level) / 7 * (1 / 8)
        else:
            for pokemon in opponent.team:
                self.xp_data["current_xp"] += (pokemon.metrics.xp_data['base_xp]'] * pokemon.metrics.level) / 7 * (1 / 8) * 1.5

    #when leveling, uses the IVs, EVs and level with the base stat
    #to calculate the current stat
    def calculate_stat(self, stat):
        base = self.base_stats[stat]
        iv = self.iv[stat]
        ev = self.ev[stat]
        level = self.level
        if stat == 'hp':
            return (((2 * (base + iv) + (math.sqrt(ev) / 4)) * level) / 100) + level + 10
        else:
            return (((2 * (base + iv) + (math.sqrt(ev) / 4)) * level) / 100) + 5

    #uses the above function to update all the self.stats values
    #the self.base_stats dont change
    def calculate_stats(self):
        self.stats = {
            'hp': self.calculate_stat('hp'),
            'atk': self.calculate_stat('atk'),
            'def': self.calculate_stat('def'),
            'spec': self.calculate_stat('spec'),
            'spd': self.calculate_stat('spd')
        }


    #didnt remove any of the original code. went down a rabbit hole
    #of the original formulas lol so I updated the classes to reflect that
    #but its kinda big, structrual changes so wanted to check
    #with yall before I went further
    def rand_stat_num(self):
        stat_rand = random.randint(self.level * 2, self.level * 4)
        return stat_rand

    def stat_randomizer(self):

        stats = {
            'hp': self.rand_stat_num(),
            'atk': self.rand_stat_num(),
            'def': self.rand_stat_num(),
            'spec': self.rand_stat_num(),
            'spd': self.rand_stat_num()
        }
        return stats