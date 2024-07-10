from .hangman import Hangman
from .rps import RPS
from .tictactoe import TicTacToe

# __all__ tells the package (games dir) what to make accessible when games is imported in main.py
__all__ = ['Hangman', 'RPS', 'TicTacToe']