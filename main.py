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
from curses import wrapper
from engine import Engine
from input import InputHandler
from actors import Player
from map import GameMap


def main(screen):
    curses.curs_set(0)
    screen.nodelay(True)

    actors = [Player(10, 10, "@")]

    engine = Engine(actors, InputHandler(), GameMap(30, 30))

    engine.render_refresh()

    while True:
        engine.handle_input()


if __name__ == "__main__":
    wrapper(main)
