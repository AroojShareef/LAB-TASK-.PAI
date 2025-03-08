def is_safe(board, row, col, n):
    """
check if a queen safe to place at board[row][col].
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
         
    i , j = row, col
    while i >=0 and j >=0:
        if board [i][j] == 1:
            return False
        
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True
def solve_n_queen(board, row , n):
    """
    solve the n-queen problem by using backtracking.
    """   

    if row == n:
        print_solution(board, n)
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
                board[row][col] = 1
                if solve_n_queen(board, row + 1, n):
                 return True
                board[row][col] = 0

    return False

def print_solution(board, n):
    """
    Print the chessboard with queens placed.
    """
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print()

def n_queens(n):
    """
    Initialize the board and solve the N-Queens problem.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queen(board, 0, n):
        print("No solution exists.")

n = 6 
n_queens(n)


