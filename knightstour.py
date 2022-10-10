chess_board = [[1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]

def print_board():
    for i in range(8):
        for j in range(8):
            print(chess_board[i][j], end="\t")
        print("\n")


def poss_(x, y):
    x_pos = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []
    for i in range(8):
        if x+x_pos[i] >= 0 and x+x_pos[i] <= 7 and y+pos_y[i] >= 0 and y+pos_y[i] <= 7 and chess_board[x+x_pos[i]][y+pos_y[i]] == 0:
            possibilities.append([x+x_pos[i], y+pos_y[i]])

    return possibilities

def solve():
    counter = 2
    x = 0
    y = 0
    for i in range(63):
        pos = poss_(x, y)
        minimum = pos[0]
        for p in pos:
            if len(poss_(p[0], p[1])) <= len(poss_(minimum[0], minimum[1])):
                minimum = p
        x = minimum[0]
        y = minimum[1]
        chess_board[x][y] = counter
        counter += 1
    


solve()  

print_board()