#!/usr/bin/env python3

import curses
from curses import wrapper
from engine import Engine
from input import InputHandler
from actors import Player


def main(screen):
    curses.curs_set(0)
    screen.nodelay(True)

    engine = Engine(Player(0, 0), InputHandler(), screen)

    engine.render()

    while True:
        engine.handle_input()


if __name__ == "__main__":
    wrapper(main)
