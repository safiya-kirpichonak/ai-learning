"use strict";

function checkCollisions(snake, width, height) {
    const head = snake[0];
    
    const hitWall = head.x < 0 || head.x >= width || head.y < 0 || head.y >= height;
    
    const hitSelf = snake.slice(1).some((segment) => {
        return segment.x === head.x && segment.y === head.y;
    });

    return hitWall || hitSelf;
};
