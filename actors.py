#!/usr/bin/env python3


class Actor:
    def __init__(self, y, x, char):
        self.y = y
        self.x = x
        self.char = char

    def move(self, dy, dx):
        self.y += dy
        self.x += dx


class Player(Actor):
    pass
