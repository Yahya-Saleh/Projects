# Tic Tac Toe Player

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Initialize the count variables
    X_count = 0
    O_count = 0

    # For each row count the instance of each values
    for row in board:
        X_count += row.count(X)
        O_count += row.count(O)

    # Since X goes first it will be X's turn if both players had an equal number of moves
    if X_count == O_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pos_actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            # If the cell is empty Then a move is possible
            if cell == EMPTY:
                # Add its position
                pos_actions.add((i, j))

    return pos_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Verify if the action is possible
    i, j = action
    # If the cell is not empty then the action is not possible
    if board[i][j] != EMPTY:
        raise Exception("Not a valid action")

    # Create a deep copy so as not to alter the original list since the AI uses it
    result = deepcopy(board)
    result[i][j] = player(board)

    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Horizontal checking
        if board[i].count(X) == 3:
            return X
        elif board[i].count(O) == 3:
            return O

        # Vertical checking
        if board[0][i] != EMPTY:
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return board[0][i]

    # Diagonal checking
    for i in range(0, 3, 2):
        if board[0][i] != EMPTY:
            if board[0][i] == board[2][abs(i - 2)]:
                if board[0][i] == board[1][1]:
                    return board[1][1]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    # If an Empty cell exists and there's no winner then the game is not over
    for row in board:
        if row.count(EMPTY) > 0:
            return False

    # It's a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # The X player wants to maximize the value and the O minimizes
    if player(board) == X:
        return max_value(board)[1]
    else:
        return mini_value(board)[1]


def max_value(board):
    if terminal(board):
        return [utility(board)]

    best_action = [-2, ()]
    for action in actions(board):
        actions_value = mini_value(result(board, action))

        if actions_value[0] > best_action[0]:
            best_action[0] = actions_value[0]
            best_action[1] = action

            if actions_value[0] == 1:
                return best_action

    return best_action


def mini_value(board):
    if terminal(board):
        return [utility(board)]

    best_action = [2, ()]
    for action in actions(board):
        actions_value = max_value(result(board, action))

        if actions_value[0] < best_action[0]:
            best_action[0] = actions_value[0]
            best_action[1] = action

            if actions_value[0] == -1:
                return best_action

    return best_action
