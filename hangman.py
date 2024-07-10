import random
from hangman_art import stages
from tools import print_message as pm
from getpass import getpass as gp
# TODO: handle repeated guesses
# ensure guess is one letter
# add 'solve' option - either by entering "solve" or just by typing out the whole word?


class Hangman:

    def __init__(self):
        self.name = "Hangman"
        self.lives = 6
        self.playing = False

    def game_over(self):
        pm("Game Complete", 2, 1)
        again = input("Would you like to play again?, y/n")
        if again.lower() == 'y':
            self.lives = 6
            self.game_loop()
        else:
            self.playing = False

    def game_loop(self):
        pm(self.name, 3, 1)
        secret_word = gp("Enter word: ")

        duplicates = {}
        for i in range(len(secret_word)):
            for letter in secret_word:
                if secret_word[i] == letter:
                    if duplicates.get(letter):
                        duplicates[letter].append(i)
                    else:
                        duplicates[letter] = [i]

        guessed_letters = []
        token = []

        for letter in secret_word:  #type: ignore
            token.append("_")

        pm(token, 1, 1)

        while self.playing:

            if self.lives == 0:
                pm("Game Over", 1, 1)
                pm(f"The correct word is {secret_word}", 1, 1)
                self.game_over()

            else:
                user_guess = input("Guess a letter:")

                if user_guess in secret_word:
                    for char in secret_word:
                        if user_guess == char:
                            if user_guess in duplicates:
                                for index in duplicates[user_guess]:
                                    token[index] = user_guess
                            else:
                                token[secret_word.index(char)] = user_guess
                else:
                    self.lives -= 1

                pm(stages[self.lives], 3, 1)
                guessed_letters.append(user_guess)
                pm(
                    f"You have guessed the following letters:\n{guessed_letters}",
                    3, 1)

                pm(token, 2, 1)
                tokenstr = "".join(token)
                if tokenstr == secret_word:
                    pm('You win!', 1, 1)
                    self.game_over()

