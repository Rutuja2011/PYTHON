#slip4_2
#Write a puthon porgram fo the eight queens problem.(Uniformed Search)

N = 8

def solveNQueens(board, col):
    # Base case: All queens are placed
    if col == N:
        printSolution(board)
        return True

    # Try placing the queen in each row of this column
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur for the next column
            if solveNQueens(board, col + 1):
                return True

            # If placing the queen doesn't lead to a solution, backtrack
            board[i][col] = 0

    return False

def isSafe(board, row, col):
    # Check left side in current row
    for x in range(col):
        if board[row][x] == 1:
            return False

    # Check upper diagonal on left side
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    # Check lower diagonal on left side
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()  # blank line for clarity


# Initialize the chessboard
board = [[0 for _ in range(N)] for _ in range(N)]


# Run solver
if not solveNQueens(board, 0):
    print("No solution found")
