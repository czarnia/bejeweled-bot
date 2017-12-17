#!/usr/bin/python
# -*- coding: ascii -*-

import autopy as ap
import pygame
import struct
import Quartz.CoreGraphics as CG

### screen helpers #

def get_color(x,y,board):
    return board[y][x]

def get_pixel(x, y):
    x, y = int(x)*2, int(y)*2
    data_format = "BBBB" #BBBB
    offset = 4 * ((screenshot_width*int(round(y))) + int(round(x)))
    b, g, r, a = struct.unpack_from(data_format, screenshot_data, offset=offset)
    return (r, g, b)

def get_field(x, y, anchor):
    x, y = board_to_pixel(x, y, anchor)
    return get_pixel(x, y)

def get_board(anchor):
    capture()
    board = []
    for y in range(0, 8):
        board.append([])
        for x in range(0, 8):
            pix = get_field(x, y, anchor)
            color = match_color(pix)
            board[y].append(color)
    return board

def get_screen_size():
    return ap.screen.get_size();

def match_color(pix):
    names = ['y', 'w', 'r', 'o', 'p', 'g', 'b', 'X', 'g', 'y',
             'y', 'g', 'b', 'w', 'g', 'r', 'p', 'p', 'o', 'p', 'b']
    colors = [(254, 254, 38), (254, 254, 254), (254, 29, 59),
              (254, 254, 137), (250, 10, 250), (98, 254, 156),
              (20, 112, 232), (114, 186, 112), (0, 168, 10),
              (254, 247, 67), (255, 255, 102), (206, 255, 255),
              (44, 156, 252), (211, 211, 211),  (0, 94, 6),
              (215, 17, 30), (185, 16, 184), (217, 19, 216),
              (252, 126, 44), (255, 73, 255), (21, 74, 120)]
    c = 0
    for color in colors:
        diff = 0
        for i in range(3):
            diff += abs(color[i]-pix[i])
        if diff < 60:
            return names[c]
        c += 1
    return '.'

def board_to_pixel(x, y, anchor):
    x = x*40 + 195 + anchor[0]
    y = y*40 + 70 + anchor[1]
    return x, y

def capture():
    global screenshot_width
    global screenshot_data
    region = CG.CGRectInfinite
    # Create screenshot as CGImage
    image = CG.CGWindowListCreateImage(region, CG.kCGWindowListOptionOnScreenOnly,
                                       CG.kCGNullWindowID, CG.kCGWindowImageDefault)
    prov = CG.CGImageGetDataProvider(image)
    screenshot_data = CG.CGDataProviderCopyData(prov)
    screenshot_width = CG.CGImageGetWidth(image)

def same_gem(x0, y0, x1, y1, board):
    m = 7 # max row
    if x0 < 0 or y0 < 0 or x1 < 0 or y1 < 0 or x0 > m or y0 > m or x1 > m or y1 > m:
        return False
    elif board[y0][x0] == '.' or board[y1][x1] == '.':
        return False
    elif board[y0][x0] == 'X' or board[y1][x1] == 'X':
        return True
    else:
        return board[y0][x0] == board[y1][x1]

def board_valid(board):
    whites = 0
    for line in board:
        for field in line:
            if field == 'w':
                whites += 1
    if whites >= 20:
        return False
    else:
        return True

### anchor helpers ###

def get_anchor():
    screen_size = get_screen_size();
    print 'Searching for anchor, please stand by. screen size:', screen_size
    capture()

    x = y = 0
    for i in range(screen_size[0]):
        if x == 0 and get_pixel(i, screen_size[1]/2) == (199, 199, 199):
            x = i
        if y == 0 and get_pixel(screen_size[0]/3, i) == (215, 215, 215):
            y = i
        if x != 0 and y != 0:
            anchor = (x, y)
            break
    print "Detected anchor:", anchor

    return anchor

### canvas helpers ###

def draw_canvas(board):
    board_size = [320, 320]
    colors = {'y': (254, 254, 38), 'w': (254, 254, 254), 'r': (254, 29, 59),
              'o': (254, 128, 0),  'p': (250, 10, 250),  'g': (50, 254, 50),
              'b': (20, 112, 232), 'X': (114, 186, 112), '.': (0, 0, 0)}
    signs = []
    for line in board:
        for sign in line:
            signs.append(sign)

    for y in range(8):
        for x in range(8):
            col = colors[board[y][x]]
            pygame.draw.rect(disp, col, (x*40, y*40, 40, 40))
    pygame.display.flip()

def start_canvas():
    pygame.init()
    disp = pygame.display.set_mode([320, 320])
    pygame.display.set_caption("Bejeweled Blitz Demo")
