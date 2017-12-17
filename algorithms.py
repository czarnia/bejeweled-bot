import movesdict
import screen_handler as screen

def action(x,y,board,anchor):
    if screen.same_gem(x, y, x-1, y, board): # two gems next to each other, horizontal
        if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x+1, y, x+1, y-1, anchor) # right
        if screen.same_gem(x, y, x+2, y, board): movesdict.move_fields(x+1, y, x+2, y, anchor)
        if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x+1, y, x+1, y+1, anchor)
        if screen.same_gem(x, y, x-2, y-1, board): movesdict.move_fields(x-2, y, x-2, y-1, anchor) # left
        if screen.same_gem(x, y, x-2, y+1, board): movesdict.move_fields(x-2, y, x-2, y+1, anchor)
        if screen.same_gem(x, y, x-3, y, board): movesdict.move_fields(x-2, y, x-3, y, anchor)
    if screen.same_gem(x, y, x, y-1, board): # two gems next to each other, vertical
        if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x, y+1, x+1, y+1, anchor) # below
        if screen.same_gem(x, y, x, y+2, board): movesdict.move_fields(x, y+1, x, y+2, anchor)
        if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x, y+1, x-1, y+1, anchor)
        if screen.same_gem(x, y, x-1, y-2, board): movesdict.move_fields(x, y-2, x-1, y-2, anchor) # above
        if screen.same_gem(x, y, x+1, y-2, board): movesdict.move_fields(x, y-2, x+1, y-2, anchor)
        if screen.same_gem(x, y, x, y-3, board): movesdict.move_fields(x, y-2, x, y-3, anchor)
    if screen.same_gem(x, y, x-2, y, board): # gem in the middle is missing, horizontal
        if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x-1, y, x-1, y-1, anchor)
        if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x-1, y, x-1, y+1, anchor)
    if screen.same_gem(x, y, x, y-2, board): # gem in the middle is missing, vertical
        if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x, y-1, x-1, y-1, anchor)
        if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x, y-1, x+1, y-1, anchor)


def zone_algorithm(board, anchor):
    for y in range(4, 8):
        for x in range(0, 3):
            action(x,y,board,anchor)
    for y in range(4, 8):
        for x in range(4, 8):
            action(x,y,board,anchor)
    for y in range(2, 6):
        for x in range(2, 6):
            action(x,y,board,anchor)
    for y in range(0, 4):
        for x in range(0, 4):
            action(x,y,board,anchor)
    for y in range(0, 4):
        for x in range(4, 8):
            action(x,y,board,anchor)
    for y in range(2, 6):
        for x in range(0, 4):
            action(x,y,board,anchor)
    for y in range(2, 6):
        for x in range(4, 8):
            action(x,y,board,anchor)


def basic_algorithm_by_color(board, anchor):
    movesdictdict = {}
    color = 'a'
    maxcolor = 'a'
    length = 0;
    for y in range(0, 8):
        for x in range(0, 8):
            if screen.same_gem(x, y, x-1, y, board): # two gems next to each other, horizontal
                if screen.same_gem(x, y, x+1, y-1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x+1,y,x+1,y-1])
                if screen.same_gem(x, y, x+1, y-1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x+1, y, x+1, y-1])
                if screen.same_gem(x, y, x+2, y, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x+1, y, x+2, y])
                if screen.same_gem(x, y, x+1, y+1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x+1, y, x+1, y+1])
                if screen.same_gem(x, y, x-2, y-1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x-2, y, x-2, y-1])
                if screen.same_gem(x, y, x-2, y+1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x-2, y, x-2, y+1])
                if screen.same_gem(x, y, x-3, y, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x-2, y, x-3, y])
            if screen.same_gem(x, y, x, y-1, board): # two gems next to each other, vertical
                if screen.same_gem(x, y, x+1, y+1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x, y+1, x+1, y+1])
                if screen.same_gem(x, y, x, y+2, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x, y+1, x, y+2])
                if screen.same_gem(x, y, x-1, y+1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x, y+1, x-1, y+1])
                if screen.same_gem(x, y, x-1, y-2, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x, y-2, x-1, y-2])
                if screen.same_gem(x, y, x+1, y-2, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x, y-2, x+1, y-2])
                if screen.same_gem(x, y, x, y-3, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x, y-2, x, y-3])
            if screen.same_gem(x, y, x-2, y, board): # gem in the middle is missing, horizontal
                if screen.same_gem(x, y, x-1, y-1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x-1, y, x-1, y-1])
                if screen.same_gem(x, y, x-1, y+1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x-1, y, x-1, y+1])
            if screen.same_gem(x, y, x, y-2, board): # gem in the middle is missing, vertical
                if screen.same_gem(x, y, x-1, y-1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x, y-1, x-1, y-1])
                if screen.same_gem(x, y, x+1, y-1, board):
                    color = screen.get_field(x,y,anchor)
                    if color not in movesdict:
                        movesdict[color] = []
                    movesdict[color].append([x, y-1, x+1, y-1])

    for x in movesdict:
        if len(movesdict[x]) > length:
            length = len(movesdict[x])
            maxcolor = x

    for x in movesdict[maxcolor]:
        moves.move_fields(x[0], x[1], x[2], x[3], anchor)


