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


def tile(walkable, char, t_id):
    tile = {}
    tile["walkable"] = walkable
    tile["char"] = char
    tile["id"] = t_id

    return tile


class Tiles:
    GRASS = tile(True, ".", "floor")
    TREE = tile(False, "♣", "tree")
