#!/usr/bin/python
# -*- coding: ascii -*-

import autopy as ap
import time

### constants ###
SLEEPING_TIME = 0.02

import screen_handler as screen

### input helpers ###

def left_down():
    ap.mouse.toggle(True, ap.mouse.LEFT_BUTTON)
    time.sleep(SLEEPING_TIME)

def left_up():
    ap.mouse.toggle(False, ap.mouse.LEFT_BUTTON)
    time.sleep(SLEEPING_TIME)

def move_mouse(x, y, anchor):
    x, y = screen.board_to_pixel(x, y, anchor)
    ap.mouse.move(int(x), int(y))
    time.sleep(SLEEPING_TIME)

def click(x, y, anchor):
    move_mouse(x, y, anchor)
    left_down()
    left_up()

def move_fields(x0, y0, x1, y1, anchor):
    move_mouse(x0, y0, anchor)
    left_down()
    move_mouse(x1, y1, anchor)
    left_up()


def focus_on_browser(anchor):
    click(2, 7, anchor)

def click_play(anchor):
    click(2, 7, anchor)
