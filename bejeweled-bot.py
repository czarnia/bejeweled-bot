#!/usr/bin/python
# -*- coding: ascii -*-
'''
Plays a game of Bejeweled Blitz on Facebook.

Created: 24.12.2012
Updated: Aug 2016

@author: Adrianus Kleemans
'''

import pygame
import time
import sys

import moves
import screen_handler as screen

MAX_MOVES = 5
DRAW_CANVAS = False
MAX_TIME = 75 # for some gems, use up to 160s

def start_game(anchor):
    print "Starting game!"
    time.sleep(3)
    moves.focus_on_browser(anchor)
    time.sleep(1)
    moves.click_play(anchor)
    time.sleep(1)

### main ###

def main():
    print 'Starting, please bring window into position'
    time.sleep(3)

    anchor = screen.get_anchor();

    if (not anchor[0]) or (not anchor[1]):
        return

    # preparing canvas
    if DRAW_CANVAS:
        screen.start_canvas()

	# play
    start_game(anchor)

    board = screen.get_board(anchor)
    t = time.time()

    while (time.time() - t) < MAX_TIME:
        if screen.get_field(2, 4, anchor) == (60, 109, 118) or screen.get_field(4, 6, anchor) == (219, 219, 219) or not screen.board_valid(board):
            break # "time up", "encore" or  board corrupted
        board = screen.get_board(anchor)

        if DRAW_CANVAS: screen.draw_canvas(board)

        for y in range(0, 8):
            for x in range(0, 8):
                if screen.same_gem(x, y, x-1, y, board): # two gems next to each other, horizontal
                    if screen.same_gem(x, y, x+1, y-1, board): moves.move_fields(x+1, y, x+1, y-1, anchor) # right
                    if screen.same_gem(x, y, x+2, y, board): moves.move_fields(x+1, y, x+2, y, anchor)
                    if screen.same_gem(x, y, x+1, y+1, board): moves.move_fields(x+1, y, x+1, y+1, anchor)
                    if screen.same_gem(x, y, x-2, y-1, board): moves.move_fields(x-2, y, x-2, y-1, anchor) # left
                    if screen.same_gem(x, y, x-2, y+1, board): moves.move_fields(x-2, y, x-2, y+1, anchor)
                    if screen.same_gem(x, y, x-3, y, board): moves.move_fields(x-2, y, x-3, y, anchor)
                if screen.same_gem(x, y, x, y-1, board): # two gems next to each other, vertical
                    if screen.same_gem(x, y, x+1, y+1, board): moves.move_fields(x, y+1, x+1, y+1, anchor) # below
                    if screen.same_gem(x, y, x, y+2, board): moves.move_fields(x, y+1, x, y+2, anchor)
                    if screen.same_gem(x, y, x-1, y+1, board): moves.move_fields(x, y+1, x-1, y+1, anchor)
                    if screen.same_gem(x, y, x-1, y-2, board): moves.move_fields(x, y-2, x-1, y-2, anchor) # above
                    if screen.same_gem(x, y, x+1, y-2, board): moves.move_fields(x, y-2, x+1, y-2, anchor)
                    if screen.same_gem(x, y, x, y-3, board): moves.move_fields(x, y-2, x, y-3, anchor)
                if screen.same_gem(x, y, x-2, y, board): # gem in the middle is missing, horizontal
                    if screen.same_gem(x, y, x-1, y-1, board): moves.move_fields(x-1, y, x-1, y-1, anchor)
                    if screen.same_gem(x, y, x-1, y+1, board): moves.move_fields(x-1, y, x-1, y+1, anchor)
                if screen.same_gem(x, y, x, y-2, board): # gem in the middle is missing, vertical
                    if screen.same_gem(x, y, x-1, y-1, board): moves.move_fields(x, y-1, x-1, y-1, anchor)
                    if screen.same_gem(x, y, x+1, y-1, board): moves.move_fields(x, y-1, x+1, y-1, anchor)
    print "Game ended."
    return

if __name__ == "__main__":
    main()
