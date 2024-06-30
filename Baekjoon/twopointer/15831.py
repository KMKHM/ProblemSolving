"""
준표의 조약돌
문제: https://www.acmicpc.net/problem/15831
"""
import sys

input = sys.stdin.readline

n, b, w = map(int, input().split())

s = input().rstrip()

ans = 0

black, white = 0, 0

start = 0

for end in range(n):

    if s[end] == "B":
        black += 1
    else:
        white += 1

    while b < black:
        if s[start] == "B":
            black -= 1
        else:
            white -= 1
        start += 1
    if white >= w:
        ans = max(ans, end - start + 1)

print(ans)