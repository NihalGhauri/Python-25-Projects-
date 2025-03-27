
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Use a single list to represent a 3x3 board
        self.current_winner = None  # Fixed variable name

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' ')

    @staticmethod
    def print_board_nums():
        # Tells us what number corresponds to what box; i.e. a mapping.
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Return list of available spots (checks for a space, not an empty string)
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_square(self):
        # Return True if there is at least one empty square
        return ' ' in self.board

    def num_empty_squares(self):
        # Count how many empty squares are left
        return self.board.count(' ')

    def make_move(self, square, letter):
        # If valid move, assign the square to the letter and check for a winner
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row of the move
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check the column of the move
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals only if the move is on a diagonal (even-numbered square)
        if square % 2 == 0:
            # Left-to-right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            # Right-to-left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    # Show the initial board
    if print_game:
        print("Initial Board:")
    game.print_board_nums()  # Show numbers 0-8 to guide the players
    print()


    letter = 'X'  # Starting letter

    # Main game loop
    while game.empty_square():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Make the move and print the board if the move is valid
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # Empty line for better readability

            # Check if we have a winner
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # Switch players
            letter = 'O' if letter == 'X' else 'X'
        else:
            # If move is invalid, you can print a message or handle it appropriately.
            print("Invalid move. Try again.")

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
