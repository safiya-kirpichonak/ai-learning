# Gemini CLI Learning Project

## Directory Overview
This is the little project for investigating Gemini CLI abilities. Here we will create snake with JavaScript and HTML.

## Key Files
- index.html: Entry point, contains the ASCII game board container.
- index.js: Main script that kicks off the game.
- startGame.js: Initializes game state and starts the intervals.
- createInitialState.js: Returns the initial game state object.
- updateState.js: Pure function that calculates the next game state.
- moveSnake.js: Pure function to update snake coordinates.
- checkCollisions.js: Pure function to detect wall and self collisions.
- generateFood.js: Pure function to spawn food at random coordinates.
- drawBoard.js: Pure function that renders the game state to an ASCII string.
- renderState.js: Function that updates the DOM with the board string.
- handleInput.js: Manages keyboard event listeners for direction changes.
- runTick.js: Orchestrates the state update and rendering for each tick.

## Usage
Open index.html in any modern web browser to play the ASCII Snake game. Use the Arrow Keys to control the snake.

## Additional Coding Preferences
1. Write "use strict;" in the each JavaScript file.
2. Use ", not ' in the JavaScript files.
3. Always use ";" in the JavaScript files.
4. New function - new JavaScript file.
5. Only functional programming.