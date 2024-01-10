#!/usr/bin/env python3

import curses
from actions import MovementAction, QuitAction


class Engine:
    def __init__(self, player, input_handler, screen):
        self.player = player
        self.input_handler = input_handler

        self.screen = screen

    def handle_input(self):
        try:
            key = self.screen.getkey()
        except curses.error:
            key = None

        action = self.input_handler.keydown(key)

        if action is None:
            pass

        elif isinstance(action, MovementAction):
            self.player.y += action.dy
            self.player.x += action.dx

            self.render()

        elif isinstance(action, QuitAction):
            raise SystemExit()

    def render(self):
        self.screen.clear()

        self.screen.addstr(self.player.y, self.player.x, "@")

        self.screen.refresh()
