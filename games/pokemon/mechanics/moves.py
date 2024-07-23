import random
from games.pokemon.pokedata.type_damage import TYPE_DATA
from games.pokemon.pokedata.multipliers import MULTIPLIERS

class Move:
    def __init__(self, name, desc, move_type, power, accuracy, pp):
        self.name = name
        self.desc = desc
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.max_pp = 61

    @property
    def is_damaging(self):
        return self.power > 0

    @property
    def is_physical(self):
        physical_types = ["NORMAL", "FIGHTING", "FLYING", "GROUND", "ROCK", "BUG", "GHOST", "POISON"]
        return self.move_type in physical_types

    @property
    def is_special(self):
        return self.is_damaging and not self.is_physical

    def use(self, actor, target):
        random_acc = random.randint(0, 255)
        hits = random_acc < self.accuracy * (MULTIPLIERS[actor.battle_mult['acc']]/MULTIPLIERS[target.battle_mult['evas']])
        if not hits:
            return "miss"
        if self.is_special:
            atk = actor.metrics.stats["spec"]
            defense = target.metrics.stats["spec"]
        else:
            atk = actor.metrics.stats["atk"]
            defense = target.metrics.stats["def"]
        crit = random.randint(0, 255) <= actor.metrics.stats["spd"]
        crit_hit = 2 if crit else 1
        stab = 1.5 if self.move_type.lower() in actor.types else 1
        t1 = TYPE_DATA[self.move_type.title()][target.types[0]]
        if len(target.types) > 1:
            t2 = TYPE_DATA[self.move_type.title()][target.types[1]]
        else:
            t2 = 1
        dmg_pretotal = ((((((2 * actor.metrics.level * crit_hit) / 5) + 2) * self.power * (atk / defense)) / 50) + 2) * stab * t1 * t2
        if dmg_pretotal == 1:
            return 1
        elif dmg_pretotal == 0:
            return "miss"
        else:
            rand_factor = random.randint(217, 255)
            return (dmg_pretotal * rand_factor) // 255
    
ALL_MOVES = {}

