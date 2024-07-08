import random  # type: ignore
from tools import print_message as pm  # type: ignore


class RPS:
    def __init__(self):
        self.name = "Rock, Paper, Scissors"
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0
        self.playing = False
        self.computer_choice = None
        self.user_choice = None

    def computer_wins(self):
        message = f"Computer chose {self.computer_choice}\n{self.computer_choice} beats {self.user_choice}\nComputer wins!"
        pm(message, 2, 1)

    def player_wins(self):
        message = f"Computer chose {self.computer_choice}\n{self.user_choice} beats {self.computer_choice}\nPlayer wins!"
        pm(message, 2, 1)

    def game_loop(self):
        pm(self.name, 3, 1)
        pm("Hello! Welcome the game!", 2, 1)
        pm("Your choices are: rock, paper, scissors", 2, 1)
        while self.playing:
            self.computer_choice = random.choice(self.choices)
            self.user_choice = input("Enter your choice: ").lower()

            if self.user_choice in self.choices:
                if self.user_choice == self.computer_choice:
                    pm("its a tie", 2, 1)
                elif self.user_choice == 'rock' and self.computer_choice == 'scissors'\
                or self.user_choice == 'paper' and self.computer_choice == 'rock' \
                or self.user_choice == 'scissors' and self.computer_choice == 'paper':
                    self.player_wins()
                    self.user_score += 1
                else:
                    self.computer_wins()
                    self.computer_score += 1
            if self.user_choice == "quit".lower():
                pm(f"Thanks for playing! The final score is\nComputer: {self.computer_score}\nPlayer: {self.user_score}", 2, 1)
                if self.user_score > self.computer_score:
                    pm("You win!", 2, 1)
                else:
                    pm("Computer Wins!", 2, 1)
                    pm("Get gud", 2, 1)
                self.playing = False
