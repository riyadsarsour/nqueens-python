
def is_a_threat(board, row, col):

    # down right diagonal check
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 'Q':
            return True

    # down left diagonal check
    for i, j in zip(range(row, -1, -1), range(col, max_cols)):
        if board[i][j] == 'Q':
            return True

    # column check
    for r in range(row):
        if board[r][col] == 'Q':
            return True

    return False


def formatAns(board):
    for i in range(max_cols):
        print(board[i])
    print("\n")


def place_queens(board, row):
    if row == max_cols:
        global ans
        ans += 1
        formatAns(board)
        return
    for col in range(max_cols):
        if not is_a_threat(board, row, col):
            board[row][col] = 'Q'
            place_queens(board, row + 1)

            # to find other solution clear queen
            # backtrack and remove the queen from the current square
            board[row][col] = '0'
    None

    # place queen at every square in the current row `r`
    # and recur for each valid movement


if __name__ == "__main__":
    # execute only if run as a script
    max_cols = input("How many queens would you like to place?\n")
    board = [['0' for x in range(max_cols)] for y in range(max_cols)]
    ans = 0
    place_queens(board, 0)
    print("There are " + str(ans)+" solutions")
