"""
색종이 - 3
"""
board = [[0] * 100 for _ in range(100)]

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            board[i][j] = 1

for i in range(100):
    for j in range(100):
        if board[i][j]:
            pass
