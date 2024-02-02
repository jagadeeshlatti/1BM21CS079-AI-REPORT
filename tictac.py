import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Representing board as a list

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        self.board[square] = letter

    def check_winner(self, symbol):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == symbol:
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == symbol:
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] == symbol or \
           self.board[2] == self.board[4] == self.board[6] == symbol:
            return True
        return False

def minimax(board, depth, maximizing_player):
    if board.check_winner('X'):
        return -10 + depth, None
    elif board.check_winner('O'):
        return 10 - depth, None
    elif not board.empty_squares():
        return 0, None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval, _ = minimax(board, depth + 1, False)
            board.make_move(move, ' ')
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval, _ = minimax(board, depth + 1, True)
            board.make_move(move, ' ')
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

def play_game():
    board = TicTacToe()
    board.print_board()

    while board.empty_squares():
        if board.num_empty_squares() % 2 == 1:  # AI's turn
            _, move = minimax(board, 0, True)
            board.make_move(move, 'O')
            print("AI's move:")
        else:  # Human's turn
            while True:
                try:
                    move = int(input("Enter your move (0-8): "))
                    if move in board.available_moves():
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Enter a number.")
            board.make_move(move, 'X')
            print("Your move:")
        board.print_board()

        if board.check_winner('O'):
            print("AI wins!")
            break
        elif board.check_winner('X'):
            print("You win!")
            break
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
