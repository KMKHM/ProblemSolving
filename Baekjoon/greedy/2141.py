"""
우체국
문제: https://www.acmicpc.net/problem/2141
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = []
people = 0


for _ in range(n):
    a, b = map(int, input().split())
    nums.append([a, b])
    people += b

nums.sort(key=lambda x: x[0])
cnt = 0

for i, j in nums:
    cnt += j
    if cnt >= people/2:
        print(i)
        break


