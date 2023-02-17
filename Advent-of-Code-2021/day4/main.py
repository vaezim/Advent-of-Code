from Board import findWinningBoard, findWinningBoard2


with open('input.txt', 'r') as file:
    lines = file.readlines()

nums_called = lines[0].strip().split(',')

boards = []
for i, line in enumerate(lines[1:]):
    if line == '\n':
        boards.append([])
        continue

    boards[-1].append(line.strip().split())

##### Part 1 #####
winningBoardIdx, least_calls, filled_boards = findWinningBoard(boards, nums_called)
winningBoard = boards[winningBoardIdx]
filled = filled_boards[winningBoardIdx]

unmarkedSum = 0
for i in range(len(winningBoard)):
    for j in range(len(winningBoard[i])):
        if filled[i][j] == 0:
            unmarkedSum += int(winningBoard[i][j])
print(f"Answer of Part 1: {int(nums_called[least_calls-1]) * unmarkedSum}")

##### Part 2 #####
losingBoardIdx, most_calls, filled_boards = findWinningBoard2(boards, nums_called)
losingBoard = boards[losingBoardIdx]
filled = filled_boards[losingBoardIdx]

unmarkedSum = 0
for i in range(len(losingBoard)):
    for j in range(len(losingBoard[i])):
        if filled[i][j] == 0:
            unmarkedSum += int(losingBoard[i][j])
print(f"Answer of Part 2: {int(nums_called[most_calls-1]) * unmarkedSum}")
