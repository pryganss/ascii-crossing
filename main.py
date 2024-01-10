#!/usr/bin/env python3

import curses
from curses import wrapper


class Player:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def main(screen):
    curses.curs_set(0)

    player = Player(5, 5)
    while True:
        screen.addstr(player.y, player.x, "@")
        screen.refresh()

        key = screen.getkey()

        if key == "KEY_UP":
            player.y -= 1
        elif key == "KEY_DOWN":
            player.y += 1
        elif key == "KEY_LEFT":
            player.x -= 1
        elif key == "KEY_RIGHT":
            player.x += 1

        screen.clear()


if __name__ == "__main__":
    wrapper(main)
