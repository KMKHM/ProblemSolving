"""
치킨 배달
문제: https://www.acmicpc.net/problem/15686
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 집
home = []

# 치킨집
chicken = []

# 도시
city = []

for i in range(n):
    row = list(map(int, input().split()))
    city.append(row)
    for j in range(n):
        if row[j] == 1:
            home.append([i, j])
        if row[j] == 2:
            chicken.append([i, j])

def getDistance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

visited = [[0] * n for _ in range(n)]



