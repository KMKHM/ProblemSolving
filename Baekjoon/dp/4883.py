"""
삼각 그래프
문제: https://www.acmicpc.net/problem/4883
"""
import sys

input = sys.stdin.readline

idx=1

while True:
    n = int(input())

    if n == 0:
        sys.exit(0)

    graph = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):
        for j in range(3):
            if i == 1:
                graph[i][j] += graph[i - 1][1]
                continue
            if j == 0:
                graph[i][j] += min(graph[i-1][0], graph[i - 1][1])
            elif j == 1:
                graph[i][j] += min(graph[i-1][0], graph[i - 1][1], graph[i - 1][2])
            else:
                graph[i][j] += min(graph[i-1][1], graph[i-1][2])

    print(str(idx)+". " + str(graph[-1][1]))
    idx += 1