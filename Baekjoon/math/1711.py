"""
직각 삼각형
문제: https://www.acmicpc.net/problem/1711
"""
import sys

input = sys.stdin.readline

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            dot1, dot2, dot3 = points[i], points[j], points[k]

            d1 = (dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2
            d2 = (dot2[0]-dot3[0])**2 + (dot2[1]-dot3[1])**2
            d3 = (dot3[0]-dot1[0])**2 + (dot3[1]-dot1[1])**2

            max_val = max(d1, d2, d3)

            if 2 * max_val == d1 + d2 + d3:
                cnt += 1

print(cnt)