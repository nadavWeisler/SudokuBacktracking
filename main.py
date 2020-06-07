#############################################################
# FILE : ex8.py
# WRITER : Nadav Weisler , weisler , 316493758
# EXERCISE : intro2cs ex8
# DESCRIPTION: Contains sudoku solving algorithem and
#   different versions for handling subsets of list
#############################################################

import math


def solve_sudoku(board):
    """
    General function for solve sudoku
    :param board: matrix
    :return: boolean
    """
    origin = board[:]
    val = play_sudoku(board)
    if val:
        return True

    board = origin
    return False


def play_sudoku(board, current=(0, 0)):
    """
    Check if sudoku board has a solution
    :param board: matrix
    :param current: tuple (index in matrix)
    :return: boolean
    """
    current = next_cell(board, current)
    if current == None:
        return True
    for i in range(1, len(board) + 1):
        if board_valid(board, current, i):
            board[current[0]][current[1]] = i
            if play_sudoku(board, current):
                return True
            board[current[0]][current[1]] = 0
    return False


def next_cell(board, current):
    """
    Get next cell in board after current
    :param board: matrix
    :param current: tuple (matrix index)
    :return: tuple(matrix index) or None if not exists
    """
    for row in range(current[0], len(board)):
        for col in range(current[1], len(board)):
            if board[row][col] == 0:
                return (row, col)
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row, col)
    return None


def board_valid(board, current, i):
    """
    Check if matrix is valid
    :param board: matrix
    :param current: tuple(matrix index)
    :param i: number
    :return: boolean
    """
    if all([i != board[current[0]][x] for x in range(len(board))]):
        valid_col = all([i != board[x][current[0]] for x in range(len(board))])
        if valid_col:
            sqrt_n = int(math.sqrt(len(board)))
            top_point = (sqrt_n * (current[0] // sqrt_n),
                         sqrt_n * (current[1] // sqrt_n))
            for x in range(top_point[0], top_point[0] + sqrt_n):
                for y in range(top_point[1], top_point[1] + sqrt_n):
                    if board[x][y] == i:
                        return False
            return True
    return False


def get_set_from_curs(cur_set):
    """
    Get number set from boolean list
    :param cur_set: list
    :return: list
    """
    result = []
    for (idx, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            result.append(idx)
    return result


def k_subset_helper_for_return(cur_set, k, index, picked):
    # Base: we picked out k items.
    if k == picked:
        format_set = get_set_from_curs(cur_set)
        return [format_set]

    # If we reached the end of the list, backtrack.
    if index == len(cur_set):
        return []

    # Runs on all sets that include this index.
    cur_set_with_true = cur_set[:]
    cur_set_with_true[index] = True

    cur_set_with_false = cur_set[:]
    cur_set_with_false[index] = False

    return k_subset_helper_for_return(cur_set_with_true, k, index + 1, picked + 1) + \
           (k_subset_helper_for_return(cur_set_with_false, k, index + 1, picked))


def k_subset_helper_for_fill(cur_set, k, index, picked, result=[]):
    # Base: we picked out k items.
    if k == picked:
        format_set = get_set_from_curs(cur_set)
        result.append(format_set)
        return

    # If we reached the end of the list, backtrack.
    if index == len(cur_set):
        return

    # Runs on all sets that include this index.
    cur_set[index] = True
    k_subset_helper_for_fill(cur_set, k, index + 1, picked + 1, result)

    # Runs on all sets that do not include index.
    cur_set[index] = False
    k_subset_helper_for_fill(cur_set, k, index + 1, picked, result)


def k_subset_helper_for_print(cur_set, k, index, picked):
    # Base: we picked out k items.
    if k == picked:
        format_set = get_set_from_curs(cur_set)
        print(format_set)
        return

    # If we reached the end of the list, backtrack.
    if index == len(cur_set):
        return

    # Runs on all sets that include this index.
    cur_set[index] = True
    k_subset_helper_for_print(cur_set, k, index + 1, picked + 1)

    # Runs on all sets that do not include index.
    cur_set[index] = False
    k_subset_helper_for_print(cur_set, k, index + 1, picked)


def print_k_subsets(n, k):
    if k <= n:
        cur_set = [False] * n
        k_subset_helper_for_print(cur_set, k, 0, 0)


def fill_k_subsets(n, k, lst):
    if k <= n:
        cur_set = [False] * n
        k_subset_helper_for_fill(cur_set, k, 0, 0, lst)


def return_k_subsets(n, k):
    if k <= n:
        cur_set = [False] * n
        return k_subset_helper_for_return(cur_set, k, 0, 0)
