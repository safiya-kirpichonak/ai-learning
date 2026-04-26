"use strict";

function generateFood(snake, width, height) {
    const x = Math.floor(Math.random() * width);
    const y = Math.floor(Math.random() * height);
    
    const isOnSnake = snake.some((segment) => {
        return segment.x === x && segment.y === y;
    });

    if (isOnSnake) {
        return generateFood(snake, width, height);
    }

    return { x: x, y: y };
};
