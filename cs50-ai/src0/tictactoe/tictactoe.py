"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    countX = 0
    countO = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                countX += 1
            elif board[row][col] == O:
                countO += 1
    return X if countX == countO else O            


def actions(board):

    possibleActions = set()

    for row in range(3):
        for column in range(3):
            if (board[row][column] == EMPTY):
                possibleActions.add((row, column))
    return possibleActions            


def result(board, action):
     
    if action not in actions(board):
        raise Exception("Invalid action")

    copiedArray = [row[:] for row in board]
    copiedArray[action[0]][action[1]] = player(board)
    return copiedArray


def checkRows(board, player):
    for row in range(3):
        if (board[row][0] == player and board[row][1] == player and board[row][2] == player):
            return True
    return False    


def checkColums(board, player):
    for col in range(3):
        if (board[0][col] == player and board[1][col] == player and board[2][col] == player):
            return True
    return False


def checkDiagonals(board, player):
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True
    elif (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False


def winner(board):
    if (checkRows(board, X) or checkColums(board, X) or checkDiagonals(board, X)):
        return X
    elif (checkRows(board, O) or checkColums(board, O) or checkDiagonals(board, O)):
        return O
    else:
        return None


def isTie(board):
    count = 9
    for row in range(3):
        for col in range(3):
            if (board[row][col] != EMPTY):
                count -= 1
    if (count == 0):
        return True
    

def terminal(board):
    if (winner(board) or isTie(board)):
        return True
    else:
        return False


def utility(board):

    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0
    

def min_value(board):
    if (terminal(board)):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

2
def max_value(board):
    if (terminal(board)):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def minimax(board):

    if (terminal(board)):
        return None
    elif (player(board) == X):
        arr = []
        for action in actions(board):
            arr.append((min_value(result(board, action)), action))
        return max(arr)[1]
    elif (player(board) == O):
        arr = []
        for action in actions(board):
            arr.append((max_value(result(board, action)), action))
        return min(arr)[1]