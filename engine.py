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
from menu import Title, Menu
from input import MovementAction


class Engine:
    def __init__(self, actors, input_handler, game_map, screen):
        self.actors = actors
        self.input_handler = input_handler
        self.game_map = game_map

        self.pad = curses.newpad(100, 100)

        self.term_width = curses.COLS
        self.term_height = curses.LINES

        self.screen = screen

        self.pad.keypad(True)

    def handle_input(self):
        try:
            key = self.pad.getkey()
        except curses.error:
            key = None

        action = self.input_handler.keydown(key)

        if action is not None:
            action.perform(self, self.actors[0])

        if key == "KEY_RESIZE":
            self.resize_term()

    def render_actor(self, actor):
        self.pad.addstr(actor.y, actor.x, actor.char)

        self.pad.refresh(0, 0, 0, 0, self.term_height - 1, self.term_width - 1)

    def render_tile(self, y, x):
        self.pad.addstr(y, x, self.game_map.tiles[y][x]["char"])

        self.pad.refresh(0, 0, 0, 0, self.term_height - 1, self.term_width - 1)

    def render_refresh(self):
        for i in range(self.game_map.height):
            for j in range(self.game_map.height):
                self.render_tile(i, j)

        for actor in self.actors:
            self.render_actor(actor)

    def resize_term(self):
        self.term_height, self.term_width = self.screen.getmaxyx()

        self.pad.refresh(0, 0, 0, 0, self.term_height - 1, self.term_width - 1)

    def menu(self):
        title = Title(self.screen)
        menu = Menu(self.screen)
        selection = 0

        title.Draw()
        menu.Draw()
        menu.Select(selection)

        while True:
            key = self.pad.getkey()

            action = self.input_handler.keydown(key)

            if action is not None:
                if isinstance(action, MovementAction):
                    selection = max(
                        0, min(len(menu.buttons) - 1, action.dy + selection)
                    )

            menu.Select(selection)

            if key == "\n":
                return selection
