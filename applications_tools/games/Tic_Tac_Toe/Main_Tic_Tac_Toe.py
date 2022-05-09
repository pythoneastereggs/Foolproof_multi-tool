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

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # Ελέγχει σειρές
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # Ελέγχει στήλες
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # Ελέγχει διαγώνιες
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # Λαμβάνει είσοδο χρήστη
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            self.fix_spot(row - 1, col - 1, player)

            # Ελέγχει αν ο παίκτης κέρδισε
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # Ελέγχει αν το παιχνίδι είναι ισοπαλία
            if self.is_board_filled():
                print("Match Draw!")
                break

            # Αλλάζει την σειρά
            player = self.swap_player_turn(player)

        # Δείχνει τον πίνακα
        print()
        self.show_board()


# Ξεκινά το παιχνίδι
tic_tac_toe = TicTacToe()
tic_tac_toe.start()