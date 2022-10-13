board = [7,2,4,5,6," ",8,3,1]
goal_board = [1,2,3,4,5,6,7,8," "]

def show_board(board):
    for i in range(len(board)):
        print(board[i],end=" ")
        if i % 3 == 2:
            print()
    print()


def get_possible_actions(board):
   
    actions = []
    empty_index = board.index(" ")
    r = empty_index // 3
    c = empty_index % 3
    if r < 2:
        actions.append("Down")
    if r > 0:
        actions.append("Up")
    if c < 2:
        actions.append("Right")
    if c > 0:
        actions.append("Left")
    return actions



def update_board(board,action):
    empty_index = board.index(" ")
    if action == "Up":
        switch_index = empty_index - 3
    elif action == "Down":
        switch_index = empty_index + 3
    elif action == "Left":
        switch_index = empty_index - 1
    else: 
        switch_index = empty_index + 1
    board[empty_index], board[switch_index] = board[switch_index], board[empty_index]


import random
def random_shuffle(board, move_cnt):
    for i in range(move_cnt):
        update_board(board, random.choice(get_possible_actions(board)))


#Random Search

def random_search(board):
    loop_cnt = 0
    while board != goal_board:
        action = random.choice(get_possible_actions(board))
        update_board(board, action)
        
        loop_cnt += 1
    show_board(board)
    print("Done in {} steps".format(loop_cnt))



show_board(board)
show_board(goal_board)
print(get_possible_actions(board))
random_shuffle(board,100)
random_search(board)
print()