def basic_algorithm_horizontal_first(board, anchor):
    for y in range(0, 8):
        for x in range(0, 8):
            if screen.same_gem(x, y, x-1, y, board): # two gems next to each other, horizontal
                if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x+1, y, x+1, y-1, anchor) # right
                if screen.same_gem(x, y, x+2, y, board): movesdict.move_fields(x+1, y, x+2, y, anchor)
                if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x+1, y, x+1, y+1, anchor)
                if screen.same_gem(x, y, x-2, y-1, board): movesdict.move_fields(x-2, y, x-2, y-1, anchor) # left
                if screen.same_gem(x, y, x-2, y+1, board): movesdict.move_fields(x-2, y, x-2, y+1, anchor)
                if screen.same_gem(x, y, x-3, y, board): movesdict.move_fields(x-2, y, x-3, y, anchor)
            if screen.same_gem(x, y, x-2, y, board): # gem in the middle is missing, horizontal
                if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x-1, y, x-1, y-1, anchor)
                if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x-1, y, x-1, y+1, anchor)
            if screen.same_gem(x, y, x, y-1, board): # two gems next to each other, vertical
                if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x, y+1, x+1, y+1, anchor) # below
                if screen.same_gem(x, y, x, y+2, board): movesdict.move_fields(x, y+1, x, y+2, anchor)
                if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x, y+1, x-1, y+1, anchor)
                if screen.same_gem(x, y, x-1, y-2, board): movesdict.move_fields(x, y-2, x-1, y-2, anchor) # above
                if screen.same_gem(x, y, x+1, y-2, board): movesdict.move_fields(x, y-2, x+1, y-2, anchor)
                if screen.same_gem(x, y, x, y-3, board): movesdict.move_fields(x, y-2, x, y-3, anchor)
            if screen.same_gem(x, y, x, y-2, board): # gem in the middle is missing, vertical
                if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x, y-1, x-1, y-1, anchor)
                if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x, y-1, x+1, y-1, anchor)


def basic_algorithm_vertical_first_middle(board, anchor):
    for y in range(0, 8):
        for x in range(0, 8):
            if screen.same_gem(x, y, x, y-2, board): # gem in the middle is missing, vertical
                if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x, y-1, x-1, y-1, anchor)
                if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x, y-1, x+1, y-1, anchor)
            if screen.same_gem(x, y, x, y-1, board): # two gems next to each other, vertical
                if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x, y+1, x+1, y+1, anchor) # below
                if screen.same_gem(x, y, x, y+2, board): movesdict.move_fields(x, y+1, x, y+2, anchor)
                if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x, y+1, x-1, y+1, anchor)
                if screen.same_gem(x, y, x-1, y-2, board): movesdict.move_fields(x, y-2, x-1, y-2, anchor) # above
                if screen.same_gem(x, y, x+1, y-2, board): movesdict.move_fields(x, y-2, x+1, y-2, anchor)
                if screen.same_gem(x, y, x, y-3, board): movesdict.move_fields(x, y-2, x, y-3, anchor)
            if screen.same_gem(x, y, x-2, y, board): # gem in the middle is missing, horizontal
                if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x-1, y, x-1, y-1, anchor)
                if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x-1, y, x-1, y+1, anchor)
            if screen.same_gem(x, y, x-1, y, board): # two gems next to each other, horizontal
                if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x+1, y, x+1, y-1, anchor) # right
                if screen.same_gem(x, y, x+2, y, board): movesdict.move_fields(x+1, y, x+2, y, anchor)
                if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x+1, y, x+1, y+1, anchor)
                if screen.same_gem(x, y, x-2, y-1, board): movesdict.move_fields(x-2, y, x-2, y-1, anchor) # left
                if screen.same_gem(x, y, x-2, y+1, board): movesdict.move_fields(x-2, y, x-2, y+1, anchor)
                if screen.same_gem(x, y, x-3, y, board): movesdict.move_fields(x-2, y, x-3, y, anchor)

