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
Prints out the 2D grid battleship gameboard.
"""
def print_board(board):
    for row in board:
        print(*row)

"""
Create random coordinates for placing the ships on the game board.
"""
def create_ship():
    return random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)

"""
Prompt the player to enter their choice: Y=yes or N=no.
"""
def play_again():
    """
    Converts the users input to lowercase for case-insensitivity and
    checks if lowercase input is equal to y to determine the users choise.
    """
    try_again = input("Want to play again? <Y>es or <N>o ->\n")
    return try_again.lower() == "y"

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

    """
    Initialize the game state by calling the 'initialize_game()' function.
    This function sets up the game board, places ships, and defines the maximum ammo.
    """
    game_board, ships, ammo = initialize_game()

    """
    Prints game board as long as ammo is grater then 0
    """
    while ammo > 0:
        print_board(game_board)

        """
        Prompt the user to enter row and column numbers for their next move.
        Prints error message if user write other then numbers.
        """
        try:
            row = int(input("Enter a row number between 1 and 5 ->\n"))
            column = int(input("Enter a column number between 1 and 5 ->\n"))
        except ValueError:
            print("Only enter numbers!")
            continue

        """
        Checks if the users input for row and column is within the valid range, 1 and 5.
        If either row or column is outside valid range, print error message. 
        """
        if not valid_input(row) or not valid_input(column):
            print("\nThe number must be between 1 and 5!")
            continue

        """
        Adjusts the users input from 1-based indexing to 0-based indexing for row and column.
        """
        row -= 1
        column -= 1

        """
        Checks if the user has already shot at the specified location on the game board.
        If the location has already been targeted (contains 'MISS' or 'HIT'), inform the player.
        """
        if game_board[row][column] in (MISS, HIT):
            print("\nYou have alredy fire that place!\n")
            continue

        """
        Initialize a boolean variable hit_ship to track whether the users shot hits a ship.
        Iterate through each ship's position in the ships list.
        Check if the users shot matches the position of a ship.
        If a match is found, set hit_ship to True and exit the loop.
        """
        hit_ship = False
        for ship_row, ship_column in ships:
            if (row, column) == (ship_row, ship_column):
                hit_ship = True
                break

        """
        Checks if the users shot hit a ship, if successful hit the user gets a message and rewared a new ammo. 
        Update the game board to mark the hit cell with the 'HIT' constant and decrement the count of remaining ships as one ship has been hit.
        """
        if hit_ship:
            print("\nBOOM! You hit a ship! You were rewared a new ammo!\n")
            game_board[row][column] = HIT
            NUM_SHIPS -= 1

            """
            Checks if all ships have been destroyed, if thats the case congratulate the user.
            Check if usedr wants to play again, if not print Goodbye.
            If user choose to play again, reset game state.
            """
            if NUM_SHIPS == 0:
                print("Congratulations! You won!")
                if not play_again():
                    print("Goodbye!")
                    break
                else:
                    game_board, ships, ammo = initialize_game()

            """
            Inform the user that they missed their shot.
            Update the game board to mark the missed shot with the 'MISS' constant.
            Decrease users remaining ammunition by 1.
            """
            else:
                print("\nYou missed!\n")
                game_board[row][column] = MISS
                ammo -= 1

            """
            Display the current state of the users resources, remaining ammo and remaining ships.
            """
            print(f"Ammo left: {ammo} | Ships left: {NUM_SHIPS}")

        """
        Checks if the user has run out of ammo, if ammo is out = game over. 
        """
        if ammo <= 0:
            print("You're out of ammo! Game over.")
            """
            Check if the user wants to play again.
            If the user chooses to play again, start a new game by calling the 'main()' function.
            If the user chooses not to play again, print "Goodbye!" and exit.
            """
            if play_again():
                main()
            else:
                print("Goodbye!")

"""
Check if this script is being run as the main program.
If the script is being run directly, execute the 'main()' function to start the game.
"""
if __name__ == "__main__" :
    main()
