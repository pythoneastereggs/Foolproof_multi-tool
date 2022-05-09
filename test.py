import random

class TicTacToe:
    
    def __init__(self):
        self.board = []
    
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)