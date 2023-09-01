"""
Import random package to be able to create random integers. 
"""
import random


"""
Constants for the battleship game
"""
EMPTY = "O"
HIT = "X"
MISS = "-"
BOARD_SIZE = 5
NUM_SHIPS = 3
MAX_AMMO = 10


"""
Prints out the battleship gameboard. 
"""
def print_board(board):
    for row in board:
        print(*row)

def create_ship():
    return random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)

def main():
    # Display welcome message to the player
    print("""Welcome to the battleship game!\nYour task is to find and destroy all the ships on the map.""")

    # Provide game instructions
    print("""\nInstructions:\n\nYou have 10 ammo and there are 3 hidden ships on the map.
    In order to hit them, you have to enter the numbers for that location.
    For example:\nThe first row and first column, you write 1 and 1\nGood luck!\n""")

    """
    Initialize the game board whit empty cells
    """
    def initialize_game():
        return [[EMPTY]*BOARD_SIZE for _ in range (BOARD_SIZE)], [create_ship() for _ in range(NUM_SHIPS)], MAX_AMMO

    """
    Check if the provided "number" is within the valid input range, which is between 1 and BOARD_SIZE (inclusive).
    Returns True if "number" is valid, otherwise returns False.
    """
    def valid_input(number):
        return 1 <= number <= BOARD_SIZE
