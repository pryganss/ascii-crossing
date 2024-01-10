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
    def __init__(self, actors, input_handler, screen, game_map):
        self.actors = actors
        self.input_handler = input_handler
        self.game_map = game_map

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
            self.render_tile(self.actors[0].y, self.actors[0].x)

            self.actors[0].move(action.dy, action.dx)

            self.render_actor(self.actors[0])

        elif isinstance(action, QuitAction):
            raise SystemExit()

    def render_actor(self, actor):
        self.screen.addstr(actor.y, actor.x, actor.char)

        self.screen.refresh()

    def render_tile(self, y, x):
        self.screen.addstr(y, x, self.game_map.tiles[y][x]["char"])

        self.screen.refresh()

    def render_refresh(self):
        for i in range(self.game_map.height):
            for j in range(self.game_map.height):
                self.render_tile(i, j)

        for actor in self.actors:
            self.render_actor(actor)
