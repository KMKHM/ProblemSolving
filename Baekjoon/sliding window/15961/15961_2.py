"""
회전 초밥
문제: https://www.acmicpc.net/problem/15961
"""
import sys
from collections import Counter

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr += arr

res = 0

i = 0
j = i+k-1


dic = Counter(arr[:i+k])

while i < n:
    if c not in dic: # 쿠폰이 딕셔너리에 없을때
        res = max(len(dic) + 1, res)
        # break
    else:
        res = max(res, len(dic))
        #
    dic[arr[i]] -= 1
    if not dic[arr[i]]:
        del dic[arr[i]]

    i += 1
    j += 1
    dic[arr[j]] += 1

print(res)