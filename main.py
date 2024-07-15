from games import Hangman, RPS, TicTacToe, PokemonGame
from support.tools import print_message as pm


rps = RPS()
hangman = Hangman()
tictactoe = TicTacToe()
pokemon = PokemonGame()
game_options = [rps, hangman, tictactoe, pokemon]


def main():

    pm("Welcome to the Games console! What game would you like to play?", 2, 1)

    i = 1

    for game in game_options:
        print(f"{i}. {game.name}")
        i += 1
    game_choice = input("Input the game number for your chosen game. ")

    chosen_game = game_options[int(game_choice) - 1]
    chosen_game.playing = True

    while chosen_game.playing:
        chosen_game.game_loop()
    main()


if __name__ == "__main__":
    main()