class Absorb(Move):
    def __init__(self, name="Absorb", desc="Restores the user's HP by 1/2 of the damage inflicted on the target.", move_type="Grass", power=20, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass
ALL_MOVES["Absorb"] = Absorb()

class Acid(Move):
    def __init__(self, name="Acid", desc="May lower opponent's Special Defense.", move_type="POISON", power=40, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Acid"] = Acid() 

class AcidArmor(Move):
    def __init__(self, name="Acid Armor", desc="Sharply raises user's Defense.", move_type="POISON", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Acid Armor"] = AcidArmor() 

class Agility(Move):
    def __init__(self, name="Agility", desc="Sharply raises user's Speed.", move_type="PSYCHIC", power=None, accuracy=None, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Agility"] = Agility() 

class Amnesia(Move):
    def __init__(self, name="Amnesia", desc="Sharply raises user's Special Defense.", move_type="PSYCHIC", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Amnesia"] = Amnesia() 

class AuroraBeam(Move):
    def __init__(self, name="Aurora Beam", desc="May lower opponent's Attack.", move_type="ICE", power=65, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Aurora Beam"] = AuroraBeam() 

class Barrage(Move):
    def __init__(self, name="Barrage", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=15, accuracy=85, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Barrage"] = Barrage() 

class Barrier(Move):
    def __init__(self, name="Barrier", desc="Sharply raises user's Defense.", move_type="PSYCHIC", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Barrier"] = Barrier() 

class Bide(Move):
    def __init__(self, name="Bide", desc="User takes damage for two turns then strikes back double.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bide"] = Bide() 

class Bind(Move):
    def __init__(self, name="Bind", desc="Traps opponent, damaging them for 4-5 turns.", move_type="NORMAL", power=15, accuracy=85, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bind"] = Bind() 

class Bite(Move):
    def __init__(self, name="Bite", desc="May cause flinching.", move_type="DARK", power=60, accuracy=100, pp=25):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bite"] = Bite() 

class Blizzard(Move):
    def __init__(self, name="Blizzard", desc="May freeze opponent.", move_type="ICE", power=110, accuracy=70, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Blizzard"] = Blizzard() 

class BodySlam(Move):
    def __init__(self, name="Body Slam", desc="May paralyze opponent.", move_type="NORMAL", power=85, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Body Slam"] = BodySlam() 

class BoneClub(Move):
    def __init__(self, name="Bone Club", desc="May cause flinching.", move_type="GROUND", power=65, accuracy=85, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bone Club"] = BoneClub() 

class Bonemerang(Move):
    def __init__(self, name="Bonemerang", desc="Hits twice in one turn.", move_type="GROUND", power=50, accuracy=90, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bonemerang"] = Bonemerang() 

class Bubble(Move):
    def __init__(self, name="Bubble", desc="May lower opponent's Speed.", move_type="WATER", power=40, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bubble"] = Bubble() 

class BubbleBeam(Move):
    def __init__(self, name="Bubble Beam", desc="May lower opponent's Speed.", move_type="WATER", power=65, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bubble Beam"] = BubbleBeam() 

class Clamp(Move):
    def __init__(self, name="Clamp", desc="Traps opponent, damaging them for 4-5 turns.", move_type="WATER", power=35, accuracy=85, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Clamp"] = Clamp() 

class CometPunch(Move):
    def __init__(self, name="Comet Punch", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=18, accuracy=85, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Comet Punch"] = CometPunch() 

class ConfuseRay(Move):
    def __init__(self, name="Confuse Ray", desc="Confuses opponent.", move_type="GHOST", power=None, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Confuse Ray"] = ConfuseRay() 

class Confusion(Move):
    def __init__(self, name="Confusion", desc="May confuse opponent.", move_type="PSYCHIC", power=50, accuracy=100, pp=25):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Confusion"] = Confusion() 

class Constrict(Move):
    def __init__(self, name="Constrict", desc="May lower opponent's Speed by one stage.", move_type="NORMAL", power=10, accuracy=100, pp=35):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Constrict"] = Constrict() 

class Conversion(Move):
    def __init__(self, name="Conversion", desc="Changes user's type to that of its first move.", move_type="NORMAL", power=None, accuracy=None, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Conversion"] = Conversion() 

class Counter(Move):
    def __init__(self, name="Counter", desc="When hit by a Physical Attack, user strikes back with 2x power.", move_type="FIGHTING", power=None, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Counter"] = Counter() 

class Crabhammer(Move):
    def __init__(self, name="Crabhammer", desc="High critical hit ratio.", move_type="WATER", power=100, accuracy=90, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Crabhammer"] = Crabhammer() 

class Cut(Move):
    def __init__(self, name="Cut", desc="nan", move_type="NORMAL", power=50, accuracy=95, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Cut"] = Cut() 

class DefenseCurl(Move):
    def __init__(self, name="Defense Curl", desc="Raises user's Defense.", move_type="NORMAL", power=None, accuracy=None, pp=40):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Defense Curl"] = DefenseCurl() 

class Dig(Move):
    def __init__(self, name="Dig", desc="Digs underground on first turn, attacks on second. Can also escape from caves.", move_type="GROUND", power=80, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Dig"] = Dig() 

class Disable(Move):
    def __init__(self, name="Disable", desc="Opponent can't use its last attack for a few turns.", move_type="NORMAL", power=None, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Disable"] = Disable() 

class DizzyPunch(Move):
    def __init__(self, name="Dizzy Punch", desc="May confuse opponent.", move_type="NORMAL", power=70, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Dizzy Punch"] = DizzyPunch() 

class DoubleKick(Move):
    def __init__(self, name="Double Kick", desc="Hits twice in one turn.", move_type="FIGHTING", power=30, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Double Kick"] = DoubleKick() 

class DoubleSlap(Move):
    def __init__(self, name="Double Slap", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=15, accuracy=85, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Double Slap"] = DoubleSlap() 

class DoubleTeam(Move):
    def __init__(self, name="Double Team", desc="Raises user's Evasiveness.", move_type="NORMAL", power=None, accuracy=None, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Double Team"] = DoubleTeam() 

class DoubleEdge(Move):
    def __init__(self, name="Double-Edge", desc="User receives recoil damage.", move_type="NORMAL", power=120, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Double-Edge"] = DoubleEdge() 

class DragonRage(Move):
    def __init__(self, name="Dragon Rage", desc="Always inflicts 40 HP.", move_type="DRAGON", power=None, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Dragon Rage"] = DragonRage() 

class DreamEater(Move):
    def __init__(self, name="Dream Eater", desc="User recovers half the HP inflicted on a sleeping opponent.", move_type="PSYCHIC", power=100, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Dream Eater"] = DreamEater() 

class DrillPeck(Move):
    def __init__(self, name="Drill Peck", desc="nan", move_type="FLYING", power=80, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Drill Peck"] = DrillPeck() 

class Earthquake(Move):
    def __init__(self, name="Earthquake", desc="Power is doubled if opponent is underground from using Dig.", move_type="GROUND", power=100, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Earthquake"] = Earthquake() 

class EggBomb(Move):
    def __init__(self, name="Egg Bomb", desc="nan", move_type="NORMAL", power=100, accuracy=75, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Egg Bomb"] = EggBomb() 

class Ember(Move):
    def __init__(self, name="Ember", desc="May burn opponent.", move_type="FIRE", power=40, accuracy=100, pp=25):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Ember"] = Ember() 

class Explosion(Move):
    def __init__(self, name="Explosion", desc="User faints.", move_type="NORMAL", power=250, accuracy=100, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Explosion"] = Explosion() 

class FireBlast(Move):
    def __init__(self, name="Fire Blast", desc="May burn opponent.", move_type="FIRE", power=110, accuracy=85, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fire Blast"] = FireBlast() 

class FirePunch(Move):
    def __init__(self, name="Fire Punch", desc="May burn opponent.", move_type="FIRE", power=75, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fire Punch"] = FirePunch() 

class FireSpin(Move):
    def __init__(self, name="Fire Spin", desc="Traps opponent, damaging them for 4-5 turns.", move_type="FIRE", power=35, accuracy=85, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fire Spin"] = FireSpin() 

class Fissure(Move):
    def __init__(self, name="Fissure", desc="One-Hit-KO, if it hits.", move_type="GROUND", power=None, accuracy=30, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fissure"] = Fissure() 

class Flamethrower(Move):
    def __init__(self, name="Flamethrower", desc="May burn opponent.", move_type="FIRE", power=90, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Flamethrower"] = Flamethrower() 

class Flash(Move):
    def __init__(self, name="Flash", desc="Lowers opponent's Accuracy.", move_type="NORMAL", power=None, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Flash"] = Flash() 

class Fly(Move):
    def __init__(self, name="Fly", desc="Flies up on first turn, attacks on second turn.", move_type="FLYING", power=90, accuracy=95, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fly"] = Fly() 

class FocusEnergy(Move):
    def __init__(self, name="Focus Energy", desc="Increases critical hit ratio.", move_type="NORMAL", power=None, accuracy=None, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Focus Energy"] = FocusEnergy() 

class FuryAttack(Move):
    def __init__(self, name="Fury Attack", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=15, accuracy=85, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fury Attack"] = FuryAttack() 

class FurySwipes(Move):
    def __init__(self, name="Fury Swipes", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=18, accuracy=80, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fury Swipes"] = FurySwipes() 

class Glare(Move):
    def __init__(self, name="Glare", desc="Paralyzes opponent.", move_type="NORMAL", power=None, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Glare"] = Glare() 

class Growl(Move):
    def __init__(self, name="Growl", desc="Lowers opponent's Attack.", move_type="NORMAL", power=None, accuracy=100, pp=40):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Growl"] = Growl() 

class Growth(Move):
    def __init__(self, name="Growth", desc="Raises user's Attack and Special Attack.", move_type="NORMAL", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Growth"] = Growth() 

class Guillotine(Move):
    def __init__(self, name="Guillotine", desc="One-Hit-KO, if it hits.", move_type="NORMAL", power=None, accuracy=30, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Guillotine"] = Guillotine() 

class Gust(Move):
    def __init__(self, name="Gust", desc="Hits Pok�mon using Fly/Bounce/Sky Drop with double power.", move_type="FLYING", power=40, accuracy=100, pp=35):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Gust"] = Gust() 

class Harden(Move):
    def __init__(self, name="Harden", desc="Raises user's Defense.", move_type="NORMAL", power=None, accuracy=None, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Harden"] = Harden() 

class Haze(Move):
    def __init__(self, name="Haze", desc="Resets all stat changes.", move_type="ICE", power=None, accuracy=None, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Haze"] = Haze() 

class Headbutt(Move):
    def __init__(self, name="Headbutt", desc="May cause flinching.", move_type="NORMAL", power=70, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Headbutt"] = Headbutt() 

class HighJumpKick(Move):
    def __init__(self, name="High Jump Kick", desc="If it misses, the user loses half their HP.", move_type="FIGHTING", power=130, accuracy=90, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["High Jump Kick"] = HighJumpKick() 

class HornAttack(Move):
    def __init__(self, name="Horn Attack", desc="nan", move_type="NORMAL", power=65, accuracy=100, pp=25):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Horn Attack"] = HornAttack() 

class HornDrill(Move):
    def __init__(self, name="Horn Drill", desc="One-Hit-KO, if it hits.", move_type="NORMAL", power=None, accuracy=30, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Horn Drill"] = HornDrill() 

class HydroPump(Move):
    def __init__(self, name="Hydro Pump", desc="nan", move_type="WATER", power=110, accuracy=80, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Hydro Pump"] = HydroPump() 

class HyperBeam(Move):
    def __init__(self, name="Hyper Beam", desc="User must recharge next turn.", move_type="NORMAL", power=150, accuracy=90, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Hyper Beam"] = HyperBeam() 

class HyperFang(Move):
    def __init__(self, name="Hyper Fang", desc="May cause flinching.", move_type="NORMAL", power=80, accuracy=90, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Hyper Fang"] = HyperFang() 

class Hypnosis(Move):
    def __init__(self, name="Hypnosis", desc="Puts opponent to sleep.", move_type="PSYCHIC", power=None, accuracy=60, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Hypnosis"] = Hypnosis() 

class IceBeam(Move):
    def __init__(self, name="Ice Beam", desc="May freeze opponent.", move_type="ICE", power=90, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Ice Beam"] = IceBeam() 

class IcePunch(Move):
    def __init__(self, name="Ice Punch", desc="May freeze opponent.", move_type="ICE", power=75, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Ice Punch"] = IcePunch() 

class JumpKick(Move):
    def __init__(self, name="Jump Kick", desc="If it misses, the user loses half their HP.", move_type="FIGHTING", power=100, accuracy=95, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Jump Kick"] = JumpKick() 

class KarateChop(Move):
    def __init__(self, name="Karate Chop", desc="High critical hit ratio.", move_type="FIGHTING", power=50, accuracy=100, pp=25):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Karate Chop"] = KarateChop() 

class Kinesis(Move):
    def __init__(self, name="Kinesis", desc="Lowers opponent's Accuracy.", move_type="PSYCHIC", power=None, accuracy=80, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Kinesis"] = Kinesis() 

class LeechLife(Move):
    def __init__(self, name="Leech Life", desc="User recovers half the HP inflicted on opponent.", move_type="BUG", power=80, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Leech Life"] = LeechLife() 

class LeechSeed(Move):
    def __init__(self, name="Leech Seed", desc="Drains HP from opponent each turn.", move_type="GRASS", power=None, accuracy=90, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Leech Seed"] = LeechSeed() 

class Leer(Move):
    def __init__(self, name="Leer", desc="Lowers opponent's Defense.", move_type="NORMAL", power=None, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Leer"] = Leer() 

class Lick(Move):
    def __init__(self, name="Lick", desc="May paralyze opponent.", move_type="GHOST", power=30, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Lick"] = Lick() 

class LightScreen(Move):
    def __init__(self, name="Light Screen", desc="Halves damage from Special attacks for 5 turns.", move_type="PSYCHIC", power=None, accuracy=None, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Light Screen"] = LightScreen() 

class LovelyKiss(Move):
    def __init__(self, name="Lovely Kiss", desc="Puts opponent to sleep.", move_type="NORMAL", power=None, accuracy=75, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Lovely Kiss"] = LovelyKiss() 

class LowKick(Move):
    def __init__(self, name="Low Kick", desc="The heavier the opponent, the stronger the attack.", move_type="FIGHTING", power=None, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Low Kick"] = LowKick() 

class Meditate(Move):
    def __init__(self, name="Meditate", desc="Raises user's Attack.", move_type="PSYCHIC", power=None, accuracy=None, pp=40):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Meditate"] = Meditate() 

class MegaDrain(Move):
    def __init__(self, name="Mega Drain", desc="User recovers half the HP inflicted on opponent.", move_type="GRASS", power=40, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mega Drain"] = MegaDrain() 

class MegaKick(Move):
    def __init__(self, name="Mega Kick", desc="nan", move_type="NORMAL", power=120, accuracy=75, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mega Kick"] = MegaKick() 

class MegaPunch(Move):
    def __init__(self, name="Mega Punch", desc="nan", move_type="NORMAL", power=80, accuracy=85, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mega Punch"] = MegaPunch() 

class Metronome(Move):
    def __init__(self, name="Metronome", desc="User performs almost any move in the game at random.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Metronome"] = Metronome() 

class Mimic(Move):
    def __init__(self, name="Mimic", desc="Copies the opponent's last move.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mimic"] = Mimic() 

class Minimize(Move):
    def __init__(self, name="Minimize", desc="Sharply raises user's Evasiveness.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Minimize"] = Minimize() 

class MirrorMove(Move):
    def __init__(self, name="Mirror Move", desc="User performs the opponent's last move.", move_type="FLYING", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mirror Move"] = MirrorMove() 

class Mist(Move):
    def __init__(self, name="Mist", desc="User's stats cannot be changed for a period of time.", move_type="ICE", power=None, accuracy=None, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mist"] = Mist() 

class NightShade(Move):
    def __init__(self, name="Night Shade", desc="Inflicts damage equal to user's level.", move_type="GHOST", power=None, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Night Shade"] = NightShade() 

class PayDay(Move):
    def __init__(self, name="Pay Day", desc="Money is earned after the battle.", move_type="NORMAL", power=40, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Pay Day"] = PayDay() 

class Peck(Move):
    def __init__(self, name="Peck", desc="nan", move_type="FLYING", power=35, accuracy=100, pp=35):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Peck"] = Peck() 

class PetalDance(Move):
    def __init__(self, name="Petal Dance", desc="User attacks for 2-3 turns but then becomes confused.", move_type="GRASS", power=120, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Petal Dance"] = PetalDance() 

class PinMissile(Move):
    def __init__(self, name="Pin Missile", desc="Hits 2-5 times in one turn.", move_type="BUG", power=25, accuracy=95, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Pin Missile"] = PinMissile() 

class PoisonGas(Move):
    def __init__(self, name="Poison Gas", desc="Poisons opponent.", move_type="POISON", power=None, accuracy=90, pp=40):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Poison Gas"] = PoisonGas() 

class PoisonPowder(Move):
    def __init__(self, name="Poison Powder", desc="Poisons opponent.", move_type="POISON", power=None, accuracy=75, pp=35):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Poison Powder"] = PoisonPowder() 

class PoisonSting(Move):
    def __init__(self, name="Poison Sting", desc="May poison the opponent.", move_type="POISON", power=15, accuracy=100, pp=35):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Poison Sting"] = PoisonSting() 

class Pound(Move):
    def __init__(self, name="Pound", desc="nan", move_type="NORMAL", power=40, accuracy=100, pp=35):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Pound"] = Pound() 

class Psybeam(Move):
    def __init__(self, name="Psybeam", desc="May confuse opponent.", move_type="PSYCHIC", power=65, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Psybeam"] = Psybeam() 

class Psychic(Move):
    def __init__(self, name="Psychic", desc="May lower opponent's Special Defense.", move_type="PSYCHIC", power=90, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Psychic"] = Psychic() 

class Psywave(Move):
    def __init__(self, name="Psywave", desc="Inflicts damage 50-150% of user's level.", move_type="PSYCHIC", power=None, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Psywave"] = Psywave() 

class QuickAttack(Move):
    def __init__(self, name="Quick Attack", desc="User attacks first.", move_type="NORMAL", power=40, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Quick Attack"] = QuickAttack() 

class Rage(Move):
    def __init__(self, name="Rage", desc="Raises user's Attack when hit.", move_type="NORMAL", power=20, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Rage"] = Rage() 

class RazorLeaf(Move):
    def __init__(self, name="Razor Leaf", desc="High critical hit ratio.", move_type="GRASS", power=55, accuracy=95, pp=25):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Razor Leaf"] = RazorLeaf() 

class RazorWind(Move):
    def __init__(self, name="Razor Wind", desc="Charges on first turn, attacks on second. High critical hit ratio.", move_type="NORMAL", power=80, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Razor Wind"] = RazorWind() 

class Recover(Move):
    def __init__(self, name="Recover", desc="User recovers half its max HP.", move_type="NORMAL", power=None, accuracy=None, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Recover"] = Recover() 

class Reflect(Move):
    def __init__(self, name="Reflect", desc="Halves damage from Physical attacks for 5 turns.", move_type="PSYCHIC", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Reflect"] = Reflect() 

class Rest(Move):
    def __init__(self, name="Rest", desc="User sleeps for 2 turns, but user is fully healed.", move_type="PSYCHIC", power=None, accuracy=None, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Rest"] = Rest() 

class Roar(Move):
    def __init__(self, name="Roar", desc="In battles, the opponent switches. In the wild, the Pok�mon runs.", move_type="NORMAL", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Roar"] = Roar() 

class RockSlide(Move):
    def __init__(self, name="Rock Slide", desc="May cause flinching.", move_type="ROCK", power=75, accuracy=90, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Rock Slide"] = RockSlide() 

class RockThrow(Move):
    def __init__(self, name="Rock Throw", desc="nan", move_type="ROCK", power=50, accuracy=90, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Rock Throw"] = RockThrow() 

class RollingKick(Move):
    def __init__(self, name="Rolling Kick", desc="May cause flinching.", move_type="FIGHTING", power=60, accuracy=85, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Rolling Kick"] = RollingKick() 

class SandAttack(Move):
    def __init__(self, name="Sand Attack", desc="Lowers opponent's Accuracy.", move_type="GROUND", power=None, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sand Attack"] = SandAttack() 

class Scratch(Move):
    def __init__(self, name="Scratch", desc="nan", move_type="NORMAL", power=40, accuracy=100, pp=35):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Scratch"] = Scratch() 

class Screech(Move):
    def __init__(self, name="Screech", desc="Sharply lowers opponent's Defense.", move_type="NORMAL", power=None, accuracy=85, pp=40):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Screech"] = Screech() 

class SeismicToss(Move):
    def __init__(self, name="Seismic Toss", desc="Inflicts damage equal to user's level.", move_type="FIGHTING", power=None, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Seismic Toss"] = SeismicToss() 

class SelfDestruct(Move):
    def __init__(self, name="Self-Destruct", desc="User faints.", move_type="NORMAL", power=200, accuracy=100, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Self-Destruct"] = SelfDestruct() 

class Sharpen(Move):
    def __init__(self, name="Sharpen", desc="Raises user's Attack.", move_type="NORMAL", power=None, accuracy=None, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sharpen"] = Sharpen() 

class Sing(Move):
    def __init__(self, name="Sing", desc="Puts opponent to sleep.", move_type="NORMAL", power=None, accuracy=55, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sing"] = Sing() 

class SkullBash(Move):
    def __init__(self, name="Skull Bash", desc="Raises Defense on first turn, attacks on second.", move_type="NORMAL", power=130, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Skull Bash"] = SkullBash() 

class SkyAttack(Move):
    def __init__(self, name="Sky Attack", desc="Charges on first turn, attacks on second. May cause flinching. High critical hit ratio.", move_type="FLYING", power=140, accuracy=90, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sky Attack"] = SkyAttack() 

class Slam(Move):
    def __init__(self, name="Slam", desc="nan", move_type="NORMAL", power=80, accuracy=75, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Slam"] = Slam() 

class Slash(Move):
    def __init__(self, name="Slash", desc="High critical hit ratio.", move_type="NORMAL", power=70, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Slash"] = Slash() 

class SleepPowder(Move):
    def __init__(self, name="Sleep Powder", desc="Puts opponent to sleep.", move_type="GRASS", power=None, accuracy=75, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sleep Powder"] = SleepPowder() 

class Sludge(Move):
    def __init__(self, name="Sludge", desc="May poison opponent.", move_type="POISON", power=65, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sludge"] = Sludge() 

class Smog(Move):
    def __init__(self, name="Smog", desc="May poison opponent.", move_type="POISON", power=30, accuracy=70, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Smog"] = Smog() 

class Smokescreen(Move):
    def __init__(self, name="Smokescreen", desc="Lowers opponent's Accuracy.", move_type="NORMAL", power=None, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Smokescreen"] = Smokescreen() 

class SoftBoiled(Move):
    def __init__(self, name="Soft-Boiled", desc="User recovers half its max HP.", move_type="NORMAL", power=None, accuracy=None, pp=5):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Soft-Boiled"] = SoftBoiled() 

class SolarBeam(Move):
    def __init__(self, name="Solar Beam", desc="Charges on first turn, attacks on second.", move_type="GRASS", power=120, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Solar Beam"] = SolarBeam() 

class SonicBoom(Move):
    def __init__(self, name="Sonic Boom", desc="Always inflicts 20 HP.", move_type="NORMAL", power=None, accuracy=90, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sonic Boom"] = SonicBoom() 

class SpikeCannon(Move):
    def __init__(self, name="Spike Cannon", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=20, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Spike Cannon"] = SpikeCannon() 

class Splash(Move):
    def __init__(self, name="Splash", desc="Doesn't do ANYTHING.", move_type="NORMAL", power=None, accuracy=None, pp=40):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Splash"] = Splash() 

class Spore(Move):
    def __init__(self, name="Spore", desc="Puts opponent to sleep.", move_type="GRASS", power=None, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Spore"] = Spore() 

class Stomp(Move):
    def __init__(self, name="Stomp", desc="May cause flinching.", move_type="NORMAL", power=65, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Stomp"] = Stomp() 

class Strength(Move):
    def __init__(self, name="Strength", desc="nan", move_type="NORMAL", power=80, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Strength"] = Strength() 

class StringShot(Move):
    def __init__(self, name="String Shot", desc="Sharply lowers opponent's Speed.", move_type="BUG", power=None, accuracy=95, pp=40):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["String Shot"] = StringShot() 

class Struggle(Move):
    def __init__(self, name="Struggle", desc="Only usable when all PP are gone. Hurts the user.", move_type="NORMAL", power=50, accuracy=None, pp=None):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Struggle"] = Struggle() 

class StunSpore(Move):
    def __init__(self, name="Stun Spore", desc="Paralyzes opponent.", move_type="GRASS", power=None, accuracy=75, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Stun Spore"] = StunSpore() 

class Submission(Move):
    def __init__(self, name="Submission", desc="User receives recoil damage.", move_type="FIGHTING", power=80, accuracy=80, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Submission"] = Submission() 

class Substitute(Move):
    def __init__(self, name="Substitute", desc="Uses HP to creates a decoy that takes hits.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Substitute"] = Substitute() 

class SuperFang(Move):
    def __init__(self, name="Super Fang", desc="Always takes off half of the opponent's HP.", move_type="NORMAL", power=None, accuracy=90, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Super Fang"] = SuperFang() 

class Supersonic(Move):
    def __init__(self, name="Supersonic", desc="Confuses opponent.", move_type="NORMAL", power=None, accuracy=55, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Supersonic"] = Supersonic() 

class Surf(Move):
    def __init__(self, name="Surf", desc="Hits all adjacent Pok�mon.", move_type="WATER", power=90, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Surf"] = Surf() 

class Swift(Move):
    def __init__(self, name="Swift", desc="Ignores Accuracy and Evasiveness.", move_type="NORMAL", power=60, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Swift"] = Swift() 

class SwordsDance(Move):
    def __init__(self, name="Swords Dance", desc="Sharply raises user's Attack.", move_type="NORMAL", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Swords Dance"] = SwordsDance() 

class Tackle(Move):
    def __init__(self, name="Tackle", desc="Charges the foe with a full-body tackle.", move_type="NORMAL", power=35, accuracy=95, pp=35):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Tackle"] = Tackle() 

class TailWhip(Move):
    def __init__(self, name="Tail Whip", desc="Lowers opponent's Defense.", move_type="NORMAL", power=None, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Tail Whip"] = TailWhip() 

class TakeDown(Move):
    def __init__(self, name="Take Down", desc="User receives recoil damage.", move_type="NORMAL", power=90, accuracy=85, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Take Down"] = TakeDown() 

class Teleport(Move):
    def __init__(self, name="Teleport", desc="Allows user to flee wild battles; also warps player to last Pok�Center.", move_type="PSYCHIC", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Teleport"] = Teleport() 

class Thrash(Move):
    def __init__(self, name="Thrash", desc="User attacks for 2-3 turns but then becomes confused.", move_type="NORMAL", power=120, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thrash"] = Thrash() 

class Thunder(Move):
    def __init__(self, name="Thunder", desc="May paralyze opponent.", move_type="ELECTRIC", power=110, accuracy=70, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunder"] = Thunder() 

class ThunderPunch(Move):
    def __init__(self, name="Thunder Punch", desc="May paralyze opponent.", move_type="ELECTRIC", power=75, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunder Punch"] = ThunderPunch() 

class ThunderShock(Move):
    def __init__(self, name="Thunder Shock", desc="May paralyze opponent.", move_type="ELECTRIC", power=40, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunder Shock"] = ThunderShock() 

class ThunderWave(Move):
    def __init__(self, name="Thunder Wave", desc="Paralyzes opponent.", move_type="ELECTRIC", power=None, accuracy=90, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunder Wave"] = ThunderWave() 

class Thunderbolt(Move):
    def __init__(self, name="Thunderbolt", desc="May paralyze opponent.", move_type="ELECTRIC", power=90, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunderbolt"] = Thunderbolt() 

class Toxic(Move):
    def __init__(self, name="Toxic", desc="Badly poisons opponent.", move_type="POISON", power=None, accuracy=90, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Toxic"] = Toxic() 

class Transform(Move):
    def __init__(self, name="Transform", desc="User takes on the form and attacks of the opponent.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Transform"] = Transform() 

class TriAttack(Move):
    def __init__(self, name="Tri Attack", desc="May paralyze, burn or freeze opponent.", move_type="NORMAL", power=80, accuracy=100, pp=10):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Tri Attack"] = TriAttack() 

class Twineedle(Move):
    def __init__(self, name="Twineedle", desc="Hits twice in one turn. May poison opponent.", move_type="BUG", power=25, accuracy=100, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Twineedle"] = Twineedle() 

class VineWhip(Move):
    def __init__(self, name="Vine Whip", desc="nan", move_type="GRASS", power=45, accuracy=100, pp=25):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Vine Whip"] = VineWhip() 

class ViseGrip(Move):
    def __init__(self, name="Vise Grip", desc="nan", move_type="NORMAL", power=55, accuracy=100, pp=30):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Vise Grip"] = ViseGrip() 

class WaterGun(Move):
    def __init__(self, name="Water Gun", desc="nan", move_type="WATER", power=40, accuracy=100, pp=25):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Water Gun"] = WaterGun() 

class Waterfall(Move):
    def __init__(self, name="Waterfall", desc="May cause flinching.", move_type="WATER", power=80, accuracy=100, pp=15):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Waterfall"] = Waterfall() 

class Whirlwind(Move):
    def __init__(self, name="Whirlwind", desc="In battles, the opponent switches. In the wild, the Pok�mon runs.", move_type="NORMAL", power=None, accuracy=None, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Whirlwind"] = Whirlwind() 

class WingAttack(Move):
    def __init__(self, name="Wing Attack", desc="nan", move_type="FLYING", power=60, accuracy=100, pp=35):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Wing Attack"] = WingAttack() 

class Withdraw(Move):
    def __init__(self, name="Withdraw", desc="Raises user's Defense.", move_type="WATER", power=None, accuracy=None, pp=40):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Withdraw"] = Withdraw() 

class Wrap(Move):
    def __init__(self, name="Wrap", desc="Traps opponent, damaging them for 4-5 turns.", move_type="NORMAL", power=15, accuracy=90, pp=20):
        super().__init__(name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Wrap"] = Wrap() 


