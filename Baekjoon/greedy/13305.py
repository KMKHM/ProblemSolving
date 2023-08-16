"""
주유소
문제: https://www.acmicpc.net/problem/13305
"""
import sys

input = sys.stdin.readline

n = int(input())

distance = list(map(int, input().split()))

cost = list(map(int, input().split()))

min_cost = sys.maxsize

ans = 0

for i in range(n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
        ans += (min_cost * distance[i])
    else:
        ans += (min_cost * distance[i])
print(ans)
