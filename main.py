#!/usr/bin/env python3

import curses
from curses import wrapper
from input import InputHandler
from actions import MovementAction, QuitAction
from actors import Player


def main(screen):
    curses.curs_set(0)

    input_handler = InputHandler()

    player = Player(5, 5)
    while True:
        screen.addstr(player.y, player.x, "@")
        screen.refresh()

        key = screen.getkey()
        action = input_handler.keydown(key)

        if action is None:
            continue

        if isinstance(action, MovementAction):
            player.y += action.dy
            player.x += action.dx

        elif isinstance(action, QuitAction):
            raise SystemExit()

        screen.clear()


if __name__ == "__main__":
    wrapper(main)
