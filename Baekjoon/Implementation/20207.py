"""
달력
문제: https://www.acmicpc.net/problem/20207
"""
import sys

input = sys.stdin.readline

n = int(input())

plan = []

plan = sorted(list(map(int, input().split())) for _ in range(n))

dic = dict()

for a, b in plan:
    for i in range(a, b+1):
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1


ans = 0

# 사각형의 가로, 세로
width = list(dic.keys())
height = list(dic.values())

tmp = width[0]
h, w = height[0], 1


for i in range(1, len(width)):
    if (tmp + 1) == width[i]:
        tmp = width[i]
        h = max(h, height[i])
        w += 1
    else:
        ans += (h*w)
        h = height[i]
        w = 1
        tmp = width[i]

ans += h*w

print(ans)