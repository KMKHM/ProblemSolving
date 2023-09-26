"""
N-Queen
문제: https://www.acmicpc.net/problem/9663
"""
n = int(input())

board = [0] * n

ans = 0

# 놓을 수 있는지 판단하는 함수
def check(x):
    for i in range(x):
        if board[i] == board[x] or abs(i-x) == abs(board[i] - board[x]):
            return False
    return True

# 백트래킹
def bt(x):
    global ans

    if x == n:
        ans += 1
        return

    for i in range(n):
        board[x] = i
        if check(x):
            bt(x + 1)

bt(0)

print(ans)