"""
꽃길
문제: https://www.acmicpc.net/problem/14620
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)


visited = [[0] * n for _ in range(n)]

def check(a, b):
    for i in range(4):
        na, nb = a + dx[i], b + dy[i]
        if visited[na][nb]:
            return False
    return True

tmp = 0

def bt(level):
    global ans, tmp

    if level == 3:
        ans = min(ans, tmp)
        return

    for i in range(1, n-1):
        for j in range(1, n-1):
            if check(i, j):
                visited[i][j] = 1
                tmp += nums[i][j]
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    visited[nx][ny] = 1
                    tmp += nums[nx][ny]

                bt(level + 1)

                visited[i][j] = 0
                tmp -= nums[i][j]
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    visited[nx][ny] = 0
                    tmp -= nums[nx][ny]

bt(0)

print(ans)
