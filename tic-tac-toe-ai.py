
## CodSoft Task 1 Tic tac toe AI ##

import math
import copy
import os

X = 100
O = -100
tie = 0

player_dict = {
    X : " X ", 
    O : " O ", 
    tie : " _ "
}

state = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def winner(state):
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] and state[i][0] != 0:
            return state[i][0]
        if state[0][i] == state[1][i] == state[2][i] and state[0][i] != 0:
            return state[0][i]
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != 0:
        return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] != 0:
        return state[0][2]

    return tie

def available_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                moves.append([i,j])
    return moves


####  ALGORITHM ####
def minimax(state, depth, player):
    s = copy.deepcopy(state)

    winning_player = winner(s)
    if  winning_player != tie:
        if winning_player == X : 
            return winning_player - depth
        else :
            return winning_player + depth

    if len(available_moves(s)) == 0 :
        return 0

    if player == X:
        max_val = -math.inf
        for move in available_moves(s):
            i = move[0]
            j = move[1]
            s[i][j] = player
            val = minimax(s, depth+1, O)
            s[i][j] = 0
            max_val = max(max_val , val)

        return max_val
    
    if player == O:
        min_val = math.inf
        for move in available_moves(s):
            i = move[0]
            j = move[1]
            s[i][j] = player
            val = minimax(s, depth+1, X)
            s[i][j] = 0
            min_val = min(min_val, val)

        return min_val
    
#### MAX TURN ####
def max_turn(state):
    max_val = -math.inf
    max_move = None
    s = copy.deepcopy(state)
    for move in available_moves(s):
        i, j = move[0], move[1]
        s[i][j] = X
        val = minimax(s, 1, O)
        if max_val < val:
            max_val = val
            max_move = move
        s[i][j] = 0
    return max_move

##### MIN TURN #####
def min_turn(state):
    min_val = math.inf
    min_move = None
    s = copy.deepcopy(state)
    for move in available_moves(s):
        i, j = move[0], move[1]
        s[i][j] = O
        val = minimax(s, 1, X)
        if min_val > val:
            min_val = val
            min_move = move
        s[i][j] = 0
    return min_move

###############################################################

########################## PLAY ###############################
def play(begin_state, begin_player):
    s = begin_state
    player = begin_player
    os.system("clear")
    print('-'*11)
    for i in range(3):
        print("|" , end='')
        for j in range(3):
            print(player_dict[s[i][j]], end='')
        print("|")
        print('-'*11)
    print()
    print()
    try:
        while winner(s) == 0:
            
            if player == X:         #user
                while True:
                    print("YOUR TURN!")
                    i,j = input("Enter your move (row col): ").strip().split()
                    i,j = int(i), int(j)
                    i -= 1
                    j -= 1
                    while (i not in range(3) or j not in range(3)):
                        print("Invalid Move! Try again.")
                        i,j = input("Enter your move (row col): ").strip().split()
                        i,j = int(i), int(j)
                        i -= 1
                        j -= 1
                    if s[i][j] != 0:
                        print("Enter the move for empty square! Try again.")
                    else :
                        break
                s[i][j] = X
                player = O
            else :                  #AI
                os.system("clear")
                # print("MY TURN!")
                move = min_turn(s)
                i,j = move[0], move[1]
                s[i][j] = O
                player = X
            
            print('-'*11)
            for i in range(3):
                print("|" , end='')
                for j in range(3):
                    print(player_dict[s[i][j]], end='')
                print("|")
                print('-'*11)
            print()
            print()
        
    except KeyboardInterrupt:
        print("Game Interrupted!")
        exit(0)


##### MAIN #####
if __name__ == "__main__":
    os.system('clear')
    print("You are the first player!")
    p = input("Pick your Peice [x or o] : ").strip().upper()
    while (p != 'X' and p != 'O'):
        print("Invalid Choice! Try again.")
        p = input("Pick your Peice [x or o] : ").strip().upper()
    if p == 'O':
        player_dict[X] = " O "
        player_dict[O] = " X "
    print("Press Enter to start the game!")
    input()
    play(state, X)
