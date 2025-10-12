"""
https://www.acmicpc.net/problem/1633
"""
import sys
input = sys.stdin.readline

arr = []
while 1:
    nums = list(map(int, input().split()))
    if not nums:
        break
    arr.append(nums)

dp = [[0]*16 for _ in range(16)]

for wv, bv in arr:
    for w in range(15, -1, -1):
        for b in range(15, -1, -1):
            if w+1 <= 15:
                dp[w+1][b] = max(dp[w+1][b], dp[w][b] + wv)
            if b+1 <= 15:
                dp[w][b+1] = max(dp[w][b+1], dp[w][b] + bv)

print(dp[15][15])