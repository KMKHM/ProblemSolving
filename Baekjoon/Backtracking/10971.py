"""
외판원 순회 2
문제: https://www.acmicpc.net/problem/10971
"""
import sys

input = sys.stdin.readline

n = int(input())

weight = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n

ans = sys.maxsize

def bt(start, now, val, cnt):
    global ans

    if val > ans:
        return

    if cnt == n and weight[now][start]:
        val += weight[now][start]
        ans = min(ans, val)
        return

    for i in range(n):
        if not visited[i] and weight[now][i]:
            visited[i] = 1
            bt(start, i, val + weight[now][i], cnt + 1)
            visited[i] = 0

for node in range(n):
    visited[node] = 1
    bt(node, node, 0, 1)
    visited[node] = 0

print(ans)