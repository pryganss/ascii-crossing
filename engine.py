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

        #### HACK REMOVE THIS TERRIBLE IDEA ####
        self.screen.addstr(self.actors[0].y, self.actors[0].x, self.actors[0].char)

        self.screen.refresh()
