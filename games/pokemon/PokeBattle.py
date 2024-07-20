from support.tools import display_menu
from support.tools import print_message as pm


class Battle:
    def __init__(self, enemy, player_pokemon):
        self.enemy = enemy
        self.player_pokemon = player_pokemon

    def battle(self):
        pm(f"A wild {self.enemy.name} appeared!", 2, 1)
        pm(f"Go! {self.player_pokemon.name}!", 2, 1)
        while self.player_pokemon.stats['hp'] > 0 and self.enemy.stats['hp'] > 0:
            self.player_turn()
            if self.enemy.stats['hp'] <= 0:
                pm(f"{self.enemy.name} fainted!", 2, 1)
                break
            self.enemy_turn()
            if self.player_pokemon.stats['hp'] <= 0:
                pm(f"{self.player_pokemon.name} fainted!", 2, 1)
                break

    def player_turn(self):
        options = ["Fight", "Run"]
        display_menu(options, "What will you do?")
        choice = int(input("Enter your selection: ")) - 1
        if choice == 0:
            self.fight()
        else:
            self.run()

    def fight(self):
        pm(f"{self.player_pokemon.name} used Tackle!", 2, 1)
        self.enemy.stats['hp'] -= 10
        pm(f"{self.enemy.name} took 10 damage!", 2, 1)

    def run(self):
        pm("You ran away!", 2, 1)

    def enemy_turn(self):
        pm(f"{self.enemy.name} used Tackle!", 2, 1)
        self.player_pokemon.stats['hp'] -= 10
        pm(f"{self.player_pokemon.name} took 10 damage!", 2, 1)
