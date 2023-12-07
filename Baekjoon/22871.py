"""
징검다리 건너기 (large)
문제: https://www.acmicpc.net/problem/22871
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

def power(a, b):
    return (b - a) * (1 + abs(nums[a]-nums[b]))

dp = [sys.maxsize] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        # j -> i로 가는 힘중 최대값을 구하고
        tmp = max(power(j, i), dp[j])
        # 그 중 최소값을 기록
        dp[i] = min(tmp, dp[i])

print(dp[-1])
