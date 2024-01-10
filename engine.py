#!/usr/bin/env python3

import curses
from actions import MovementAction, QuitAction


class Engine:
    def __init__(self, actors, input_handler, screen):
        self.actors = actors
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
            self.actors[0].move(action.dy, action.dx)

            self.render()

        elif isinstance(action, QuitAction):
            raise SystemExit()

    def render(self):
        self.screen.clear()

        for actor in self.actors:
            self.screen.addstr(actor.y, actor.x, actor.char)

        self.screen.refresh()
