# N-Queens Problem using Backtracking in Python

def print_board(board, n):   #Function to print the chessboard
    print("\n Solution for", n, "Queens:\n")

    for row in board:   
        for cell in row:
            print(cell, end=" ")
        print()


def is_safe(board, row, col, n):  #Function to check if queen can be placed safely 

    for i in range(col):  #Check left-side of current row
        if board[row][i] == "Q":
            return False

    #Check upper diagonal on left side
    i = row 
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    #Check lower diagonal on left side 
    i = row
    j = col

    while i < n and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):   #backtracking function to solve N-Queens 

    # Base Case: All queens are placed
    if col >= n:
        return True

    # Try placing queen in every row
    for row in range(n):

        # Check safe position
        if is_safe(board, row, col, n):

            board[row][col] = "Q"   #Place queen

            if solve_n_queens(board, col + 1, n):    #Recursive call for next column 
                return True

            board[row][col] = "."   #Backtracking

    return False


n = int(input("Enter value of N: "))   #Main program

board = [["." for _ in range(n)] for _ in range(n)]  #Create empty chessboard

if solve_n_queens(board, 0, n): #Solve problem
    print_board(board, n)
else:
    print("No solution exists.")