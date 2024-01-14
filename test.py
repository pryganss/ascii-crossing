#!/usr/bin/env python3
import curses

window = curses.initscr()
curses.noecho()
# window.keypad(True)

while True:
    k = window.getkey()
    print(k)
