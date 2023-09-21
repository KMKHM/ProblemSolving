"""
개똥벌레
문제: https://www.acmicpc.net/problem/3020
"""
import sys
input = sys.stdin.readline

n, h = map(int, input().split())

board = [0] * h

for i in range(n):
    # 크기
    m = int(input())
    # 짝수번쨰
    if i % 2 == 0:
        for k in range(m):
            board[k] += 1

    # 홀수번째
    else:
        for k in range(h-1, h-m-1, -1):
            board[k] += 1

val = min(board)

ans = 0

for num in board:
    if num == val:
        ans += 1

print(val, ans)