def basic_algorithm_vertical_first_boarder(board, anchor):
    for y in range(0, 8):
        for x in range(0, 8):
            if screen.same_gem(x, y, x, y-1, board): # two gems next to each other, vertical
                if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x, y+1, x+1, y+1, anchor) # below
                if screen.same_gem(x, y, x, y+2, board): movesdict.move_fields(x, y+1, x, y+2, anchor)
                if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x, y+1, x-1, y+1, anchor)
                if screen.same_gem(x, y, x-1, y-2, board): movesdict.move_fields(x, y-2, x-1, y-2, anchor) # above
                if screen.same_gem(x, y, x+1, y-2, board): movesdict.move_fields(x, y-2, x+1, y-2, anchor)
                if screen.same_gem(x, y, x, y-3, board): movesdict.move_fields(x, y-2, x, y-3, anchor)
            if screen.same_gem(x, y, x, y-2, board): # gem in the middle is missing, vertical
                if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x, y-1, x-1, y-1, anchor)
                if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x, y-1, x+1, y-1, anchor)
            if screen.same_gem(x, y, x-1, y, board): # two gems next to each other, horizontal
                if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x+1, y, x+1, y-1, anchor) # right
                if screen.same_gem(x, y, x+2, y, board): movesdict.move_fields(x+1, y, x+2, y, anchor)
                if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x+1, y, x+1, y+1, anchor)
                if screen.same_gem(x, y, x-2, y-1, board): movesdict.move_fields(x-2, y, x-2, y-1, anchor) # left
                if screen.same_gem(x, y, x-2, y+1, board): movesdict.move_fields(x-2, y, x-2, y+1, anchor)
                if screen.same_gem(x, y, x-3, y, board): movesdict.move_fields(x-2, y, x-3, y, anchor)
            if screen.same_gem(x, y, x-2, y, board): # gem in the middle is missing, horizontal
                if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x-1, y, x-1, y-1, anchor)
                if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x-1, y, x-1, y+1, anchor)



def basic_algorithm(board, anchor):
    for y in range(0, 8):
        for x in range(0, 8):
            if screen.same_gem(x, y, x-1, y, board): # two gems next to each other, horizontal
                if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x+1, y, x+1, y-1, anchor) # right
                if screen.same_gem(x, y, x+2, y, board): movesdict.move_fields(x+1, y, x+2, y, anchor)
                if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x+1, y, x+1, y+1, anchor)
                if screen.same_gem(x, y, x-2, y-1, board): movesdict.move_fields(x-2, y, x-2, y-1, anchor) # left
                if screen.same_gem(x, y, x-2, y+1, board): movesdict.move_fields(x-2, y, x-2, y+1, anchor)
                if screen.same_gem(x, y, x-3, y, board): movesdict.move_fields(x-2, y, x-3, y, anchor)
            if screen.same_gem(x, y, x, y-1, board): # two gems next to each other, vertical
                if screen.same_gem(x, y, x+1, y+1, board): movesdict.move_fields(x, y+1, x+1, y+1, anchor) # below
                if screen.same_gem(x, y, x, y+2, board): movesdict.move_fields(x, y+1, x, y+2, anchor)
                if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x, y+1, x-1, y+1, anchor)
                if screen.same_gem(x, y, x-1, y-2, board): movesdict.move_fields(x, y-2, x-1, y-2, anchor) # above
                if screen.same_gem(x, y, x+1, y-2, board): movesdict.move_fields(x, y-2, x+1, y-2, anchor)
                if screen.same_gem(x, y, x, y-3, board): movesdict.move_fields(x, y-2, x, y-3, anchor)
            if screen.same_gem(x, y, x-2, y, board): # gem in the middle is missing, horizontal
                if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x-1, y, x-1, y-1, anchor)
                if screen.same_gem(x, y, x-1, y+1, board): movesdict.move_fields(x-1, y, x-1, y+1, anchor)
            if screen.same_gem(x, y, x, y-2, board): # gem in the middle is missing, vertical
                if screen.same_gem(x, y, x-1, y-1, board): movesdict.move_fields(x, y-1, x-1, y-1, anchor)
                if screen.same_gem(x, y, x+1, y-1, board): movesdict.move_fields(x, y-1, x+1, y-1, anchor)

def random_algorithm(board, anchor):
    for y in range(0, 8):
        for x in range(0, 8):
            if screen.same_gem(x, y, x-1, y, board): # two gems next to each other, horizontal
                movesdict.move_fields(x+1, y, x+1, y-1, anchor) # right
                movesdict.move_fields(x+1, y, x+2, y, anchor)
                movesdict.move_fields(x+1, y, x+1, y+1, anchor)
                movesdict.move_fields(x-2, y, x-2, y-1, anchor) # left
                movesdict.move_fields(x-2, y, x-2, y+1, anchor)
                movesdict.move_fields(x-2, y, x-3, y, anchor)
            if screen.same_gem(x, y, x, y-1, board): # two gems next to each other, vertical
                movesdict.move_fields(x, y+1, x+1, y+1, anchor) # below
                movesdict.move_fields(x, y+1, x, y+2, anchor)
                movesdict.move_fields(x, y+1, x-1, y+1, anchor)
                movesdict.move_fields(x, y-2, x-1, y-2, anchor) # above
                movesdict.move_fields(x, y-2, x+1, y-2, anchor)
                movesdict.move_fields(x, y-2, x, y-3, anchor)
            if screen.same_gem(x, y, x-2, y, board): # gem in the middle is missing, horizontal
                movesdict.move_fields(x-1, y, x-1, y-1, anchor)
                movesdict.move_fields(x-1, y, x-1, y+1, anchor)
            if screen.same_gem(x, y, x, y-2, board): # gem in the middle is missing, vertical
                movesdict.move_fields(x, y-1, x-1, y-1, anchor)
                movesdict.move_fields(x, y-1, x+1, y-1, anchor)
