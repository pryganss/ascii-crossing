#!/usr/bin/env python3

# ASCII Crossing is a free open source cozy farming simulator type game
# Copyright (C) 2024

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
