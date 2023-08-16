"""
두 개의 탑
문제: https://www.acmicpc.net/problem/2118
"""
n = int(input())

distance = [int(input()) for _ in range(n)]

val = sum(distance)

# i에서 i+1로 가는 거리
for i in range(n):
    distance[i] = min(distance[i], val-distance[i])

print(distance)


