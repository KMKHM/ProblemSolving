"""
할로윈의 양아치
문제: https://www.acmicpc.net/problem/20303
"""
import sys

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
    parent[x] = find(parent[x])
    return parent[x]

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

dic = dict()

for p in range(1, n+1):
    if parent[p] not in dic:
        dic[parent[p]] = 1
    else:
        dic[parent[p]] += 1

dic2 = dict()

for i in range(1, n+1):
    if parent[i] not in dic2:
        dic2[parent[i]] = nums[i]
    else:
        dic2[parent[i]] += nums[i]
print(dic)
print(dic2)

# dp = [[0]*k for _ in range(len(dic))]
#
# for node, val in dic.items():
#     for j in range(1, k):
#         weight = val
#         value = dic2[node]
#         if j < weight:
#             dp[val][j] = dp[val-1][j]
#         else:
#             dp[val][j] = max(dp[val-1][j], dp[val-1][j-weight] + value)
#
# print(dp)





