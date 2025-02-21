"""
할아버지는 유명해!
문제: https://www.acmicpc.net/problem/5766
"""
import sys
from collections import Counter

input = sys.stdin.readline

while 1:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        sys.exit(0)

    dic = Counter()

    for _ in range(n):
        nums = list(map(int, input().split()))
        for num in nums:
            dic[num] += 1


    res = []

    second = sorted(set(dic.values()))[-2]

    for i, j in dic.items():
        if j == second:
            res.append(i)

    print(*sorted(res))



