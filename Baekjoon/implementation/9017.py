"""
크로스 컨트리
문제: https://www.acmicpc.net/problem/9017
"""
import sys
from collections import Counter

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    possible = [i for i, j in Counter(nums).items() if j == 6]

    dic = dict(zip(possible, [0]*len(possible)))
    cnt = dict(zip(possible, [0]*len(possible)))

    final = dict()

    for idx, v in enumerate(i for i in nums if i in dic):
        if cnt[v] <= 3:
            dic[v] += (idx+1)
            cnt[v] += 1
        else:
            if v not in final:
                final[v] = (idx+1)

    fourth = [i for i, j in dic.items() if j == min(dic.values())]

    if len(fourth) == 1:
        print(fourth[0])
    else:
        val = min(final[i] for i in fourth)
        for i, j in final.items():
            if j == val:
                print(i)
                break