# Battleship Game

Welcome to Battleship Game, a simple and entertaining implementation of the classic game "Battleship" which runs in the Code Institute mock terminal on Heroku. In this game, your task is to discover and destroy hidden ships on a 5x5 board using your shots and strategy.

**Features:**
- Interactive game board
- Ammunition handling
- Hidden ships
- Win and loss notifications
- Clear game instructions
- Simple and readable source code

Play the game, challenge your skill and see if you can destroy all the ships before your ammo runs out!

![Screenshot of the game on diffrent screen sizes](https://user-images.githubusercontent.com/129947589/265952135-0745c6be-a67e-4e76-ad29-151b1eedcf0f.png)

## How to play
The battleship game is based on a classic strategy pen-and-paper game which dates back from World War I. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

### Instructions:
1. You have a 5x5 game board where you need to locate and sink three hidden ships.
2. You start with 10 ammo.
3. To make a shot, enter the row and column numbers where you want to fire.
   - For example, to target the first row and first column, you would enter `1` for both row and column.
4. The game will inform you if your shot hit a ship, missed, or if you have already fired at a location.
5. Your ammo count will decrease with each shot.
6. Keep playing until you destroy all the ships or run out of ammo.

![Screenshot of the game](https://user-images.githubusercontent.com/129947589/265952183-071dea35-0f6c-4d63-9c28-5daca52ea4e3.png)

### Gameplay

The game will display the game board, and you will enter row and column numbers for your shots. The game board legend is as follows:

- `O` represents an empty cell.
- `X` represents a hit on a ship.
- `-` represents a missed shot.

### Winning

To win the game, you must sink all three hidden ships before running out of ammo. If you succeed, you will be prompted to play again.

Enjoy the Battleship game!

## Features

This Battleship implementation has the following features:

1. **Game board:** An interactive 5x5 board where you can see and shoot ships.

2. **Ammo:** You start with 10 shots, and each hit rewards you with an extra shot.

3. **Ships:** The game has 3 hidden ships that are randomly placed on the board on every restart.

4. **Win and Loss Notifications:** You will be notified if you win or lose the game, and you have the option to play again if you want.

5. **Game Instructions:** Clear instructions are given at the beginning of the game to help the player understand the rules.

6. **Error Handling:** Incorrect input and invalid moves are handled to provide a user-friendly experience.

7. **Simple and clear source code:** The source code is structured and commented for easy understanding and possible adaptation.

8. **Interactivity:** The game is played in the terminal and has a simple interactive user interface.

## Data model

This section describes how data and game logic are organized and represented in the code for this Battleship game.

### Data structures

- **Game board:** The game board is represented as a 2D list, where each cell can be either empty ("O"), hit ("X") or missed ("-").

- **Ship positions:** The positions of the hidden ships are represented as a list of tuples, where each tuple contains the coordinates (row and column) of a ship on the board.

- **Variables and Constants:** The code uses constants like `EMPTY`, `HIT`, `MISS` to represent cell states on the board and other constants like `BOARD_SIZE`, `NUM_SHIPS`, and `MAX_AMMO` to control the game .

### Game logic

- The game uses a main loop (`main()`) that handles the entire game logic.

- For each round, the player is allowed to shoot on a cell by entering row and column numbers. The game checks if the shot hit a ship, missed, or had already been fired.

- Hits reward the player with extra ammo and keep count of the number of hits to determine when all ships have been destroyed.

- The game continues until either all ships have been destroyed or the player runs out of ammo.

### Data management

- To manage the game board and track hits and misses, the code uses 2D lists.

- The game logic is enclosed in a main function (`main()`) with several inner functions to keep the code structured and easy to read.

## Testing
I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter

- Given invalid inputs: strings when numbers are recuired, out of bounds inputs and same inputs twice.

- Tested in my local terminal and the Code Institute Heroku terminal. 
### Bugs

#### Solved bugs

- When working on this project I got some problem with the comments in the code and had to reduce them to make the code work as planed. 

### Remaining Bugs

- No remaining bugs. 

### Validator Testing

- No errors were returned after final testing. 

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
1. Fork or clone this reposity
2. Create a new Heroku app
3. Set the buildbacks to `Python` and `NodeJS` in that order
4. Link the Heroku app to the reposity
5. Click on `Deploy`

## Credits

- Code Insitutes course material to help whit deployment. 
- Wikipedia for the details of the Battleship game. 
- W3school to help whit some of the pyhon code functions etc. 
- Youtube

