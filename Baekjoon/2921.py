"""
도영이가 만든 맛있는 음식
문제: https://www.acmicpc.net/problem/2961
"""
import sys

input = sys.stdin.readline

n = int(input())

ans = sys.maxsize

ingredient = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n

res = []

def cal(arr):
    tmp1, tmp2 = 1, 0
    for a, b in arr:
        tmp1 *= a
        tmp2 += b
    return abs(tmp1-tmp2)
def bt(idx):
    global ans

    if idx > 0:
        ans = min(ans, cal(res))

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            res.append(ingredient[i])
            bt(idx+1)
            res.pop()
            visited[i] = 0

bt(0)

print(ans)