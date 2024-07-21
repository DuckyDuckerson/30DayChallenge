import subprocess
import random



#----------------------------------------------


# def displaymenu():
#   print("Main Menu")
#   print("1. Play Hangman!")
#   print("2. Play RPS ")
#   print("3. Play TicTacToe")


# displaymenu()
# user_choice = input("Enter your choice: ")

# if user_choice == "1":
#   subprocess.run(["python", "games/hangman.py"])
# elif user_choice == "2":
#   subprocess.call(["python", "games/rps.py"])
# elif user_choice == "3":
#   subprocess.call(["python", "games/tictactoe.py"])
# else:
#   print ("Please input correct number")
  
attack_power = ()
if health <= 0:
  print("This pokemons fainted")
  
else:
  playertwo_poke -= attackpower





# player_1 attacks player_2
# if hit is sucessful, player_2 loses health
# if not, player_2 attacks player_1
# if hit is sucessful, player_1 loses health
# if not, player_1 attacks player_2
percentage = random.randint(1,50)
#attack_power * (percentage / 100)

# if player_1 health <= 0: ask player to use health item in bag and check for quanitity 
# and depending on item to heal for certain amount of health

attacks  = {
  1: ["Punch", 10],
  2: ["Kick", 20],
  3: ["Ember", 40],
  4: ["Flamethrower", 60],
}
attack_choice = int(input("Enter your attack: "))
hit_chance = random.randint(1,100)
player_1_health = 100
player_2_health = 100

if hit_chance > 50:
 print(attack_choice - player_2_health) 
else:
  print("you missed")


class Battle:
  def __init__(self, player, enemy):
    # here the enemy is an instance of the pokemon class
    self.enemy = enemy
    self.player = player
    self.turn = random.choice(["player", "enemy"])

  def player_turn(self):
    pass
    #prmpt player for action choice, give options like use move, use item, attempt to catch (disabled in trainer battles) and attempt to flee
   #probably have a method for each action type, to keep the code a bit organized 

  def enemy_turn(self):
    move = random.choice(self.enemy.moves)
    dmg = self.attack(move, self.player)
    print(f"Enemy uses {move.name} for {dmg} damage")
    self.turn = "player"

  def attack(self, move, attacked_pokemon):
    pass
    #calculate damage bases on attacked_pokemon type and enemy move type and also stats
    #maybe return the damage done based on stats

  def battle(self):
    pass
    #while the player team has pokemon with health in it and the enemy is still alive, continue the battle
    #end it when all the players pokemon have fainted or the enemy if caught or has fainted

class TrainerBattle:
  def __init__(self, player, enemy):
    self.player = player
    self.enemy = enemy
    #in the TrainerBattle class the enemy is an instance of the #Trainer class

  def battle_trainer(self, player):
    chosen_pokemon = random.choice(self.enemy.pokemon_team)
    battle = Battle(player, chosen_pokemon)
    while chosen_pokemon.stats.stats["hp"] > 0:
      battle.battle()
    #this isnt the best way to do this, because we also need to check for the players team and have the ability to swap out pokemon when desired
    #and then have the trainer swap out their pokemon when it faints
    # but prolly best to worry about that when we get there. for now we can just perfect the battle itself, like against a single wild pokemon.