"""
단어 맞추기
문제: https://www.acmicpc.net/problem/9081
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = list(input().rstrip())
    length = len(s)

    # 가장 큰 인덱스값과 그 다음 큰 인덱스값
    a, b = 0, 0

    for i in range(1, length):
        if s[i] > s[i-1]:
            if a < i:
                a = i

    for i in range(1, length):
        if s[i] > s[a-1]:
            if b < i:
                b = i
    if a != 0 and b != 0:
        s[a-1], s[b] = s[b], s[a-1]
        print(s)
        s[a:] = sorted(s[a:])

    print("".join(s))
