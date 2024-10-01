"""
빚
문제: https://www.acmicpc.net/problem/10427
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, *arr = map(int, input().split())

    arr.sort()

    arr = [0] + arr

    prefix = [0] * (n+1)

    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + arr[i]

    res = 0

    def solve(cnt):
        tmp = sys.maxsize
        for i in range(cnt, n+1):
            print(i)
            tmp = min(tmp, arr[i] * cnt - prefix[i] + prefix[i-cnt])
        return tmp

    for i in range(1, n+1):
        res += solve(i)

    print(res)