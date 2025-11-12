def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    if row == n:
        print_board(board)
        return True  # or remove this if you want all solutions instead of first one

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n)
            board[row][col] = 0  # backtrack

    return False

def make_arr(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


# Example usage:
n = 4
board = make_arr(n, n)
# print_board(board)
solve_nqueens(board, 0, n)
