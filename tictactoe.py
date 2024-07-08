#ASCII for x's and o's
#player vs player
#player input (numbering out the grid)
#check if player won/loss
from support import print_message as pm
from test import board

class TicTacToe:
    def __init__(self):
        self.name = "TicTacToe"
        self.playing = False
        self.turn = None
        self.turn_num = 0
        self.setup = False
        self.player_one = Player("X")
        self.player_two = Player("O")
        self.win_conditions = [
             (21, 27, 33), (75, 81, 87), (129, 135, 141), #rows
             (21, 75, 129), (27, 81, 135), (33, 87, 141), #columns
             (21, 81, 141), (33, 81, 129) #diagonals
        ]
        self.board = """
             |     |     
          1  |  2  |  3  
        _____|_____|_____
             |     |     
          4  |  5  |  6  
        _____|_____|_____
             |     |     
          7  |  8  |  9  
             |     |  
        """

    
    def check_for_win(self):
        for condition in self.win_conditions:
             if self.board[condition[0]] == self.board[condition[1]] and self.board[condition[0]] == self.board[condition[2]]:
                self.game_over(self.board[condition[0]])
                 

    def game_over(self, go_type):
        if go_type == "Draw":
            pm("Game Over - It's A Draw!", 2, 1)
        else:
            if self.player_one.char == go_type:
                self.player_one.score += 1
                pm("Player One Wins!", 2, 1)
            else:
                self.player_two.score += 1
                pm("Player Two Wins!", 2, 1)
            
        again = input("Do you want to play again? y/N")
        if again == "y":
            self.board = """
                 |     |     
              1  |  2  |  3  
            _____|_____|_____
                 |     |     
              4  |  5  |  6  
            _____|_____|_____
                 |     |     
              7  |  8  |  9  
                 |     |  
            """
            self.turn = self.player_one
            self.turn_num = 0
            self.game_loop()
        else:
            self.playing = False

    
    def game_setup(self):
        player1 = input("X or O?\n~: ").upper()  
        if player1 == "X":
            self.player_one = Player("X")
            self.player_two = Player("O")
        else:
            self.player_one = Player("O")
            self.player_two = Player("X")
        self.turn = self.player_one
        self.setup = True

    
    def game_loop(self):
        if not self.setup:
            self.game_setup()
        
        while self.playing:
            pm(self.board, 5, 1)
            while self.turn == self.player_one:
                player1_input = input('P1: Choose a square\n~: ')
                if player1_input in self.board:
                    board_list = list(self.board)
                    board_list[self.board.index(player1_input)] = self.player_one.char
                    self.board = "".join(board_list)
                    print(self.board)
                    self.turn = self.player_two
                else:
                    player1_input = input('P1: Choose a square\n~: ')

    
            while self.turn == self.player_two:
                player2_input = input('P2: Choose a square\n~: ')
                if player2_input in self.board:
                    board_list = list(self.board)
                    board_list[self.board.index(player2_input)] = self.player_two.char
                    self.board = "".join(board_list)
                    self.turn = self.player_one
                else:
                    player2_input = input('P2: Choose a square\n~: ')

                    continue
            self.check_for_win()
            self.turn_num += 1
            if self.turn_num == 9:
                self.game_over("Draw")




class Player:
    def __init__(self, char):
        self.char = char
        self.score = 0