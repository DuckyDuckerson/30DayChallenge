from rps import RPS  # type: ignore
from hangman import Hangman  # type: ignore
from tictactoe import TicTacToe  # type: ignore
from support import print_message as pm


rps = RPS()
hangman = Hangman()
tictactoe = TicTacToe()
games = [rps, hangman, tictactoe]


def main():
    pm("Welcome to the Games console! What game would you like to play?", 2, 1)

    i = 1

    for game in games:
        print(f"{i}. {game.name}")
        i += 1
    game_choice = input("Input the game number for your chosen game. ")

    chosen_game = games[int(game_choice) - 1]
    chosen_game.playing = True

    while chosen_game.playing:
        chosen_game.game_loop()
    main()


if __name__ == "__main__":
    main()
