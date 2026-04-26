"use strict";

function updateState(state, newDirection) {
    if (state.isGameOver) {
        return state;
    }

    const head = state.snake[0];
    const nextHead = {
        x: head.x + newDirection.x,
        y: head.y + newDirection.y
    };

    const hasEaten = nextHead.x === state.food.x && nextHead.y === state.food.y;
    const newSnake = moveSnake(state.snake, newDirection, hasEaten);
    
    if (checkCollisions(newSnake, state.width, state.height)) {
        return {
            ...state,
            isGameOver: true
        };
    }

    return {
        ...state,
        snake: newSnake,
        food: hasEaten ? generateFood(newSnake, state.width, state.height) : state.food,
        direction: newDirection,
        score: hasEaten ? state.score + 1 : state.score
    };
};
