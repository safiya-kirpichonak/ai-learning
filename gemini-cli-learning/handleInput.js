"use strict";

function handleInput() {
    let currentDirection = { x: 1, y: 0 };
    
    window.addEventListener("keydown", (event) => {
        const key = event.key;
        
        if ((key === "ArrowUp" || key === "Up") && currentDirection.y === 0) {
            currentDirection = { x: 0, y: -1 };
            event.preventDefault();
        } else if ((key === "ArrowDown" || key === "Down") && currentDirection.y === 0) {
            currentDirection = { x: 0, y: 1 };
            event.preventDefault();
        } else if ((key === "ArrowLeft" || key === "Left") && currentDirection.x === 0) {
            currentDirection = { x: -1, y: 0 };
            event.preventDefault();
        } else if ((key === "ArrowRight" || key === "Right") && currentDirection.x === 0) {
            currentDirection = { x: 1, y: 0 };
            event.preventDefault();
        }
    });
    
    return () => {
        return currentDirection;
    };
};
