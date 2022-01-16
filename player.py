import math
import random

# base player class
class Player:
    def __init__(self, letter):
    # Letter is X or O
        self.letter = letter

    # getting next moves in given game
    def get_move(self, game):
        pass

    # computer player
class RandomCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_move())
        return square

    # human player
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input Move (0-8):')
            # checking correct value byu casting to an interger 
            # if it does not work i will say invalid, if the spot
            # is not available it will also say invalid 
            try:
                val = int(square)
                if val not in game.available_move():
                    raise ValueError
                valid_square = True # Successful
            except ValueError:
                print('Invalid Square')

        return val