"""
평범한 배낭
문제: https://www.acmicpc.net/problem/12865
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

"""
2차원 DP
"""
items = [tuple(map(int, input().split())) for _ in range(n)]
DynamicProgramming = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight, value = items[i-1][0], items[i-1][1]
    for j in range(1, k+1):
        if j < weight:
            DynamicProgramming[i][j] = DynamicProgramming[i-1][j]
        else:
            DynamicProgramming[i][j] = max(DynamicProgramming[i-1][j], DynamicProgramming[i-1][j-weight] + value)

print(DynamicProgramming[-1][-1])


"""
1차원 DP
"""
# dp = [0] * (k+1)
#
# for i in range(n):
#     weight, value = map(int, input().split())
#     for j in range(k, weight-1, -1):
#         dp[j] = max(dp[j], dp[j-weight] + value)
#     print(dp)
#
# print(dp[k])