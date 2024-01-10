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


class Engine:
    def __init__(self, actors, input_handler, game_map):
        self.actors = actors
        self.input_handler = input_handler
        self.game_map = game_map

        self.pad = curses.newpad(100, 100)

    def handle_input(self):
        try:
            key = self.pad.getkey()
        except curses.error:
            key = None

        action = self.input_handler.keydown(key)

        if action is not None:
            action.perform(self, self.actors[0])

    def render_actor(self, actor):
        self.pad.addstr(actor.y, actor.x, actor.char)

        self.pad.refresh(0, 0, 0, 0, self.game_map.height, self.game_map.width)

    def render_tile(self, y, x):
        self.pad.addstr(y, x, self.game_map.tiles[y][x]["char"])

        self.pad.refresh(0, 0, 0, 0, self.game_map.height, self.game_map.width)

    def render_refresh(self):
        for i in range(self.game_map.height):
            for j in range(self.game_map.height):
                self.render_tile(i, j)

        for actor in self.actors:
            self.render_actor(actor)
