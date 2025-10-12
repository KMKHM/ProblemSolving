"""
https://www.acmicpc.net/problem/11562
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dis = [[1e9]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dis[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c == 1:
        dis[a][b] = dis[b][a] = 0
    else:
        dis[a][b], dis[b][a] = 0, 1


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j] > dis[i][k] + dis[k][j]:
                dis[i][j] = dis[i][k] + dis[k][j]

k = int(input())

for _ in range(k):
    s, e = map(int, input().split())
    print(dis[s][e])
