#!/usr/bin/env python3
from config import INPUT
from actions import MovementAction, QuitAction


class InputHandler:
    def keydown(self, key):
        action = None

        if key in INPUT.DOWN:
            action = MovementAction(1, 0)
        elif key in INPUT.UP:
            action = MovementAction(-1, 0)
        elif key in INPUT.RIGHT:
            action = MovementAction(0, 1)
        elif key in INPUT.LEFT:
            action = MovementAction(0, -1)

        elif key == "q":
            action = QuitAction()

        return action
