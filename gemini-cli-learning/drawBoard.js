"use strict";

function drawBoard(state) {
    let board = "";
    
    for (let y = 0; y < state.height; y = y + 1) {
        for (let x = 0; x < state.width; x = x + 1) {
            const isFood = state.food.x === x && state.food.y === y;
            const isSnake = state.snake.some((segment) => {
                return segment.x === x && segment.y === y;
            });
            
            if (isSnake) {
                board = board + "O";
            } else if (isFood) {
                board = board + "X";
            } else {
                board = board + ".";
            }
        }
        board = board + "\n";
    }
    
    return board + "\nScore: " + state.score + (state.isGameOver ? " - GAME OVER!" : "");
};
