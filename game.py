from player import HumanPlayer, RandomCompPlayer


class TicTacToe:
    def __init__(self):
        # single liost to represent a 3x3 board
        self.board =(' ' for _ in range(9))
        # tracks winner
        self.new_winner = None 

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_num():
        # 0 | 1 | 2  numbers represent each box to make move in
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_move(self):
        move = []
        for(i, spot) in enumerate(self.board):
            if spot == ' ':
                move.append(i)
        return move

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # if valid move assign letter to square, if not return false
       # if self.board[square] == ' ':
        #    self.board[square] = letter
         #   if self.winner(square, letter):
          #      self.new_winner = letter
           # return True
        #return False 

    def winner(self, square, letter):
        # wins with 3 in a row anywhere on board
        # checking rows for win condition
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # checking column for win condition
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # checking diagonal for win condition. 
        # move must be on even number for diagonal win condition
        if square % 2 == 0:
            diagonalA = [self.board[i] for i in [0, 4, 8]] # left to right
            if all([spot == letter for spot in diagonalA]):
                return True
            diagonalB =[self.board[i] for i in [2, 4, 6]] # right to left
            if all([spot == letter for spot in diagonalB]):
                return True
        # if conditions not met
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_num()

    letter = 'X' # letter that goes first

    while game.empty_squares():
        # taking move from correct player
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        # function for making a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' Move Complete')
                game.print_board()
                print('')

            if game.new_winner:
                if print_game:
                    print(letter + ' won')
                return letter

            # alternating between players
            if letter == 'X':
                letter = "O"
            else:
                letter = 'X'

            #if print_game:
             #   print('Tie')

# game state
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomCompPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
            

        
