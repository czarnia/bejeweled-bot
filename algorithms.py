import moves
import screen_handler as screen

def basic_algorithm(board, anchor):
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

def random_algorithm(board, anchor):
    for y in range(0, 8):
        for x in range(0, 8):
            if screen.same_gem(x, y, x-1, y, board): # two gems next to each other, horizontal
                moves.move_fields(x+1, y, x+1, y-1, anchor) # right
                moves.move_fields(x+1, y, x+2, y, anchor)
                moves.move_fields(x+1, y, x+1, y+1, anchor)
                moves.move_fields(x-2, y, x-2, y-1, anchor) # left
                moves.move_fields(x-2, y, x-2, y+1, anchor)
                moves.move_fields(x-2, y, x-3, y, anchor)
            if screen.same_gem(x, y, x, y-1, board): # two gems next to each other, vertical
                moves.move_fields(x, y+1, x+1, y+1, anchor) # below
                moves.move_fields(x, y+1, x, y+2, anchor)
                moves.move_fields(x, y+1, x-1, y+1, anchor)
                moves.move_fields(x, y-2, x-1, y-2, anchor) # above
                moves.move_fields(x, y-2, x+1, y-2, anchor)
                moves.move_fields(x, y-2, x, y-3, anchor)
            if screen.same_gem(x, y, x-2, y, board): # gem in the middle is missing, horizontal
                moves.move_fields(x-1, y, x-1, y-1, anchor)
                moves.move_fields(x-1, y, x-1, y+1, anchor)
            if screen.same_gem(x, y, x, y-2, board): # gem in the middle is missing, vertical
                moves.move_fields(x, y-1, x-1, y-1, anchor)
                moves.move_fields(x, y-1, x+1, y-1, anchor)
