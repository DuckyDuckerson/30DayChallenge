class Move:
    def __init__(self, pokemon, name, desc, move_type, power, accuracy, pp):
        self.pokemon = pokemon
        self.name = name
        self.desc = desc
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

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
        if self.is_special:
            pass
            #use special attack and defend stats
        elif self.is_physical:
            pass
            #use regular atk and defend stats of pokemon
    
ALL_MOVES = {}

class Absorb(Move):
    def __init__(self, pokemon, name="Absorb", desc="Restores the user's HP by 1/2 of the damage inflicted on the target.", move_type="Grass", power=20, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass
        
class Acid(Move):
    def __init__(self, pokemon, name="Acid", desc="May lower opponent's Special Defense.", move_type="POISON", power=40, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Acid"] = Acid(pokemon=[]) 

class AcidArmor(Move):
    def __init__(self, pokemon, name="Acid Armor", desc="Sharply raises user's Defense.", move_type="POISON", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Acid Armor"] = AcidArmor(pokemon=[]) 

class Agility(Move):
    def __init__(self, pokemon, name="Agility", desc="Sharply raises user's Speed.", move_type="PSYCHIC", power=None, accuracy=None, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Agility"] = Agility(pokemon=[]) 

class Amnesia(Move):
    def __init__(self, pokemon, name="Amnesia", desc="Sharply raises user's Special Defense.", move_type="PSYCHIC", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Amnesia"] = Amnesia(pokemon=[]) 

class AuroraBeam(Move):
    def __init__(self, pokemon, name="Aurora Beam", desc="May lower opponent's Attack.", move_type="ICE", power=65, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Aurora Beam"] = AuroraBeam(pokemon=[]) 

class Barrage(Move):
    def __init__(self, pokemon, name="Barrage", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=15, accuracy=85, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Barrage"] = Barrage(pokemon=[]) 

class Barrier(Move):
    def __init__(self, pokemon, name="Barrier", desc="Sharply raises user's Defense.", move_type="PSYCHIC", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Barrier"] = Barrier(pokemon=[]) 

class Bide(Move):
    def __init__(self, pokemon, name="Bide", desc="User takes damage for two turns then strikes back double.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bide"] = Bide(pokemon=[]) 

class Bind(Move):
    def __init__(self, pokemon, name="Bind", desc="Traps opponent, damaging them for 4-5 turns.", move_type="NORMAL", power=15, accuracy=85, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bind"] = Bind(pokemon=[]) 

class Bite(Move):
    def __init__(self, pokemon, name="Bite", desc="May cause flinching.", move_type="DARK", power=60, accuracy=100, pp=25):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bite"] = Bite(pokemon=[]) 

class Blizzard(Move):
    def __init__(self, pokemon, name="Blizzard", desc="May freeze opponent.", move_type="ICE", power=110, accuracy=70, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Blizzard"] = Blizzard(pokemon=[]) 

class BodySlam(Move):
    def __init__(self, pokemon, name="Body Slam", desc="May paralyze opponent.", move_type="NORMAL", power=85, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Body Slam"] = BodySlam(pokemon=[]) 

class BoneClub(Move):
    def __init__(self, pokemon, name="Bone Club", desc="May cause flinching.", move_type="GROUND", power=65, accuracy=85, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bone Club"] = BoneClub(pokemon=[]) 

class Bonemerang(Move):
    def __init__(self, pokemon, name="Bonemerang", desc="Hits twice in one turn.", move_type="GROUND", power=50, accuracy=90, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bonemerang"] = Bonemerang(pokemon=[]) 

class Bubble(Move):
    def __init__(self, pokemon, name="Bubble", desc="May lower opponent's Speed.", move_type="WATER", power=40, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bubble"] = Bubble(pokemon=[]) 

class BubbleBeam(Move):
    def __init__(self, pokemon, name="Bubble Beam", desc="May lower opponent's Speed.", move_type="WATER", power=65, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Bubble Beam"] = BubbleBeam(pokemon=[]) 

class Clamp(Move):
    def __init__(self, pokemon, name="Clamp", desc="Traps opponent, damaging them for 4-5 turns.", move_type="WATER", power=35, accuracy=85, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Clamp"] = Clamp(pokemon=[]) 

class CometPunch(Move):
    def __init__(self, pokemon, name="Comet Punch", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=18, accuracy=85, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Comet Punch"] = CometPunch(pokemon=[]) 

class ConfuseRay(Move):
    def __init__(self, pokemon, name="Confuse Ray", desc="Confuses opponent.", move_type="GHOST", power=None, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Confuse Ray"] = ConfuseRay(pokemon=[]) 

class Confusion(Move):
    def __init__(self, pokemon, name="Confusion", desc="May confuse opponent.", move_type="PSYCHIC", power=50, accuracy=100, pp=25):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Confusion"] = Confusion(pokemon=[]) 

class Constrict(Move):
    def __init__(self, pokemon, name="Constrict", desc="May lower opponent's Speed by one stage.", move_type="NORMAL", power=10, accuracy=100, pp=35):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Constrict"] = Constrict(pokemon=[]) 

class Conversion(Move):
    def __init__(self, pokemon, name="Conversion", desc="Changes user's type to that of its first move.", move_type="NORMAL", power=None, accuracy=None, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Conversion"] = Conversion(pokemon=[]) 

class Counter(Move):
    def __init__(self, pokemon, name="Counter", desc="When hit by a Physical Attack, user strikes back with 2x power.", move_type="FIGHTING", power=None, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Counter"] = Counter(pokemon=[]) 

class Crabhammer(Move):
    def __init__(self, pokemon, name="Crabhammer", desc="High critical hit ratio.", move_type="WATER", power=100, accuracy=90, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Crabhammer"] = Crabhammer(pokemon=[]) 

class Cut(Move):
    def __init__(self, pokemon, name="Cut", desc="nan", move_type="NORMAL", power=50, accuracy=95, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Cut"] = Cut(pokemon=[]) 

class DefenseCurl(Move):
    def __init__(self, pokemon, name="Defense Curl", desc="Raises user's Defense.", move_type="NORMAL", power=None, accuracy=None, pp=40):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Defense Curl"] = DefenseCurl(pokemon=[]) 

class Dig(Move):
    def __init__(self, pokemon, name="Dig", desc="Digs underground on first turn, attacks on second. Can also escape from caves.", move_type="GROUND", power=80, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Dig"] = Dig(pokemon=[]) 

class Disable(Move):
    def __init__(self, pokemon, name="Disable", desc="Opponent can't use its last attack for a few turns.", move_type="NORMAL", power=None, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Disable"] = Disable(pokemon=[]) 

class DizzyPunch(Move):
    def __init__(self, pokemon, name="Dizzy Punch", desc="May confuse opponent.", move_type="NORMAL", power=70, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Dizzy Punch"] = DizzyPunch(pokemon=[]) 

class DoubleKick(Move):
    def __init__(self, pokemon, name="Double Kick", desc="Hits twice in one turn.", move_type="FIGHTING", power=30, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Double Kick"] = DoubleKick(pokemon=[]) 

class DoubleSlap(Move):
    def __init__(self, pokemon, name="Double Slap", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=15, accuracy=85, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Double Slap"] = DoubleSlap(pokemon=[]) 

class DoubleTeam(Move):
    def __init__(self, pokemon, name="Double Team", desc="Raises user's Evasiveness.", move_type="NORMAL", power=None, accuracy=None, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Double Team"] = DoubleTeam(pokemon=[]) 

class DoubleEdge(Move):
    def __init__(self, pokemon, name="Double-Edge", desc="User receives recoil damage.", move_type="NORMAL", power=120, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Double-Edge"] = DoubleEdge(pokemon=[]) 

class DragonRage(Move):
    def __init__(self, pokemon, name="Dragon Rage", desc="Always inflicts 40 HP.", move_type="DRAGON", power=None, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Dragon Rage"] = DragonRage(pokemon=[]) 

class DreamEater(Move):
    def __init__(self, pokemon, name="Dream Eater", desc="User recovers half the HP inflicted on a sleeping opponent.", move_type="PSYCHIC", power=100, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Dream Eater"] = DreamEater(pokemon=[]) 

class DrillPeck(Move):
    def __init__(self, pokemon, name="Drill Peck", desc="nan", move_type="FLYING", power=80, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Drill Peck"] = DrillPeck(pokemon=[]) 

class Earthquake(Move):
    def __init__(self, pokemon, name="Earthquake", desc="Power is doubled if opponent is underground from using Dig.", move_type="GROUND", power=100, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Earthquake"] = Earthquake(pokemon=[]) 

class EggBomb(Move):
    def __init__(self, pokemon, name="Egg Bomb", desc="nan", move_type="NORMAL", power=100, accuracy=75, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Egg Bomb"] = EggBomb(pokemon=[]) 

class Ember(Move):
    def __init__(self, pokemon, name="Ember", desc="May burn opponent.", move_type="FIRE", power=40, accuracy=100, pp=25):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Ember"] = Ember(pokemon=[]) 

class Explosion(Move):
    def __init__(self, pokemon, name="Explosion", desc="User faints.", move_type="NORMAL", power=250, accuracy=100, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Explosion"] = Explosion(pokemon=[]) 

class FireBlast(Move):
    def __init__(self, pokemon, name="Fire Blast", desc="May burn opponent.", move_type="FIRE", power=110, accuracy=85, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fire Blast"] = FireBlast(pokemon=[]) 

class FirePunch(Move):
    def __init__(self, pokemon, name="Fire Punch", desc="May burn opponent.", move_type="FIRE", power=75, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fire Punch"] = FirePunch(pokemon=[]) 

class FireSpin(Move):
    def __init__(self, pokemon, name="Fire Spin", desc="Traps opponent, damaging them for 4-5 turns.", move_type="FIRE", power=35, accuracy=85, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fire Spin"] = FireSpin(pokemon=[]) 

class Fissure(Move):
    def __init__(self, pokemon, name="Fissure", desc="One-Hit-KO, if it hits.", move_type="GROUND", power=None, accuracy=30, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fissure"] = Fissure(pokemon=[]) 

class Flamethrower(Move):
    def __init__(self, pokemon, name="Flamethrower", desc="May burn opponent.", move_type="FIRE", power=90, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Flamethrower"] = Flamethrower(pokemon=[]) 

class Flash(Move):
    def __init__(self, pokemon, name="Flash", desc="Lowers opponent's Accuracy.", move_type="NORMAL", power=None, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Flash"] = Flash(pokemon=[]) 

class Fly(Move):
    def __init__(self, pokemon, name="Fly", desc="Flies up on first turn, attacks on second turn.", move_type="FLYING", power=90, accuracy=95, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fly"] = Fly(pokemon=[]) 

class FocusEnergy(Move):
    def __init__(self, pokemon, name="Focus Energy", desc="Increases critical hit ratio.", move_type="NORMAL", power=None, accuracy=None, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Focus Energy"] = FocusEnergy(pokemon=[]) 

class FuryAttack(Move):
    def __init__(self, pokemon, name="Fury Attack", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=15, accuracy=85, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fury Attack"] = FuryAttack(pokemon=[]) 

class FurySwipes(Move):
    def __init__(self, pokemon, name="Fury Swipes", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=18, accuracy=80, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Fury Swipes"] = FurySwipes(pokemon=[]) 

class Glare(Move):
    def __init__(self, pokemon, name="Glare", desc="Paralyzes opponent.", move_type="NORMAL", power=None, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Glare"] = Glare(pokemon=[]) 

class Growl(Move):
    def __init__(self, pokemon, name="Growl", desc="Lowers opponent's Attack.", move_type="NORMAL", power=None, accuracy=100, pp=40):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Growl"] = Growl(pokemon=[]) 

class Growth(Move):
    def __init__(self, pokemon, name="Growth", desc="Raises user's Attack and Special Attack.", move_type="NORMAL", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Growth"] = Growth(pokemon=[]) 

class Guillotine(Move):
    def __init__(self, pokemon, name="Guillotine", desc="One-Hit-KO, if it hits.", move_type="NORMAL", power=None, accuracy=30, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Guillotine"] = Guillotine(pokemon=[]) 

class Gust(Move):
    def __init__(self, pokemon, name="Gust", desc="Hits Pok�mon using Fly/Bounce/Sky Drop with double power.", move_type="FLYING", power=40, accuracy=100, pp=35):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Gust"] = Gust(pokemon=[]) 

class Harden(Move):
    def __init__(self, pokemon, name="Harden", desc="Raises user's Defense.", move_type="NORMAL", power=None, accuracy=None, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Harden"] = Harden(pokemon=[]) 

class Haze(Move):
    def __init__(self, pokemon, name="Haze", desc="Resets all stat changes.", move_type="ICE", power=None, accuracy=None, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Haze"] = Haze(pokemon=[]) 

class Headbutt(Move):
    def __init__(self, pokemon, name="Headbutt", desc="May cause flinching.", move_type="NORMAL", power=70, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Headbutt"] = Headbutt(pokemon=[]) 

class HighJumpKick(Move):
    def __init__(self, pokemon, name="High Jump Kick", desc="If it misses, the user loses half their HP.", move_type="FIGHTING", power=130, accuracy=90, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["High Jump Kick"] = HighJumpKick(pokemon=[]) 

class HornAttack(Move):
    def __init__(self, pokemon, name="Horn Attack", desc="nan", move_type="NORMAL", power=65, accuracy=100, pp=25):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Horn Attack"] = HornAttack(pokemon=[]) 

class HornDrill(Move):
    def __init__(self, pokemon, name="Horn Drill", desc="One-Hit-KO, if it hits.", move_type="NORMAL", power=None, accuracy=30, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Horn Drill"] = HornDrill(pokemon=[]) 

class HydroPump(Move):
    def __init__(self, pokemon, name="Hydro Pump", desc="nan", move_type="WATER", power=110, accuracy=80, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Hydro Pump"] = HydroPump(pokemon=[]) 

class HyperBeam(Move):
    def __init__(self, pokemon, name="Hyper Beam", desc="User must recharge next turn.", move_type="NORMAL", power=150, accuracy=90, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Hyper Beam"] = HyperBeam(pokemon=[]) 

class HyperFang(Move):
    def __init__(self, pokemon, name="Hyper Fang", desc="May cause flinching.", move_type="NORMAL", power=80, accuracy=90, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Hyper Fang"] = HyperFang(pokemon=[]) 

class Hypnosis(Move):
    def __init__(self, pokemon, name="Hypnosis", desc="Puts opponent to sleep.", move_type="PSYCHIC", power=None, accuracy=60, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Hypnosis"] = Hypnosis(pokemon=[]) 

class IceBeam(Move):
    def __init__(self, pokemon, name="Ice Beam", desc="May freeze opponent.", move_type="ICE", power=90, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Ice Beam"] = IceBeam(pokemon=[]) 

class IcePunch(Move):
    def __init__(self, pokemon, name="Ice Punch", desc="May freeze opponent.", move_type="ICE", power=75, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Ice Punch"] = IcePunch(pokemon=[]) 

class JumpKick(Move):
    def __init__(self, pokemon, name="Jump Kick", desc="If it misses, the user loses half their HP.", move_type="FIGHTING", power=100, accuracy=95, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Jump Kick"] = JumpKick(pokemon=[]) 

class KarateChop(Move):
    def __init__(self, pokemon, name="Karate Chop", desc="High critical hit ratio.", move_type="FIGHTING", power=50, accuracy=100, pp=25):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Karate Chop"] = KarateChop(pokemon=[]) 

class Kinesis(Move):
    def __init__(self, pokemon, name="Kinesis", desc="Lowers opponent's Accuracy.", move_type="PSYCHIC", power=None, accuracy=80, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Kinesis"] = Kinesis(pokemon=[]) 

class LeechLife(Move):
    def __init__(self, pokemon, name="Leech Life", desc="User recovers half the HP inflicted on opponent.", move_type="BUG", power=80, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Leech Life"] = LeechLife(pokemon=[]) 

class LeechSeed(Move):
    def __init__(self, pokemon, name="Leech Seed", desc="Drains HP from opponent each turn.", move_type="GRASS", power=None, accuracy=90, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Leech Seed"] = LeechSeed(pokemon=[]) 

class Leer(Move):
    def __init__(self, pokemon, name="Leer", desc="Lowers opponent's Defense.", move_type="NORMAL", power=None, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Leer"] = Leer(pokemon=[]) 

class Lick(Move):
    def __init__(self, pokemon, name="Lick", desc="May paralyze opponent.", move_type="GHOST", power=30, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Lick"] = Lick(pokemon=[]) 

class LightScreen(Move):
    def __init__(self, pokemon, name="Light Screen", desc="Halves damage from Special attacks for 5 turns.", move_type="PSYCHIC", power=None, accuracy=None, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Light Screen"] = LightScreen(pokemon=[]) 

class LovelyKiss(Move):
    def __init__(self, pokemon, name="Lovely Kiss", desc="Puts opponent to sleep.", move_type="NORMAL", power=None, accuracy=75, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Lovely Kiss"] = LovelyKiss(pokemon=[]) 

class LowKick(Move):
    def __init__(self, pokemon, name="Low Kick", desc="The heavier the opponent, the stronger the attack.", move_type="FIGHTING", power=None, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Low Kick"] = LowKick(pokemon=[]) 

class Meditate(Move):
    def __init__(self, pokemon, name="Meditate", desc="Raises user's Attack.", move_type="PSYCHIC", power=None, accuracy=None, pp=40):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Meditate"] = Meditate(pokemon=[]) 

class MegaDrain(Move):
    def __init__(self, pokemon, name="Mega Drain", desc="User recovers half the HP inflicted on opponent.", move_type="GRASS", power=40, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mega Drain"] = MegaDrain(pokemon=[]) 

class MegaKick(Move):
    def __init__(self, pokemon, name="Mega Kick", desc="nan", move_type="NORMAL", power=120, accuracy=75, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mega Kick"] = MegaKick(pokemon=[]) 

class MegaPunch(Move):
    def __init__(self, pokemon, name="Mega Punch", desc="nan", move_type="NORMAL", power=80, accuracy=85, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mega Punch"] = MegaPunch(pokemon=[]) 

class Metronome(Move):
    def __init__(self, pokemon, name="Metronome", desc="User performs almost any move in the game at random.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Metronome"] = Metronome(pokemon=[]) 

class Mimic(Move):
    def __init__(self, pokemon, name="Mimic", desc="Copies the opponent's last move.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mimic"] = Mimic(pokemon=[]) 

class Minimize(Move):
    def __init__(self, pokemon, name="Minimize", desc="Sharply raises user's Evasiveness.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Minimize"] = Minimize(pokemon=[]) 

class MirrorMove(Move):
    def __init__(self, pokemon, name="Mirror Move", desc="User performs the opponent's last move.", move_type="FLYING", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mirror Move"] = MirrorMove(pokemon=[]) 

class Mist(Move):
    def __init__(self, pokemon, name="Mist", desc="User's stats cannot be changed for a period of time.", move_type="ICE", power=None, accuracy=None, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Mist"] = Mist(pokemon=[]) 

class NightShade(Move):
    def __init__(self, pokemon, name="Night Shade", desc="Inflicts damage equal to user's level.", move_type="GHOST", power=None, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Night Shade"] = NightShade(pokemon=[]) 

class PayDay(Move):
    def __init__(self, pokemon, name="Pay Day", desc="Money is earned after the battle.", move_type="NORMAL", power=40, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Pay Day"] = PayDay(pokemon=[]) 

class Peck(Move):
    def __init__(self, pokemon, name="Peck", desc="nan", move_type="FLYING", power=35, accuracy=100, pp=35):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Peck"] = Peck(pokemon=[]) 

class PetalDance(Move):
    def __init__(self, pokemon, name="Petal Dance", desc="User attacks for 2-3 turns but then becomes confused.", move_type="GRASS", power=120, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Petal Dance"] = PetalDance(pokemon=[]) 

class PinMissile(Move):
    def __init__(self, pokemon, name="Pin Missile", desc="Hits 2-5 times in one turn.", move_type="BUG", power=25, accuracy=95, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Pin Missile"] = PinMissile(pokemon=[]) 

class PoisonGas(Move):
    def __init__(self, pokemon, name="Poison Gas", desc="Poisons opponent.", move_type="POISON", power=None, accuracy=90, pp=40):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Poison Gas"] = PoisonGas(pokemon=[]) 

class PoisonPowder(Move):
    def __init__(self, pokemon, name="Poison Powder", desc="Poisons opponent.", move_type="POISON", power=None, accuracy=75, pp=35):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Poison Powder"] = PoisonPowder(pokemon=[]) 

class PoisonSting(Move):
    def __init__(self, pokemon, name="Poison Sting", desc="May poison the opponent.", move_type="POISON", power=15, accuracy=100, pp=35):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Poison Sting"] = PoisonSting(pokemon=[]) 

class Pound(Move):
    def __init__(self, pokemon, name="Pound", desc="nan", move_type="NORMAL", power=40, accuracy=100, pp=35):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Pound"] = Pound(pokemon=[]) 

class Psybeam(Move):
    def __init__(self, pokemon, name="Psybeam", desc="May confuse opponent.", move_type="PSYCHIC", power=65, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Psybeam"] = Psybeam(pokemon=[]) 

class Psychic(Move):
    def __init__(self, pokemon, name="Psychic", desc="May lower opponent's Special Defense.", move_type="PSYCHIC", power=90, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Psychic"] = Psychic(pokemon=[]) 

class Psywave(Move):
    def __init__(self, pokemon, name="Psywave", desc="Inflicts damage 50-150% of user's level.", move_type="PSYCHIC", power=None, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Psywave"] = Psywave(pokemon=[]) 

class QuickAttack(Move):
    def __init__(self, pokemon, name="Quick Attack", desc="User attacks first.", move_type="NORMAL", power=40, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Quick Attack"] = QuickAttack(pokemon=[]) 

class Rage(Move):
    def __init__(self, pokemon, name="Rage", desc="Raises user's Attack when hit.", move_type="NORMAL", power=20, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass
tm = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Butterfree", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Gyarados", "Lapras", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
level = [
  {
    "pokemon": "Charmander",
    "level": 22
  },
  {
    "pokemon": "Charmeleon",
    "level": 24
  },
  {
    "pokemon": "Charizard",
    "level": 24
  },
  {
    "pokemon": "Beedrill",
    "level": 25
  },
  {
    "pokemon": "Primeape",
    "level": 28
  },
  {
    "pokemon": "Doduo",
    "level": 36
  },
  {
    "pokemon": "Dodrio",
    "level": 39
  },
  {
    "pokemon": "Onix",
    "level": 25
  },
  {
    "pokemon": "Cubone",
    "level": 46
  },
  {
    "pokemon": "Marowak",
    "level": 55
  },
  {
    "pokemon": "Kangaskhan",
    "level": 1
  },
  {
    "pokemon": "Tauros",
    "level": 44
  },
  {
    "pokemon": "Flareon",
    "level": 48
  }
]
ALL_MOVES["Rage"] = Rage(pokemon={'level': level, "tm": tm}) 

class RazorLeaf(Move):
    def __init__(self, pokemon, name="Razor Leaf", desc="High critical hit ratio.", move_type="GRASS", power=55, accuracy=95, pp=25):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Razor Leaf"] = RazorLeaf(pokemon=[]) 

class RazorWind(Move):
    def __init__(self, pokemon, name="Razor Wind", desc="Charges on first turn, attacks on second. High critical hit ratio.", move_type="NORMAL", power=80, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Razor Wind"] = RazorWind(pokemon=[]) 

class Recover(Move):
    def __init__(self, pokemon, name="Recover", desc="User recovers half its max HP.", move_type="NORMAL", power=None, accuracy=None, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Recover"] = Recover(pokemon=[]) 

class Reflect(Move):
    def __init__(self, pokemon, name="Reflect", desc="Halves damage from Physical attacks for 5 turns.", move_type="PSYCHIC", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Reflect"] = Reflect(pokemon=[]) 

class Rest(Move):
    def __init__(self, pokemon, name="Rest", desc="User sleeps for 2 turns, but user is fully healed.", move_type="PSYCHIC", power=None, accuracy=None, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Rest"] = Rest(pokemon=[]) 

class Roar(Move):
    def __init__(self, pokemon, name="Roar", desc="In battles, the opponent switches. In the wild, the Pok�mon runs.", move_type="NORMAL", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Roar"] = Roar(pokemon=[]) 

class RockSlide(Move):
    def __init__(self, pokemon, name="Rock Slide", desc="May cause flinching.", move_type="ROCK", power=75, accuracy=90, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Rock Slide"] = RockSlide(pokemon=[]) 

class RockThrow(Move):
    def __init__(self, pokemon, name="Rock Throw", desc="nan", move_type="ROCK", power=50, accuracy=90, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Rock Throw"] = RockThrow(pokemon=[]) 

class RollingKick(Move):
    def __init__(self, pokemon, name="Rolling Kick", desc="May cause flinching.", move_type="FIGHTING", power=60, accuracy=85, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Rolling Kick"] = RollingKick(pokemon=[]) 

class SandAttack(Move):
    def __init__(self, pokemon, name="Sand Attack", desc="Lowers opponent's Accuracy.", move_type="GROUND", power=None, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sand Attack"] = SandAttack(pokemon=[]) 

class Scratch(Move):
    def __init__(self, pokemon, name="Scratch", desc="nan", move_type="NORMAL", power=40, accuracy=100, pp=35):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Scratch"] = Scratch(pokemon=[]) 

class Screech(Move):
    def __init__(self, pokemon, name="Screech", desc="Sharply lowers opponent's Defense.", move_type="NORMAL", power=None, accuracy=85, pp=40):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Screech"] = Screech(pokemon=[]) 

class SeismicToss(Move):
    def __init__(self, pokemon, name="Seismic Toss", desc="Inflicts damage equal to user's level.", move_type="FIGHTING", power=None, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Seismic Toss"] = SeismicToss(pokemon=[]) 

class SelfDestruct(Move):
    def __init__(self, pokemon, name="Self-Destruct", desc="User faints.", move_type="NORMAL", power=200, accuracy=100, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Self-Destruct"] = SelfDestruct(pokemon=[]) 

class Sharpen(Move):
    def __init__(self, pokemon, name="Sharpen", desc="Raises user's Attack.", move_type="NORMAL", power=None, accuracy=None, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sharpen"] = Sharpen(pokemon=[]) 

class Sing(Move):
    def __init__(self, pokemon, name="Sing", desc="Puts opponent to sleep.", move_type="NORMAL", power=None, accuracy=55, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sing"] = Sing(pokemon=[]) 

class SkullBash(Move):
    def __init__(self, pokemon, name="Skull Bash", desc="Raises Defense on first turn, attacks on second.", move_type="NORMAL", power=130, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Skull Bash"] = SkullBash(pokemon=[]) 

class SkyAttack(Move):
    def __init__(self, pokemon, name="Sky Attack", desc="Charges on first turn, attacks on second. May cause flinching. High critical hit ratio.", move_type="FLYING", power=140, accuracy=90, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sky Attack"] = SkyAttack(pokemon=[]) 

class Slam(Move):
    def __init__(self, pokemon, name="Slam", desc="nan", move_type="NORMAL", power=80, accuracy=75, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Slam"] = Slam(pokemon=[]) 

class Slash(Move):
    def __init__(self, pokemon, name="Slash", desc="High critical hit ratio.", move_type="NORMAL", power=70, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Slash"] = Slash(pokemon=[]) 

class SleepPowder(Move):
    def __init__(self, pokemon, name="Sleep Powder", desc="Puts opponent to sleep.", move_type="GRASS", power=None, accuracy=75, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sleep Powder"] = SleepPowder(pokemon=[]) 

class Sludge(Move):
    def __init__(self, pokemon, name="Sludge", desc="May poison opponent.", move_type="POISON", power=65, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sludge"] = Sludge(pokemon=[]) 

class Smog(Move):
    def __init__(self, pokemon, name="Smog", desc="May poison opponent.", move_type="POISON", power=30, accuracy=70, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Smog"] = Smog(pokemon=[]) 

class Smokescreen(Move):
    def __init__(self, pokemon, name="Smokescreen", desc="Lowers opponent's Accuracy.", move_type="NORMAL", power=None, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Smokescreen"] = Smokescreen(pokemon=[]) 

class SoftBoiled(Move):
    def __init__(self, pokemon, name="Soft-Boiled", desc="User recovers half its max HP.", move_type="NORMAL", power=None, accuracy=None, pp=5):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Soft-Boiled"] = SoftBoiled(pokemon=[]) 

class SolarBeam(Move):
    def __init__(self, pokemon, name="Solar Beam", desc="Charges on first turn, attacks on second.", move_type="GRASS", power=120, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Solar Beam"] = SolarBeam(pokemon=[]) 

class SonicBoom(Move):
    def __init__(self, pokemon, name="Sonic Boom", desc="Always inflicts 20 HP.", move_type="NORMAL", power=None, accuracy=90, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Sonic Boom"] = SonicBoom(pokemon=[]) 

class SpikeCannon(Move):
    def __init__(self, pokemon, name="Spike Cannon", desc="Hits 2-5 times in one turn.", move_type="NORMAL", power=20, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Spike Cannon"] = SpikeCannon(pokemon=[]) 

class Splash(Move):
    def __init__(self, pokemon, name="Splash", desc="Doesn't do ANYTHING.", move_type="NORMAL", power=None, accuracy=None, pp=40):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Splash"] = Splash(pokemon=[]) 

class Spore(Move):
    def __init__(self, pokemon, name="Spore", desc="Puts opponent to sleep.", move_type="GRASS", power=None, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Spore"] = Spore(pokemon=[]) 

class Stomp(Move):
    def __init__(self, pokemon, name="Stomp", desc="May cause flinching.", move_type="NORMAL", power=65, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Stomp"] = Stomp(pokemon=[]) 

class Strength(Move):
    def __init__(self, pokemon, name="Strength", desc="nan", move_type="NORMAL", power=80, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Strength"] = Strength(pokemon=[]) 

class StringShot(Move):
    def __init__(self, pokemon, name="String Shot", desc="Sharply lowers opponent's Speed.", move_type="BUG", power=None, accuracy=95, pp=40):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["String Shot"] = StringShot(pokemon=[]) 

class Struggle(Move):
    def __init__(self, pokemon, name="Struggle", desc="Only usable when all PP are gone. Hurts the user.", move_type="NORMAL", power=50, accuracy=None, pp=None):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Struggle"] = Struggle(pokemon=[]) 

class StunSpore(Move):
    def __init__(self, pokemon, name="Stun Spore", desc="Paralyzes opponent.", move_type="GRASS", power=None, accuracy=75, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Stun Spore"] = StunSpore(pokemon=[]) 

class Submission(Move):
    def __init__(self, pokemon, name="Submission", desc="User receives recoil damage.", move_type="FIGHTING", power=80, accuracy=80, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Submission"] = Submission(pokemon=[]) 

class Substitute(Move):
    def __init__(self, pokemon, name="Substitute", desc="Uses HP to creates a decoy that takes hits.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Substitute"] = Substitute(pokemon=[]) 

class SuperFang(Move):
    def __init__(self, pokemon, name="Super Fang", desc="Always takes off half of the opponent's HP.", move_type="NORMAL", power=None, accuracy=90, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Super Fang"] = SuperFang(pokemon=[]) 

class Supersonic(Move):
    def __init__(self, pokemon, name="Supersonic", desc="Confuses opponent.", move_type="NORMAL", power=None, accuracy=55, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Supersonic"] = Supersonic(pokemon=[]) 

class Surf(Move):
    def __init__(self, pokemon, name="Surf", desc="Hits all adjacent Pok�mon.", move_type="WATER", power=90, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Surf"] = Surf(pokemon=[]) 

class Swift(Move):
    def __init__(self, pokemon, name="Swift", desc="Ignores Accuracy and Evasiveness.", move_type="NORMAL", power=60, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Swift"] = Swift(pokemon=[]) 

class SwordsDance(Move):
    def __init__(self, pokemon, name="Swords Dance", desc="Sharply raises user's Attack.", move_type="NORMAL", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Swords Dance"] = SwordsDance(pokemon=[]) 

class Tackle(Move):
    def __init__(self, pokemon, name="Tackle", desc="nan", move_type="NORMAL", power=40, accuracy=100, pp=35):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Tackle"] = Tackle(pokemon=[]) 

class TailWhip(Move):
    def __init__(self, pokemon, name="Tail Whip", desc="Lowers opponent's Defense.", move_type="NORMAL", power=None, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Tail Whip"] = TailWhip(pokemon=[]) 

class TakeDown(Move):
    def __init__(self, pokemon, name="Take Down", desc="User receives recoil damage.", move_type="NORMAL", power=90, accuracy=85, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Take Down"] = TakeDown(pokemon=[]) 

class Teleport(Move):
    def __init__(self, pokemon, name="Teleport", desc="Allows user to flee wild battles; also warps player to last Pok�Center.", move_type="PSYCHIC", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Teleport"] = Teleport(pokemon=[]) 

class Thrash(Move):
    def __init__(self, pokemon, name="Thrash", desc="User attacks for 2-3 turns but then becomes confused.", move_type="NORMAL", power=120, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thrash"] = Thrash(pokemon=[]) 

class Thunder(Move):
    def __init__(self, pokemon, name="Thunder", desc="May paralyze opponent.", move_type="ELECTRIC", power=110, accuracy=70, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunder"] = Thunder(pokemon=[]) 

class ThunderPunch(Move):
    def __init__(self, pokemon, name="Thunder Punch", desc="May paralyze opponent.", move_type="ELECTRIC", power=75, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunder Punch"] = ThunderPunch(pokemon=[]) 

class ThunderShock(Move):
    def __init__(self, pokemon, name="Thunder Shock", desc="May paralyze opponent.", move_type="ELECTRIC", power=40, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunder Shock"] = ThunderShock(pokemon=[]) 

class ThunderWave(Move):
    def __init__(self, pokemon, name="Thunder Wave", desc="Paralyzes opponent.", move_type="ELECTRIC", power=None, accuracy=90, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunder Wave"] = ThunderWave(pokemon=[]) 

class Thunderbolt(Move):
    def __init__(self, pokemon, name="Thunderbolt", desc="May paralyze opponent.", move_type="ELECTRIC", power=90, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Thunderbolt"] = Thunderbolt(pokemon=[]) 

class Toxic(Move):
    def __init__(self, pokemon, name="Toxic", desc="Badly poisons opponent.", move_type="POISON", power=None, accuracy=90, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Toxic"] = Toxic(pokemon=[]) 

class Transform(Move):
    def __init__(self, pokemon, name="Transform", desc="User takes on the form and attacks of the opponent.", move_type="NORMAL", power=None, accuracy=None, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Transform"] = Transform(pokemon=[]) 

class TriAttack(Move):
    def __init__(self, pokemon, name="Tri Attack", desc="May paralyze, burn or freeze opponent.", move_type="NORMAL", power=80, accuracy=100, pp=10):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Tri Attack"] = TriAttack(pokemon=[]) 

class Twineedle(Move):
    def __init__(self, pokemon, name="Twineedle", desc="Hits twice in one turn. May poison opponent.", move_type="BUG", power=25, accuracy=100, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Twineedle"] = Twineedle(pokemon=[]) 

class VineWhip(Move):
    def __init__(self, pokemon, name="Vine Whip", desc="nan", move_type="GRASS", power=45, accuracy=100, pp=25):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Vine Whip"] = VineWhip(pokemon=[]) 

class ViseGrip(Move):
    def __init__(self, pokemon, name="Vise Grip", desc="nan", move_type="NORMAL", power=55, accuracy=100, pp=30):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Vise Grip"] = ViseGrip(pokemon=[]) 

class WaterGun(Move):
    def __init__(self, pokemon, name="Water Gun", desc="nan", move_type="WATER", power=40, accuracy=100, pp=25):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Water Gun"] = WaterGun(pokemon=[]) 

class Waterfall(Move):
    def __init__(self, pokemon, name="Waterfall", desc="May cause flinching.", move_type="WATER", power=80, accuracy=100, pp=15):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Waterfall"] = Waterfall(pokemon=[]) 

class Whirlwind(Move):
    def __init__(self, pokemon, name="Whirlwind", desc="In battles, the opponent switches. In the wild, the Pok�mon runs.", move_type="NORMAL", power=None, accuracy=None, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Whirlwind"] = Whirlwind(pokemon=[]) 

class WingAttack(Move):
    def __init__(self, pokemon, name="Wing Attack", desc="nan", move_type="FLYING", power=60, accuracy=100, pp=35):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Wing Attack"] = WingAttack(pokemon=[]="Physical") 

class Withdraw(Move):
    def __init__(self, pokemon, name="Withdraw", desc="Raises user's Defense.", move_type="WATER", power=None, accuracy=None, pp=40):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Withdraw"] = Withdraw(pokemon=[]="Status") 

class Wrap(Move):
    def __init__(self, pokemon, name="Wrap", desc="Traps opponent, damaging them for 4-5 turns.", move_type="NORMAL", power=15, accuracy=90, pp=20):
        super().__init__(pokemon, name, desc, move_type, power, accuracy, pp)

    def use(self, actor, target):
        pass

ALL_MOVES["Wrap"] = Wrap(pokemon=[]="Physical") 


