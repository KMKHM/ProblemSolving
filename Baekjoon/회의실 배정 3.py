"""
https://www.acmicpc.net/problem/19622
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split()))[2] for i in range(n)]

if n == 1:
    print(arr[0])
    sys.exit(0)

# arr.sort()

dp = [0] * n
dp[0] = arr[0]
dp[1] = max(dp[0], arr[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i])

print(dp[-1])