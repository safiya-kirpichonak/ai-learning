"use strict";

function createInitialState(width, height) {
    return {
        snake: [
            { x: 10, y: 10 },
            { x: 9, y: 10 },
            { x: 8, y: 10 }
        ],
        food: { x: 5, y: 5 },
        direction: { x: 1, y: 0 },
        isGameOver: false,
        score: 0,
        width: width,
        height: height
    };
};
