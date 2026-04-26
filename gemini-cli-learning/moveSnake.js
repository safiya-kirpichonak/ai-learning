"use strict";

function moveSnake(snake, direction, hasEaten) {
    const head = snake[0];
    const newHead = {
        x: head.x + direction.x,
        y: head.y + direction.y
    };
    
    if (hasEaten) {
        return [newHead, ...snake];
    }
    
    return [newHead, ...snake.slice(0, -1)];
};
