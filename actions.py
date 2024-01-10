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


class Action:
    def perform(self, engine, actor):
        raise NotImplementedError()


class QuitAction(Action):
    def perform(self, engine, actor):
        raise SystemExit()


class MovementAction(Action):
    def __init__(self, dy, dx):
        self.dy = dy
        self.dx = dx

    def perform(self, engine, actor):
        dest_y = actor.y + self.dy
        dest_x = actor.x + self.dx

        if not engine.game_map.in_bounds(dest_y, dest_x):
            return
        if not engine.game_map.tiles[dest_y][dest_x]["walkable"]:
            return

        engine.render_tile(actor.y, actor.x)
        actor.move(dest_y, dest_x)
        engine.render_actor(actor)
