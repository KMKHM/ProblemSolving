import sys

input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

dp_min = [board[0]] * n
dp_max = [board[0]] * n

for i in range(1, n):
    dp_min[i][0] = board[i][0] + min(board[i-1][0], board[i-1][1])
    dp_min[i][1] = board[i][1] + min(board[i-1][0], board[i-1][1], board[i-1][2])
    dp_min[i][2] = board[i][2] + min(board[i-1][1], board[i-1][2])
    dp_max[i][0] = board[i][0] + max(board[i-1][0], board[i-1][1])
    dp_max[i][1] = board[i][1] + max(board[i-1][0], board[i-1][1], board[i-1][2])
    dp_max[i][2] = board[i][2] + max(board[i-1][1], board[i-1][2])

print(max(dp_max[n - 1][0], dp_max[n - 1][1], dp_max[n - 1][2]),min(dp_min[n - 1][0], dp_min[n - 1][1], dp_min[n - 1][2]))