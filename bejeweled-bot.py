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
import algorithms

MAX_MOVES = 5
DRAW_CANVAS = True
MAX_TIME = 65 # for some gems, use up to 160s

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

        algorithms.zone_algorithm(board, anchor)

    print "Game ended."
    return

if __name__ == "__main__":
    main()
