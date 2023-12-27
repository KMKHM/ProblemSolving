"""
별 찍기 - 11
문제: https://www.acmicpc.net/problem/2448
"""

# 행의 수
row = int(input())
# 행의 수
r = row
k = 0

row //= 3

# k 구하기
while True:
    row //= 2
    k += 1
    if row == 1:
        break

# 열의 수 규칙
down = 5 * (2**k)
blank = (2**k) - 1

# 열의 수
c = down + blank

board = [[""]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        board[i][r-c-1] = "*"

for i in range(r):
    print(*board[i])