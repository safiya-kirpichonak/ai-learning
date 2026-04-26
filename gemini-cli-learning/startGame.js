"use strict";

function startGame() {
    const WIDTH = 20;
    const HEIGHT = 15;
    const TICK_RATE = 200;

    const getDirection = handleInput();
    let state = createInitialState(WIDTH, HEIGHT);
    
    // Initial render
    renderState(drawBoard(state));

    const intervalId = setInterval(function tick() {
        state = runTick(state, getDirection(), intervalId);
    }, TICK_RATE);
};
