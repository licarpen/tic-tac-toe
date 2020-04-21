"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty = 0
    for i in board:
        for j in i:
            if j == None:
                empty += 1
    if empty % 2 == 0:
        return O
    else: 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i, j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if action not in actions, raise exception
    if action not in actions(board):
        raise Exception('not a valid action')
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check for horizontal win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    # check for vertical win
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    if board[0][0] == board [1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_win = winner(board)
    if is_win == 'X' or  is_win == 'O' or len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    is_win = winner(board)
    if is_win == 'X':
        return 1
    elif is_win == 'O':
        return -1
    else:
        return 0

def minimax(board):
    best_score = -2
    current_actions = actions(board)
    for action in current_actions:
        current_board = result(board, action)
        score = get_utility(current_board)
        print(action, current_board, score)
        if score > best_score:
            best_score = score
            best_move = action
    return best_move
    
def get_utility(board):
    if terminal(board):
        return utility(board)
    current_player = player(board)
    if current_player == 'X':
        best_score = -2
        current_actions = actions(board)   
        for action in current_actions:
            current_board = result(board, action)
            score = get_utility(current_board)
            best_score = max(best_score, score)
            print(best_score)
        return best_score
    else:
        best_score = 2
        current_actions = actions(board) 
        for action in current_actions:
            current_board = result(board, action)
            score = get_utility(current_board)
            best_score = min(best_score, score)
        return best_score
