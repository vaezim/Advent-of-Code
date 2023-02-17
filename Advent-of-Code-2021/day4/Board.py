
def isWinning(mat):
    for i in range(len(mat)):
        ones = 0
        for j in range(len(mat[i])):
            ones += mat[i][j]
        if ones == len(mat[i]):
            return True
    for j in range(len(mat[0])):
        ones = 0
        for i in range(len(mat)):
            ones += mat[i][j]
        if ones == len(mat):
            return True
    return False

def findWinningBoard(boards, nums_called):
    filled_boards = [[[0]*len(boards[0][0]) for _ in range(len(boards[0]))] for _ in range(len(boards))]
    winningBoardIdx = float('inf')
    least_calls = float('inf')

    # finding the winning number for each board is faster
    for bIdx, board in enumerate(boards):
        curr_board = filled_boards[bIdx]
        for nIdx, n in enumerate(nums_called):

            FOUND = False
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == n:
                        curr_board[i][j] = 1
                        FOUND = True
                        break
                if FOUND: break
            if isWinning(curr_board):
                if nIdx < least_calls:
                    least_calls = nIdx
                    winningBoardIdx = bIdx
                break

    return winningBoardIdx, least_calls+1, filled_boards

def findWinningBoard2(boards, nums_called):
    filled_boards = [[[0]*len(boards[0][0]) for _ in range(len(boards[0]))] for _ in range(len(boards))]
    losingBoardIdx = float('-inf')
    most_calls = float('-inf')

    # finding the winning number for each board is faster
    for bIdx, board in enumerate(boards):
        curr_board = filled_boards[bIdx]

        for nIdx, n in enumerate(nums_called):
            FOUND = False
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == n:
                        curr_board[i][j] = 1
                        FOUND = True
                        break
                if FOUND: break
            if isWinning(curr_board):
                if nIdx > most_calls:
                    most_calls = nIdx
                    losingBoardIdx = bIdx
                break

    return losingBoardIdx, most_calls+1, filled_boards
    