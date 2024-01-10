#!/usr/bin/env python3


class Action:
    pass


class QuitAction(Action):
    pass


class MovementAction(Action):
    def __init__(self, dy, dx):
        super().__init__()

        self.dy = dy
        self.dx = dx
