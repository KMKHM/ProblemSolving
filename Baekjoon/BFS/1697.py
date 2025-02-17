"""
숨바꼭질
문제: https://www.acmicpc.net/problem/1697
"""
from collections import deque

# 수빈, 동생
n, k = map(int, input().split())

limit = 100_000 + 1

board = [0] * limit

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        cur = q.popleft()
        if cur == k:
            return board[k]

        for nx in [cur-1, cur+1, 2*cur]:
            if 0<=nx<limit and not board[nx]:
                board[nx] = board[cur] + 1
                q.append(nx)
print(bfs(n))

