#!/usr/bin/env python3


class Actor:
    x = y = None


class Player(Actor):
    def __init__(self, y, x):
        self.y = y
        self.x = x
