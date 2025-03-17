"""
할로윈의 양아치
문제: https://www.acmicpc.net/problem/20303
"""
import sys
from collections import Counter

input = sys.stdin.readline

# 아이들의 총 수, 간선, 제한
n, m, k = map(int, input().split())

# 사탕
nums = [0] + list(map(int, input().split()))

# 부모 테이블
parent = [i for i in range(n+1)]

# find
def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

# union
def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    parent[max(a, b)] = min(a, b)

# 간선 입력
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

dic = Counter()
dic2 = Counter()

for i in range(1, n+1):
    # if i != parent[i]:
    parent[i] = find(i)
    dic[parent[i]] += 1
    dic2[parent[i]] += nums[i]

ls = [[j, dic2[i]] for i, j in dic.items()]

dp = [0] * (k+1)

for w, v in ls:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k-1])