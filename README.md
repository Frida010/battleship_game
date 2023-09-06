# Battleship Game

Welcome to the battleship game! this is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

The user will be able to try to beat the computer by finding the computer's three battleships. The user has ten attempts or as called in the game, ammo. 

The user is rewarded with an extra ammo for each correct hit by the computer's battleship. Each battleship occupies one square on the board. 

![Screenshot of the game on diffrent screen sizes](https://user-images.githubusercontent.com/129947589/265952135-0745c6be-a67e-4e76-ad29-151b1eedcf0f.png)

## How to play
The battleship game is based on a classic strategy pen-and-paper game which dates back from World War I. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

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

## Data model

## Testing
I have manually tested this project by doing the following:

- Passed the code through a PEP8 linter

- Given invalid inputs: strings when numbers are recuired, out of bounds inputs and same inputs twice.

- Tested in my local terminal and the Code Institute Heroku terminal. 
### Bugs

#### Solved bugs

- When working on this project I got some problem with the comments in the code. 

### Remaining Bugs

### Validator Testing

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

