"use strict";

function runTick(state, direction, intervalId) {
    const nextState = updateState(state, direction);
    renderState(drawBoard(nextState));
    
    if (nextState.isGameOver) {
        clearInterval(intervalId);
    }
    
    return nextState;
};
