"use strict";

function renderState(boardString) {
    const boardElement = document.getElementById("game-board");
    if (boardElement) {
        boardElement.textContent = boardString;
    }
};
